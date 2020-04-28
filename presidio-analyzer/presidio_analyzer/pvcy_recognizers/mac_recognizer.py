from presidio_analyzer import Pattern
from presidio_analyzer import PatternRecognizer


# language=RegExp
REGEX = r'^([0-9A-Fa-f]{2}[:]){5}([0-9A-Fa-f]{2})$'

CONTEXT = [] # TODO

class MACRecognizer(PatternRecognizer):

    def __init__(self):
        patterns = [Pattern('MAC Address (medium)', REGEX, 0.5)]
        title_patterns = [Pattern('MAC Address Title (strong)',  # language=RegExp
                                  r'\b((phone|device|computer)[\s_-]?id|MAC)\b',
                                  0.7)]
        super().__init__(supported_entity="MAC_ADDRESS", patterns=patterns,
                         title_patterns=title_patterns,
                         context=CONTEXT)

