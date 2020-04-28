from presidio_analyzer import Pattern
from presidio_analyzer import PatternRecognizer

# language=RegExp
REGEX = r'\b([a-z0-9]{6,7}|[a-z0-9]{2}[\s_-][a-z0-9]{3,5}|[a-z0-9]{3}[\s_-][a-z0-9]{3,4})\b'
CONTEXT = [] # TODO

class LicensePlateRecognizer(PatternRecognizer):

    def __init__(self):
        patterns = [Pattern('US License Plate (weak)', REGEX, 0.05)]
        title_patterns = [Pattern('US License Plate Title (strong)',  # language=RegExp
                                  r'\b(lic(ense)?[\s_-](plate|num(ber)?|#)|plate[\s_-](num(ber)?|#))\b',
                                  0.7)]
        super().__init__(supported_entity="US_LICENSE_PLATE", patterns=patterns,
                         title_patterns=title_patterns,
                         context=CONTEXT)
