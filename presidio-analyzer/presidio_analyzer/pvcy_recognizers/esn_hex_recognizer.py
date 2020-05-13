from presidio_analyzer import Pattern
from presidio_analyzer import PatternRecognizer

# language=RegExp
REGEX = r'^[0-9a-fA-F]{8}$' # Hex ESN (eight digit mixed case hex)

CONTEXT = [] # TODO

class ESNHexRecognizer(PatternRecognizer):

    def __init__(self):
        patterns = [Pattern('ESN Hex (weak)', REGEX, 0.1)]
        title_patterns = [Pattern('ESN Hex Title (strong)',  # language=RegExp
                                  r'\b((phone|device|mobile|cell)[\s_-]?id|ESN)\b',
                                  0.7)]
        super().__init__(supported_entity="ESNHEX_ID", patterns=patterns,
                         title_patterns=title_patterns,
                         context=CONTEXT)

