from presidio_analyzer import Pattern
from presidio_analyzer import PatternRecognizer

# language=RegExp
REGEX = r'\b[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}\b'
CONTEXT = []  # TODO

class AdvertizingIDRecognizer(PatternRecognizer):

    def __init__(self):
        patterns = [Pattern('Advertising ID (medium)', REGEX, 0.5)]
        title_patterns = [Pattern('Advertising ID Title (strong)',  # language=RegExp
                                  r'(id?fa|(aa|as|ad|advertising)[\s_-]?(id|key|identifier))',
                                  0.7)]
        super().__init__(supported_entity="ADVERTISING_ID", patterns=patterns,
                         title_patterns=title_patterns,
                         context=CONTEXT)
