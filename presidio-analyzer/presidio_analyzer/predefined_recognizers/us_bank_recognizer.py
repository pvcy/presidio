from presidio_analyzer import Pattern, PatternRecognizer


class UsBankRecognizer(PatternRecognizer):
    """
    Recognizes US bank number using regex
    """

    PATTERNS = [
        Pattern("Bank Account (weak)", r"\b[0-9]{8,17}\b", 0.05,),
    ]

    CONTEXT = [
        "bank"
        # Task #603: Support keyphrases: change to "checking account"
        # as part of keyphrase change
        "check",
        "account",
        "account#",
        "acct",
        "save",
        "debit",
    ]

    def __init__(
        self,
        patterns=None,
        context=None,
        supported_language="en",
        supported_entity="US_BANK_NUMBER",
    ):
        patterns = patterns if patterns else self.PATTERNS
        title_patterns = [Pattern('Bank account title (strong)',  # language=RegExp
                                  r'\b(bank|check(ing)?|savings|account|acct|debit)(#|num(ber)?)?\b',
                                  0.7)]
        context = context if context else self.CONTEXT
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            title_patterns=title_patterns,
            context=context,
            supported_language=supported_language,
        )
