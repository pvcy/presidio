from unittest import TestCase

from tests import assert_result_within_score_range
from presidio_analyzer.predefined_recognizers import UsItinRecognizer
from pandas import Series
from presidio_analyzer import Column

us_itin_recognizer = UsItinRecognizer()
entities = ["US_ITIN"]


class TestUsItinRecognizer(TestCase):

    def test_valid_us_itin_very_weak_match(self):
        num1 = '911-701234'
        num2 = '91170-1234'
        results = us_itin_recognizer.analyze(
            '{} {}'.format(num1, num2), entities)

        assert len(results) == 2

        assert results[0].score != 0
        assert_result_within_score_range(
            results[0], entities[0], 0, 10, 0, 0.3)

        assert results[1].score != 0
        assert_result_within_score_range(
            results[1], entities[0], 11, 21, 0, 0.3)

    def test_valid_us_itin_weak_match(self):
        num = '911701234'
        results = us_itin_recognizer.analyze(num, entities)

        assert len(results) == 1
        assert_result_within_score_range(
            results[0], entities[0], 0, 9, 0.3, 0.4)

    def test_valid_us_itin_medium_match(self):
        num = '911-70-1234'
        results = us_itin_recognizer.analyze(num, entities)

        assert len(results) == 1
        assert_result_within_score_range(
            results[0], entities[0], 0, 11, 0.5, 0.6)

    def test_invalid_us_itin(self):
        num = '911-89-1234'
        results = us_itin_recognizer.analyze(num, entities)

        assert len(results) == 0

    def test_invalid_us_itin_exact_context(self):
        num = '911-89-1234'
        context = "my taxpayer id"
        results = us_itin_recognizer.analyze(
            '{} {}'.format(context, num), entities)

        assert len(results) == 0

    # Column tests

    def test_column_valid_us_itin_very_weak_match_no_title(self):
        col = Column(Series([
            '911-701234',
            '91170-1234',
        ]))

        result_group = us_itin_recognizer.analyze(col, entities)
        assert len(result_group.recognizer_results) == 2

        for result in result_group.recognizer_results:
            assert result.score != 0
            assert_result_within_score_range(
                result, entities[0], 0, 10, 0, 0.3)

    def test_column_valid_us_itin_mixed_match_no_title(self):
        col = Column(Series([
            '911-701234',   # very weak
            '911701234',    # weak
            '911-70-1234',  # medium
        ]))

        result_group = us_itin_recognizer.analyze(col, entities)
        assert len(result_group.recognizer_results) == 3

        assert_result_within_score_range(
            result_group.recognizer_results[0], entities[0], 0, 10, 0, 0.3)
        assert_result_within_score_range(
            result_group.recognizer_results[1], entities[0], 0, 9, 0.3, 0.4)
        assert_result_within_score_range(
            result_group.recognizer_results[2], entities[0], 0, 11, 0.5, 0.6)

    def test_column_valid_us_itin_mixed_match_with_relevant_title(self):
        col = Column(Series([
            '911-701234',   # very weak
            '911701234',    # weak
            '911-70-1234'   # medium
        ], name='ITIN'))

        result_group = us_itin_recognizer.analyze(col, entities)
        assert len(result_group.recognizer_results) == 3

        assert_result_within_score_range(
            result_group.recognizer_results[0], entities[0], 0, 10, 0.7, 1)
        assert_result_within_score_range(
            result_group.recognizer_results[1], entities[0], 0, 9, 1, 1)
        assert_result_within_score_range(
            result_group.recognizer_results[2], entities[0], 0, 11, 1, 1)

    def test_column_valid_us_itin_mixed_match_and_nonmatch(self):
        col = Column(Series([
            '911-701234',   # very weak
            '911701234',    # weak
            '911-70-1234',  # medium
            '911-89-1234',  # invalid
        ]))

        result_group = us_itin_recognizer.analyze(col, entities)
        assert result_group is None

    def test_column_valid_us_itin_mixed_match_with_irrelevant_title(self):
        col = Column(Series([
            '911-701234',   # very weak
            '911701234',    # weak
            '911-70-1234',  # medium
        ], name='userid'))

        result_group = us_itin_recognizer.analyze(col, entities)
        assert result_group is None
