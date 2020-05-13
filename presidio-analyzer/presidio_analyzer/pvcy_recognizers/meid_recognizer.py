from presidio_analyzer import Pattern
from presidio_analyzer import PatternRecognizer
from stdnum import meid

# language=RegExp
REGEX = r'^([0-9a-fA-F]{14,15}|[0-9]{18})$' # MEID 14/15-digit hex & 18-digit decimal

CONTEXT = [] # TODO

class MEIDRecognizer(PatternRecognizer):

    def __init__(self):
        patterns = [Pattern('MEID (weak)', REGEX, 0.2)]
        title_patterns = [Pattern('MEID Title (strong)',  # language=RegExp
                                  r'\b((phone|device|mobile|cell)[\s_-]?id|MEID)\b',
                                  0.7)]
        super().__init__(supported_entity="MEID", patterns=patterns,
                         title_patterns=title_patterns,
                         context=CONTEXT)

    def validate_result(self, pattern_text):
        return meid.is_valid(pattern_text)
