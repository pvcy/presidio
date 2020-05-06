from presidio_analyzer import Pattern
from presidio_analyzer import PatternRecognizer

# pylint: disable=line-too-long,abstract-method
# Weak pattern: all passport numbers are a weak match, e.g., 14019033
VERY_WEAK_REGEX = r'(\b[0-9]{9}\b)'


CONTEXT = [
    "us", "united", "states", "passport", "passport#", "travel",
    "document"
]


class UsPassportRecognizer(PatternRecognizer):
    """
    Recognizes US Passport number using regex
    """

    def __init__(self):
        patterns = [Pattern('Passport (very weak)', VERY_WEAK_REGEX, 0.05)]
        title_patterns = [Pattern('Passport title (strong)',
                                  r'\b(passport(\snum(ber)?|#)?)\b',
                                  0.7)]
        super().__init__(supported_entity="US_PASSPORT", patterns=patterns,
                         title_patterns=title_patterns,
                         context=CONTEXT)
