from presidio_analyzer import Pattern
from presidio_analyzer import PatternRecognizer

REGEX = r'[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?)(,\s*|\s+)[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)' # ISO 6709-ish
TITLE_REGEX = r'\b(loc|location|co-?ordinates?|coords|(geo(graphy)?[\s_-]?)?point|lat[\s_-]?lo?ng|pos(ition)?)\b'
CONTEXT = [] # TODO

class CooridateRecognizer(PatternRecognizer):

    def __init__(self):
        patterns = [Pattern('Coordinate (medium)', REGEX, 0.5)]
        title_patterns = [Pattern('Coordinate Title (strong)', TITLE_REGEX, 0.7)]
        super().__init__(supported_entity="COORDINATE", patterns=patterns,
                         title_patterns=title_patterns,
                         context=CONTEXT)
