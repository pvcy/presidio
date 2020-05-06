from . import AnalysisExplanation


class RecognizerResult:

    def __init__(self, entity_type, start, end, score,
                 analysis_explanation: AnalysisExplanation = None,
                 **kwargs):
        """
        Recognizer Result represents the findings of the detected entity
        of the analyzer in the text.
        :param index: corresponding source text index
        :param entity_type: the type of the entity
        :param start: the start location of the detected entity
        :param end: the end location of the detected entity
        :param score: the score of the detection
        :param analysis_explanation: contains the explanation of why this
                                     entity was identified
        """
        self.index = kwargs.get('index', None)
        self.entity_type = entity_type
        self.start = start
        self.end = end
        self.score = score
        self.analysis_explanation = analysis_explanation

    def append_analysis_explenation_text(self, text):
        if self.analysis_explanation:
            self.analysis_explanation.append_textual_explanation_line(text)

    def to_json(self):
        return str(self.__dict__)

    def __str__(self):
        return "type: {}, " \
               "start: {}, " \
               "end: {}, " \
               "score: {}".format(self.entity_type,
                                  self.start,
                                  self.end,
                                  self.score)

    def __repr(self):
        return self.__str__()

    def intersects(self, other):
        """
        Checks if self intersects with a different RecognizerResult
        :return: If interesecting, returns the number of
        intersecting characters.
        If not, returns 0
        """

        # if they do not overlap the intersection is 0
        if self.end < other.start or other.end < self.start:
            return 0

        # otherwise the intersection is min(end) - max(start)
        return min(self.end, other.end) - max(self.start, other.start)

    def contained_in(self, other):
        """
        Checks if self is contained in a different RecognizerResult
        :return: true if contained
        """

        return self.start >= other.start and self.end <= other.end


class RecognizerResultGroup(RecognizerResult):
    """
    Class representing grouped results (i.e. column).
    TODO
        Determine behavior for comparisons across sets.
        Extend RecognizerResult to handle column-specific metadata (i.e. index)
        Temp solution:
        - Initialize Base class attributes to best scoring result from group
        - Short circuit all overlap-type operations to False
    """

    def __init__(self, recognizer_results):
        self.recognizer_results = recognizer_results
        best_scoring = max(recognizer_results, key=lambda r: r.score)
        super().__init__(**best_scoring.__dict__)

    def to_json(self):
        return str({ 'recognizer_results' : [str(r) for r in self.recognizer_results]})

    def intersects(self, other):
        return False

    def contained_in(self, other):
        return False
