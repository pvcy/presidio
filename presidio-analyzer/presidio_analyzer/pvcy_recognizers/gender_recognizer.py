from presidio_analyzer import Pattern
from presidio_analyzer import PatternRecognizer

REGEX = r'\b(m|male|f|female|nb|non[-\s]?binary)\b'
CONTEXT = [] # TODO

class GenderRecognizer(PatternRecognizer):

    def __init__(self):
        patterns = [Pattern('Gender (medium)', REGEX, 0.5)]
        title_patterns = [Pattern('Gender Title (strong)', # language=RegExp
                                  r'\b(gender|sex)\b',
                                  0.7)]
        super().__init__(supported_entity="GENDER", patterns=patterns,
                         title_patterns=title_patterns,
                         context=CONTEXT)
