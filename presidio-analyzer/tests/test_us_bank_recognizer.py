from unittest import TestCase

from tests import assert_result
from presidio_analyzer.predefined_recognizers import UsBankRecognizer
from pandas import Series
from presidio_analyzer import Column

us_bank_recognizer = UsBankRecognizer()
entities = ["US_BANK_NUMBER"]


class TestUsBankRecognizer(TestCase):

    def test_us_bank_account_invalid_number(self):
        num = '1234567'
        results = us_bank_recognizer.analyze(num, entities)

        assert len(results) == 0

    def test_us_bank_account_no_context(self):
        num = '945456787654'
        results = us_bank_recognizer.analyze(num, entities)

        assert len(results) == 1
        assert_result(results[0], entities[0], 0, 12, 0.05)


    # Column tests

    def test_column_us_bank_account_no_title(self):
        col = Column(Series([
            '945456787654',
            '4164714570235',
            '98407500'
        ]))
        result_group = us_bank_recognizer.analyze(col, entities)

        assert len(result_group.recognizer_results) == 3
        assert_result(result_group.recognizer_results[0], entities[0], 0, 12, 0.05)
        assert_result(result_group.recognizer_results[1], entities[0], 0, 13, 0.05)
        assert_result(result_group.recognizer_results[2], entities[0], 0, 8, 0.05)

    def test_column_us_bank_account_with_relevant_title(self):
        col = Column(Series([
            '945456787654',
            '4164714570235',
            '98407500'
        ], name='acctnum'))
        result_group = us_bank_recognizer.analyze(col, entities)

        assert len(result_group.recognizer_results) == 3
        assert_result(result_group.recognizer_results[0], entities[0], 0, 12, 0.75)
        assert_result(result_group.recognizer_results[1], entities[0], 0, 13, 0.75)
        assert_result(result_group.recognizer_results[2], entities[0], 0, 8, 0.75)

    def test_column_us_bank_account_valid_and_invalid_no_title(self):
        col = Column(Series([
            '945456787654',
            '4164714570235',
            '98407500',
            '1234567'   #invalid
        ], name='acctnum'))
        result_group = us_bank_recognizer.analyze(col, entities)

        assert result_group is None
