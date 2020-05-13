import datetime

from typing import Mapping
from presidio_analyzer import LocalRecognizer, \
    Pattern, \
    RecognizerResult, \
    EntityRecognizer, \
    AnalysisExplanation, \
    EntitySource, Text

# Import 're2' regex engine if installed, if not- import 'regex'
try:
    import re2 as re
except ImportError:
    import regex as re


class PatternRecognizer(LocalRecognizer):

    def __init__(self, supported_entity, name=None,
                 supported_language='en',
                 patterns=None,
                 title_patterns=None,
                 black_list=None, context=None, version="0.0.1"):
        """
            :param patterns: the list of patterns to detect entity
            :param title_patterns: list of patterns to detect entity-related source title
            :param black_list: the list of words to detect
            :param context: list of context words
        """
        if not supported_entity:
            raise ValueError(
                "Pattern recognizer should be initialized with entity")

        if not patterns and not black_list:
            raise ValueError(
                "Pattern recognizer should be initialized with patterns"
                " or with black list")

        super().__init__(supported_entities=[supported_entity],
                         supported_language=supported_language,
                         name=name,
                         version=version)

        self.patterns = [] or patterns
        self.title_patterns = [] or title_patterns
        self.context = context

        if black_list:
            black_list_pattern = PatternRecognizer.__black_list_to_regex(
                black_list)
            self.patterns.append(black_list_pattern)
            self.black_list = black_list
        else:
            self.black_list = []

    def load(self):
        pass

    # pylint: disable=unused-argument
    def analyze(self, entity_source, entities, nlp_artifacts=None):

        entity_source = self.__standardize_source(entity_source)
        results = self.__analyze_patterns(entity_source, self.patterns, self.validate_result)

        if results:
            if entity_source.text_has_context and self.context:
            # try to improve the results score using the surrounding
            # context words
                results = self.enhance_using_context(
                    entity_source, results, nlp_artifacts, self.context)

            if entity_source.title and self.title_patterns:
            # Refine results scores using source title and title patterns
                results = self.__enhance_using_patterns(
                    self.__standardize_source(entity_source.title),
                    results, self.title_patterns)

        return entity_source.postprocess_results(results)

    @staticmethod
    def __standardize_source(source):
        """
        Upgrade strings to Text (maintaining backward compatibility,
        passthrough other EntitySources, fail unsupported source types.
        """
        if issubclass(type(source), EntitySource):
            return source
        elif type(source) is str:
            return Text(source)
        else:
            raise ValueError(f"Unsupported type ({type(source)}) used"
                             "as input to PatternRecognizer analyzer.")

    @staticmethod
    def __black_list_to_regex(black_list):
        """
        Converts a list of word to a matching regex, to be analyzed by the
         regex engine as a part of the analyze logic

        :param black_list: the list of words to detect
        :return:the regex of the words for detection
        """
        regex = r"(?:^|(?<= ))(" + '|'.join(black_list) + r")(?:(?= )|$)"
        return Pattern(name="black_list", regex=regex, score=1.0)

    # pylint: disable=unused-argument, no-self-use, assignment-from-none
    def validate_result(self, pattern_text):
        """
        Validates the pattern logic, for example by running
         checksum on a detected pattern.

        :param pattern_text: the text to validated.
        Only the part in text that was detected by the regex engine
        :return: A bool indicating whether the validation was successful.
        """
        return None

    @staticmethod
    def build_regex_explanation(
            recognizer_name,
            pattern_name,
            pattern,
            original_score,
            validation_result):
        explanation = AnalysisExplanation(recognizer=recognizer_name,
                                          original_score=original_score,
                                          pattern_name=pattern_name,
                                          pattern=pattern,
                                          validation_result=validation_result)
        return explanation

    def __analyze_patterns(self, entity_source: Mapping[int, str], patterns, validator=None):
        """
        Evaluates all patterns in the provided text, including words in
         the provided blacklist

        :param entity_source: EntitySource to analyze
        :param patterns: Patterns to match against source
        :param validator: Function to validate match
        :return: A list of RecognizerResult

        TODO:
            Should text list handling move up to AnalyzerEngine?
            Is there a more OOP way to reuse this logic across contexts?
        """
        results = []
        for i, t in entity_source.items():
            for pattern in patterns:
                match_start_time = datetime.datetime.now()
                matches = re.finditer(
                    pattern.regex,
                    t,
                    flags=re.IGNORECASE | re.DOTALL | re.MULTILINE | re.VERBOSE)
                match_time = datetime.datetime.now() - match_start_time
                self.logger.debug('--- match_time[%s]: %s.%s seconds',
                                  pattern.name,
                                  match_time.seconds,
                                  match_time.microseconds)

                for match in matches:
                    start, end = match.span()
                    current_match = t[start:end]

                    # Skip empty results
                    if current_match == '':
                        continue

                    score = pattern.score

                    validation_result = validator(current_match) if validator else None
                    description = PatternRecognizer.build_regex_explanation(
                        self.name,
                        pattern.name,
                        pattern.regex,
                        score,
                        validation_result
                    )
                    pattern_result = RecognizerResult(
                        self.supported_entities[0],
                        start,
                        end,
                        score,
                        analysis_explanation=description,
                        index=i
                    )

                    if validation_result is not None:
                        if validation_result:
                            pattern_result.score = EntityRecognizer.MAX_SCORE
                        else:
                            pattern_result.score = EntityRecognizer.MIN_SCORE

                    if pattern_result.score > EntityRecognizer.MIN_SCORE:
                        results.append(pattern_result)

        return results

    def to_dict(self):
        return_dict = super().to_dict()

        return_dict["patterns"] = [pat.to_dict() for pat in self.patterns]
        return_dict["black_list"] = self.black_list
        return_dict["context"] = self.context
        return_dict["supported_entity"] = return_dict["supported_entities"][0]
        del return_dict["supported_entities"]

        return return_dict

    @classmethod
    def from_dict(cls, entity_recognizer_dict):
        patterns = entity_recognizer_dict.get("patterns")
        if patterns:
            patterns_list = [Pattern.from_dict(pat) for pat in patterns]
            entity_recognizer_dict['patterns'] = patterns_list

        return cls(**entity_recognizer_dict)

    def __enhance_using_patterns(self, source_text, results, patterns):
        """
         TODO More accurate name than "enhance" => enrich/improve/refine
        """
        if not source_text or not patterns:
            # Nothing to match or nothing to match with => passthrough
            return results

        enhancement_results = self.__analyze_patterns(source_text, patterns)
        if enhancement_results and source_text:
            best_match = max(enhancement_results, key=lambda r: r.score)
            best_score = best_match.score
            for result in results:
                result.score = min(
                    result.score + best_score,
                    EntityRecognizer.MAX_SCORE
                )
                result.analysis_explanation.set_supportive_context_word(source_text) # NB Leaky abstraction
                result.analysis_explanation.set_improved_score(result.score)

            return results # No results are returned if nothing matches
            # TODO Demote result scores on no match instead of remove?
            # TODO Decouple Column-specific behavior (removing/demoting score) from this function.
