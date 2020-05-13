from presidio_analyzer import Pattern
from presidio_analyzer import PatternRecognizer

# language=RegExp
REGEX = r'^[0-9]{11}$'

CONTEXT = [] # TODO

class ESNDecRecognizer(PatternRecognizer):

    def __init__(self):
        patterns = [Pattern('ESN Decimal (very weak)', REGEX, 0.05)]
        title_patterns = [Pattern('ESN Decimal Title (strong)',  # language=RegExp
                                  r'\b((phone|device|mobile|cell)[\s_-]?id|ESN)\b',
                                  0.7)]
        super().__init__(supported_entity="ESNDEC_ID", patterns=patterns,
                         title_patterns=title_patterns,
                         context=CONTEXT)

    def validate_result(self, pattern_text):
        return (int(pattern_text[0:3]) <= 255 # first three digits are the manufacturer code
                and int(pattern_text[3:11] <= 16777215)) # last eight digits is the serial number
