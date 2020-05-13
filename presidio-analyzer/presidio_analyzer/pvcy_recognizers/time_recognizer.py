from presidio_analyzer import Pattern
from presidio_analyzer import PatternRecognizer

# language=RegExp
REGEX = r"\b((1[0-2]|0?[1-9])|(2[0-3]|[01]?[0-9])):([0-5]?[0-9])(\s?[AP]M?)?(:[0-5]?[0-9]([:.,*]\d{1,7})?)?(\s?'?[-+]\d{4}'?)?\b"

CONTEXT = []

class TimeRecognizer(PatternRecognizer):
    """
    TODO Update to match on Python DateTime serialized string format and other
        standard DT string serializations.
    """
    def __init__(self):
        patterns = [Pattern('Time (strong)', REGEX, 0.7)]
        title_patterns = [Pattern('Time title (strong)',
                                  r'\b(time)\b',
                                  0.7)]
        super().__init__(supported_entity="TIME", patterns=patterns,
                         title_patterns=title_patterns,
                         context=CONTEXT)
