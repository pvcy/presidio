import pytest

from tests import assert_result_within_score_range
from presidio_analyzer.predefined_recognizers import UsPassportRecognizer
from pandas import Series
from presidio_analyzer import Column


@pytest.fixture(scope="module")
def recognizer():
    return UsPassportRecognizer()


@pytest.fixture(scope="module")
def entities():
    return ["US_PASSPORT"]


@pytest.mark.parametrize(
    "text, expected_len, expected_positions, expected_score_ranges",
    [
        ("912803456", 1, ((0, 9),), ((0.0, 0.1),),),
        # requires multiword context
        # ("my travel document is 912803456", 1, ((22, 31),), ((.5, 0.6),),),
    ],
)
def test_all_us_passports(
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

def test_column_valid_us_passport_no_title(recognizer, entities):
    col = Column(Series([
        '912803456',
        '432552424',
        '467325534'
    ]))
    result_group = recognizer.analyze(col, entities)

    assert result_group is not None
    assert len(result_group.recognizer_results) == 3

    for result in result_group.recognizer_results:
        assert result.score != 0
        assert_result_within_score_range(
            result, entities[0], 0, 9, 0, 0.1)

def test_column_valid_us_passport_with_title(recognizer, entities):
    col = Column(Series([
        '912803456',
        '432552424',
        '467325534'
    ], name='passport'))
    result_group = recognizer.analyze(col, entities)

    assert result_group is not None
    assert len(result_group.recognizer_results) == 3

    for result in result_group.recognizer_results:
        assert result.score != 0
        assert_result_within_score_range(
            result, entities[0], 0, 9, 0.7, 0.8)

def test_column_mixed_valid_and_invalid_us_passport_with_related_title(recognizer, entities):
    col = Column(Series([
        '912803456',
        '432552424',
        '467325534',
        '4412238896'
    ], name='passport'))
    result_group = recognizer.analyze(col, entities)

    assert result_group is None
