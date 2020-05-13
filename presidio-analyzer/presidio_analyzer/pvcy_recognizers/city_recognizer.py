from presidio_analyzer import Pattern
from presidio_analyzer import PatternRecognizer

REGEX = r'^\p{L}+(?:([\ \-\']|(\.\ ))\p{L}+)*$'
CONTEXT = []    # TODO

class CityRecognizer(PatternRecognizer):

    def __init__(self):
        patterns = [Pattern('City (weak)', REGEX, 0.05)]
        title_patterns = [Pattern('City Title (strong)',  # language=RegExp
                                  r'\b(city|town)\b',
                                  0.7)]
        super().__init__(supported_entity="CITY", patterns=patterns,
                         title_patterns=title_patterns,
                         context=CONTEXT)
