from unittest import TestCase

from tests import assert_result
from presidio_analyzer.predefined_recognizers import NhsRecognizer
from presidio_analyzer.entity_recognizer import EntityRecognizer
from pandas import Series
from presidio_analyzer import Column

nhs_recognizer = NhsRecognizer()
entities = ["UK_NHS"]


class TestNhsRecognizer(TestCase):

    def test_valid_uk_nhs_with_dashes(self):
        num = '401-023-2137'
        results = nhs_recognizer.analyze(num, entities)

        assert len(results) == 1
        assert_result(results[0], entities[0], 0, 12, 1.0)

    def test_valid_uk_nhs_with_spaces(self):
        num = '221 395 1837'
        results = nhs_recognizer.analyze(num, entities)

        assert len(results) == 1
        assert_result(results[0], entities[0], 0, 12, 1.0)

    def test_valid_uk_nhs_with_no_delimeters(self):
        num = '0032698674'
        results = nhs_recognizer.analyze(num, entities)

        assert len(results) == 1
        assert_result(results[0], entities[0], 0, 10, 1.0)

    def test_invalid_uk_nhs(self):
        num = '401-023-2138'
        results = nhs_recognizer.analyze(num, entities)

        assert len(results) == 0


    # Column tests

    def test_column_valid_uk_nhs_mixed_no_title(self):
        col = Column(Series([
            '401-023-2137',
            '221 395 1837',
            '0032698674'
        ]))
        result_group = nhs_recognizer.analyze(col, entities)

        assert len(result_group.recognizer_results) == 3
        assert_result(result_group.recognizer_results[0], entities[0], 0, 12, 1.0)
        assert_result(result_group.recognizer_results[1], entities[0], 0, 12, 1.0)
        assert_result(result_group.recognizer_results[2], entities[0], 0, 10, 1.0)
