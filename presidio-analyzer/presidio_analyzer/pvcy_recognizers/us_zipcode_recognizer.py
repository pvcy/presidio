from presidio_analyzer import Pattern
from presidio_analyzer import PatternRecognizer

REGEX_WEAK = r'\b(\d{5})\b'
REGEX_MEDIUM = r'\b(\d{5}-\d{4})\b'
CONTEXT = [] # TODO

class UsZipcodeRecognizer(PatternRecognizer):

    def __init__(self):
        patterns = [Pattern('US Zip Code (weak)', REGEX_WEAK, 0.1),
                    Pattern('US Zip Code (medium)', REGEX_WEAK, 0.5)]
        title_patterns = [Pattern('US Zip Code Title (strong)',  # language=RegExp
                                  r'\b(zip|zip[\s_-]?code|postal|postal[\s_-]?code)\b',
                                  0.7)]
        super().__init__(supported_entity="US_ZIPCODE", patterns=patterns,
                         title_patterns=title_patterns,
                         context=CONTEXT)
