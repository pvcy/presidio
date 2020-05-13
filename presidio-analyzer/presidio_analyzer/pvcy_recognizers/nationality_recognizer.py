from presidio_analyzer import Pattern
from presidio_analyzer import PatternRecognizer
from presidio_analyzer import PresidioLogger
import csv, itertools
from pathlib import Path

# Sources:
# List of nationalities CSV file
# https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/664133/CH_Nationality_List_20171130_v1.csv/preview
# Geographical names CSV file
# https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/678684/CH_Country_List_20180124.csv/preview

NAT_NAMES_FILE = Path(__file__).parent.absolute()/'CH_Nationality_List_20171130_v1.csv'
GEO_NAMES_FILE = Path(__file__).parent.absolute()/'CH_Country_List_20180124.csv'

CONTEXT = []

class NationalityRecognizer(PatternRecognizer):
    """
    TODO Simple keyword-based recognizer. Regex performance is likely to degrade
        with long lists. Patterns that are simply long alterination groups should
        be replaced with matching against a set-like data structure.
    """

    def __init__(self):
        with open(NAT_NAMES_FILE) as nat_names, \
            open(GEO_NAMES_FILE) as geo_names:
            nat_list = [i for r in csv.reader(nat_names, quotechar='"') for i in r]
            geo_list = [i for r in csv.reader(geo_names, quotechar='"') for i in r]

        nationality_regex = self.__build_list_regex(nat_list, geo_list)

        patterns = [Pattern('Nationality (strong)', nationality_regex, 0.7)]
        title_patterns = [Pattern('Nationality Title (strong)',  # language=RegExp
                                  r'\b(country|nation(ality)?)\b',
                                  0.7)]
        super().__init__(supported_entity="NATIONALITY", patterns=patterns,
                         title_patterns=title_patterns,
                         context=CONTEXT)

    @staticmethod
    def __build_list_regex(*lists):
        return fr"\b(?:{'|'.join(itertools.chain.from_iterable(lists))})\b"
