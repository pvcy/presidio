from unittest import TestCase

from tests import assert_result_within_score_range
from presidio_analyzer.predefined_recognizers import UsPassportRecognizer
from pandas import Series
from presidio_analyzer import Column

us_passport_recognizer = UsPassportRecognizer()
entities = ["US_PASSPORT"]


class TestUsPassportRecognizer(TestCase):

    def test_valid_us_passport_no_context(self):
        num = '912803456'
        results = us_passport_recognizer.analyze(num, entities)

        assert len(results) == 1
        assert results[0].score != 0
        assert_result_within_score_range(results[0], entities[0], 0, 9, 0, 0.1)

    #  Task #603: Support keyphrases: Should pass after handling keyphrases, e.g. "travel document" or "travel permit"

    # def test_valid_us_passport_with_exact_context_phrase():
    #     num = '912803456'
    #     context = 'my travel document number is '
    #     results = us_passport_recognizer.analyze(context + num, entities)
    #
    #     assert len(results) == 1
    #     assert results[0].text = num
    #     assert results[0].score
    #

    # Column tests

    def test_column_valid_us_passport_no_title(self):
        col = Column(Series([
            '912803456',
            '432552424',
            '467325534'
        ]))
        result_group = us_passport_recognizer.analyze(col, entities)

        assert result_group is not None
        assert len(result_group.recognizer_results) == 3

        for result in result_group.recognizer_results:
            assert result.score != 0
            assert_result_within_score_range(
                result, entities[0], 0, 9, 0, 0.1)

    def test_column_valid_us_passport_with_title(self):
        col = Column(Series([
            '912803456',
            '432552424',
            '467325534'
        ], name='passport'))
        result_group = us_passport_recognizer.analyze(col, entities)

        assert result_group is not None
        assert len(result_group.recognizer_results) == 3

        for result in result_group.recognizer_results:
            assert result.score != 0
            assert_result_within_score_range(
                result, entities[0], 0, 9, 0.7, 0.8)

    def test_column_mixed_valid_and_invalid_us_passport_with_related_title(self):
        col = Column(Series([
            '912803456',
            '432552424',
            '467325534',
            '4412238896'
        ], name='passport'))
        result_group = us_passport_recognizer.analyze(col, entities)

        assert result_group is None
