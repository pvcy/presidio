from presidio_analyzer import Pattern
from presidio_analyzer import PatternRecognizer
from stdnum.us import itin, ein, ptin

# language=RegExp
REGEX_SSN_OR_ITIN = r'\b([0-9]{3})-([0-9]{2})-([0-9]{4})\b'
# language=RegExp
REGEX_EIN_VERY_WEAK = r'\b[0-9]{9}\b'
# language=RegExp
REGEX_EIN_WEAK = r'\b[0-9]{2}-[0-9]{7}\b'
# language=RegExp
REGEX_PTIN_WEAK = r'\bP-?[0-9]{8}\b'

CONTEXT = []

class UsTaxIDRecognizer(PatternRecognizer):
    """
    TODO Reusable recognizer logic. ex: A SSN is a valid US Tax ID, but it's
        also a separate recognizer. This recognizer should be able to match
        a SSN without duplicating the logic in another recognizer.
    """
    def __init__(self):
        patterns = [Pattern('US Tax ID [SSN/ITIN] (weak)', REGEX_SSN_OR_ITIN, 0.2),
                    Pattern('US Tax ID [EIN] (very weak)', REGEX_EIN_VERY_WEAK, 0.05),
                    Pattern('US Tax ID [EIN] (weak)', REGEX_EIN_WEAK, 0.2),
                    Pattern('US Tax ID [PTIN] (weak)', REGEX_EIN_WEAK, 0.3)]
        title_patterns = [Pattern('US Tax ID title (strong)',   # language=RegExp
                                  r'\b(tax[\s_-]id|ein|itin|ptin)\b',
                                  0.7)]
        super().__init__(supported_entity="US_TAX_ID", patterns=patterns,
                         title_patterns=title_patterns,
                         context=CONTEXT)

    def validate_result(self, pattern_text):
        """
        Force SSN to depend on title/context (to prevent from outscoring an SSN match)
        """
        for mod in (itin, ein, ptin):
            if mod.is_valid(pattern_text):  # NB stdnum applies a duplicate regex match
                return True

