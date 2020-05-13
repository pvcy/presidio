from presidio_analyzer import Pattern
from presidio_analyzer import PatternRecognizer
from stdnum import imei

# language=RegExp
REGEX = r'^[0-9]{14,15}$' # IMEI 14/15-digit decimal (without/with check digit)

CONTEXT = [] # TODO

class IMEIRecognizer(PatternRecognizer):

    def __init__(self):
        patterns = [Pattern('IMEI (weak)', REGEX, 0.1)]
        title_patterns = [Pattern('IMEI Title (strong)',  # language=RegExp
                                  r'\b((phone|device|mobile|cell)[\s_-]?id|IMEI)\b',
                                  0.7)]
        super().__init__(supported_entity="IMEI", patterns=patterns,
                         title_patterns=title_patterns,
                         context=CONTEXT)

    def validate_result(self, pattern_text):
        if len(pattern_text) == 15:
            return imei.is_valid(pattern_text)

        return None # 14-digit IMEI has no validation mechanism
