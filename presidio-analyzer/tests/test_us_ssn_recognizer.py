from tests import assert_result_within_score_range
from presidio_analyzer.predefined_recognizers import UsSsnRecognizer

us_ssn_recognizer = UsSsnRecognizer()
entities = ["US_SSN"]


def test_valid_us_ssn_very_weak_match():
    num1 = '078-051120'
    num2 = '07805-1120'
    results = us_ssn_recognizer.analyze(
        '{} {}'.format(num1, num2), entities)

    assert len(results) == 2

    assert results[0].score != 0
    assert_result_within_score_range(
        results[0], entities[0], 0, 10, 0, 0.3)

    assert results[0].score != 0
    assert_result_within_score_range(
        results[1], entities[0], 11, 21, 0, 0.3)


def test_valid_us_ssn_weak_match():
    num = '078051120'
    results = us_ssn_recognizer.analyze(num, entities)

    assert len(results) == 1
    assert results[0].score != 0
    assert_result_within_score_range(
        results[0], entities[0], 0, 9, 0.3, 0.4)


def test_valid_us_ssn_medium_match():
    num = '078-05-1120'
    results = us_ssn_recognizer.analyze(num, entities)

    assert len(results) == 1
    assert results[0].score != 0
    assert_result_within_score_range(
        results[0], entities[0], 0, 11, 0.5, 0.6)
    assert 0.49 < results[0].score < 0.6


def test_invalid_us_ssn():
    num = '078-05-11201'
    results = us_ssn_recognizer.analyze(num, entities)

    assert len(results) == 0

# Column tests

from pandas import Series
from presidio_analyzer import Column

def test_column_valid_us_ssn_very_weak_match_no_title():
    col = Column(Series(['078-051120', '07805-1120']))
    result_group = us_ssn_recognizer.analyze(
        col, entities)

    assert result_group is not None
    assert len(result_group.recognizer_results) == 2

    for result in result_group.recognizer_results:
        assert result.score != 0
        assert_result_within_score_range(
            result, entities[0], 0, 10, 0, 0.3)

def test_column_valid_us_ssn_mixed_match_no_title():
    col = Column(Series([
        '078-051120',   # very weak
        '078051120',    # weak
        '078-05-1120'   # medium
    ]))
    result_group = us_ssn_recognizer.analyze(
        col, entities)

    assert result_group is not None
    assert len(result_group.recognizer_results) == 3
    assert_result_within_score_range(
        result_group.recognizer_results[0],
        entities[0], 0, 10, 0, 0.3)
    assert_result_within_score_range(
        result_group.recognizer_results[1],
        entities[0], 0, 9, 0.3, 0.4)
    assert_result_within_score_range(
        result_group.recognizer_results[2],
        entities[0], 0, 11, 0.49, 0.6)

def test_column_valid_us_ssn_mixed_with_related_title():
    col = Column(Series([
        '078-051120',   # very weak
        '078051120',    # weak
        '078-05-1120'   # medium
    ], name='SSN'))
    result_group = us_ssn_recognizer.analyze(
        col, entities)

    assert result_group is not None
    assert len(result_group.recognizer_results) == 3

    assert_result_within_score_range(
        result_group.recognizer_results[0],
        entities[0], 0, 10, 0.75, 0.8)
    assert result_group.recognizer_results[1].score == 1
    assert result_group.recognizer_results[2].score == 1

def test_column_mixed_valid_and_invalid_us_ssn():
    col = Column(Series([
        '078-051120',   # very weak
        '078051120',    # weak
        '078-05-1120',  # medium
        '078-05-11201'  # invalid
    ]))
    result_group = us_ssn_recognizer.analyze(
        col, entities)

    assert result_group is None
