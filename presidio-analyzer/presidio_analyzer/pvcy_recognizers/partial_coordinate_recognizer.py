from presidio_analyzer import Pattern
from presidio_analyzer import PatternRecognizer

REGEX = r'\b(\d{2,7}\.(\d{1}|\d{2}|\d{5}))\b' # https://en.wikipedia.org/wiki/ISO_6709#String_expression_.28Annex_H.29
CONTEXT = [] # TODO


class PartialCoordinateRecognizer(PatternRecognizer):

    def __init__(self):
        patterns = [Pattern('Partial Coordinate (weak)', REGEX, 0.3)]
        title_patterns = [Pattern('Partial Coordinate Title (strong)', # language=RegExp
                                  r'\b(lat|latitude|lon|long|longitude)\b',
                                  0.7)]
        super().__init__(supported_entity="PARTIAL_COORDINATE", patterns=patterns,
                         title_patterns=title_patterns,
                         context=CONTEXT)
