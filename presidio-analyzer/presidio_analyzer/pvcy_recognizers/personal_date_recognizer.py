from presidio_analyzer import Pattern
from presidio_analyzer import PatternRecognizer

# language=RegExp
REGEX = r'''(?:[0-3]?\d(?:st|nd|rd|th)?\s+(?:of\s+)?(?:jan\.?|january|feb\.?|february|mar\.?|march|apr\.?|april|may|jun\.?|june|jul\.?|july|aug\.?|august|sep\.?|september|oct\.?|october|nov\.?|november|dec\.?|december)
            |(?:jan\.?|january|feb\.?|february|mar\.?|march|apr\.?|april|may|jun\.?|june|jul\.?|july|aug\.?|august|sep\.?|september|oct\.?|october|nov\.?|november|dec\.?|december)\s+[0-3]?\d(?:st|nd|rd|th)?)(?:\,)?\s*(?:\d{4})?
            |[0-3]?\d[-\./][0-3]?\d[-\./]\d{2,4}
            |\d{2,4}[-\.\/][0-3]?\d[-\.\/][0-3]?\d''' # NB Requires re.VERBOSE

CONTEXT = ['birth', 'birthday', 'dob', 'd.o.b', 'd/o/b', 'born', 'died', 'death', 'deceased']

class PersonalDateRecognizer(PatternRecognizer):

    def __init__(self):
        patterns = [Pattern('Personal Date (very weak)', REGEX, 0.02)]
        title_patterns = [Pattern('Personal Date Title [birthday] (strong)',    # language=RegExp
                                  r'(date[\s_-]?of[\s_-]?birth|dob|birth[\s_-]?(date|day)|d\.o\.b\.?|bday|born)',
                                  0.7),
                          Pattern('Personal Date Title [death] (strong)',       # language=RegExp
                                  r'(date[\s_-]of[\s_-]death|dateofdeath|death_date|deathdate|deceased|died)',
                                  0.7)]
        super().__init__(supported_entity="PERSONAL_DATE", patterns=patterns,
                         title_patterns=title_patterns,
                         context=CONTEXT)
