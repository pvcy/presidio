from presidio_analyzer import Pattern
from presidio_analyzer import PatternRecognizer

# pylint: disable=line-too-long,abstract-method
# Weak pattern: all passport numbers are a weak match, e.g., 14019033
REGEX = r'\b[0-9]{8,17}\b'

CONTEXT = [
    "bank"
    # Task #603: Support keyphrases: change to "checking account"
    # as part of keyphrase change
    "check",
    "account",
    "account#",
    "acct",
    "save",
    "debit"
]


class UsBankRecognizer(PatternRecognizer):
    """
    Recognizes US bank number using regex
    """

    def __init__(self):
        patterns = [Pattern('Bank Account (weak)', REGEX, 0.05)]
        title_patterns = [Pattern('Bank account title (strong)', # language=RegExp
                                  r'\b(bank|check(ing)?|savings|account|acct|debit)(#|num(ber)?)?\b',
                                  0.7)]
        super().__init__(supported_entity="US_BANK_NUMBER",
                         patterns=patterns,
                         title_patterns=title_patterns,
                         context=CONTEXT)
