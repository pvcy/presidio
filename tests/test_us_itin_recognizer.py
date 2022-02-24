import pytest

from tests import assert_result_within_score_range
from presidio_analyzer.predefined_recognizers import UsItinRecognizer
from pandas import Series
from presidio_analyzer import Column


@pytest.fixture(scope="module")
def recognizer():
    return UsItinRecognizer()


@pytest.fixture(scope="module")
def entities():
    return ["US_ITIN"]


@pytest.mark.parametrize(
    "text, expected_len, expected_positions, expected_score_ranges",
    [
        ("911-701234 91170-1234", 2, ((0, 10), (11, 21),), ((0.0, 0.3), (0.0, 0.3),),),
        ("911701234", 1, ((0, 9),), ((0.3, 0.4),),),
        ("911-70-1234", 1, ((0, 11),), ((0.5, 0.6),),),
        ("911-89-1234", 0, (), (),),
        ("my tax id 911-89-1234", 0, (), (),),
    ],
)
def test_all_us_itins(
    text,
    expected_len,
    expected_positions,
    expected_score_ranges,
    recognizer,
    entities,
    max_score,
):
    results = recognizer.analyze(text, entities)
    assert len(results) == expected_len
    for res, (st_pos, fn_pos), (st_score, fn_score) in zip(
        results, expected_positions, expected_score_ranges
    ):
        if fn_score == "max":
            fn_score = max_score
        assert_result_within_score_range(
            res, entities[0], st_pos, fn_pos, st_score, fn_score
        )

# Column tests

def test_column_valid_us_itin_very_weak_match_no_title(recognizer, entities):
    col = Column(Series([
        '911-701234',
        '91170-1234',
    ]))

    result_group = recognizer.analyze(col, entities)
    assert len(result_group.recognizer_results) == 2

    for result in result_group.recognizer_results:
        assert result.score != 0
        assert_result_within_score_range(
            result, entities[0], 0, 10, 0, 0.3)

def test_column_valid_us_itin_mixed_match_no_title(recognizer, entities):
    col = Column(Series([
        '911-701234',   # very weak
        '911701234',    # weak
        '911-70-1234',  # medium
    ]))

    result_group = recognizer.analyze(col, entities)
    assert len(result_group.recognizer_results) == 3

    assert_result_within_score_range(
        result_group.recognizer_results[0], entities[0], 0, 10, 0, 0.3)
    assert_result_within_score_range(
        result_group.recognizer_results[1], entities[0], 0, 9, 0.3, 0.4)
    assert_result_within_score_range(
        result_group.recognizer_results[2], entities[0], 0, 11, 0.5, 0.6)

def test_column_valid_us_itin_mixed_match_with_relevant_title(recognizer, entities):
    col = Column(Series([
        '911-701234',   # very weak
        '911701234',    # weak
        '911-70-1234'   # medium
    ], name='ITIN'))

    result_group = recognizer.analyze(col, entities)
    assert len(result_group.recognizer_results) == 3

    assert_result_within_score_range(
        result_group.recognizer_results[0], entities[0], 0, 10, 0.7, 1)
    assert_result_within_score_range(
        result_group.recognizer_results[1], entities[0], 0, 9, 1, 1)
    assert_result_within_score_range(
        result_group.recognizer_results[2], entities[0], 0, 11, 1, 1)

def test_column_valid_us_itin_mixed_match_and_nonmatch(recognizer, entities):
    col = Column(Series([
        '911-701234',   # very weak
        '911701234',    # weak
        '911-70-1234',  # medium
        '911-89-1234',  # invalid
    ]))

    result_group = recognizer.analyze(col, entities)
    assert result_group is None

def test_column_valid_us_itin_mixed_match_with_irrelevant_title(recognizer, entities):
    col = Column(Series([
        '911-701234',   # very weak
        '911701234',    # weak
        '911-70-1234',  # medium
    ], name='userid'))

    result_group = recognizer.analyze(col, entities)
    assert result_group is None
