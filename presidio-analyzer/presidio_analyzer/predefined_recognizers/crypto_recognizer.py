from hashlib import sha256
from presidio_analyzer import Pattern, PatternRecognizer

# Copied from:
# http://rosettacode.org/wiki/Bitcoin/address_validation#Python


class CryptoRecognizer(PatternRecognizer):
    """
    Recognizes common crypto account numbers using regex + checksum
    """

    PATTERNS = [
        Pattern("Crypto (Medium)", r"\b[13][a-km-zA-HJ-NP-Z1-9]{26,33}\b", 0.5),
    ]

    CONTEXT = ["wallet", "btc", "bitcoin", "crypto"]

    def __init__(
        self,
        patterns=None,
        context=None,
        supported_language="en",
        supported_entity="CRYPTO",
    ):
        patterns = patterns if patterns else self.PATTERNS
        title_patterns = [Pattern('Crypto Title (Strong)',  # language=RegExp
                                  r'\b(wallet|btc|bitcoin|crypto)\b',
                                  0.7)]
        context = context if context else self.CONTEXT
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            title_patterns=title_patterns,
            context=context,
            supported_language=supported_language,
        )

    def validate_result(self, pattern_text):
        try:
            bcbytes = self.__decode_base58(pattern_text, 25)
            return bcbytes[-4:] == sha256(sha256(bcbytes[:-4]).digest()).digest()[:4]
        except ValueError:
            return False

    @staticmethod
    def __decode_base58(bc, length):
        digits58 = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
        n = 0
        for char in bc:
            n = n * 58 + digits58.index(char)
        return n.to_bytes(length, "big")
