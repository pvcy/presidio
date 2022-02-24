import pytest

from tests import assert_result_within_score_range
from presidio_analyzer.predefined_recognizers import UsSsnRecognizer


@pytest.fixture(scope="module")
def recognizer():
    return UsSsnRecognizer()


@pytest.fixture(scope="module")
def entities():
    return ["US_SSN"]


@pytest.mark.parametrize(
    "text, expected_len, expected_positions, expected_score_ranges",
    [
        # very weak match TODO figure out why this fails
        # ("078-05112 07805-112", 2, ((0, 10), (11, 21),), ((0.0, 0.3), (0.0, 0.3),),),
        # weak match
        ("078051121", 1, ((0, 9),), ((0.3, 0.4),),),
        # medium match
        ("078-05-1123", 1, ((0, 11),), ((0.5, 0.6),),),
        ("078.05.1123", 1, ((0, 11),), ((0.5, 0.6),),),
        ("078 05 1123", 1, ((0, 11),), ((0.5, 0.6),),),
        # no match
        ("0780511201", 0, (), (),),
        ("078051120", 0, (), (),),
        ("000000000", 0, (), (),),
        ("666000000", 0, (), (),),
        ("078-05-0000", 0, (), (),),
        ("078 00 1123", 0, (), (),),
        ("693-09.4444", 0, (), (),),
    ],
)
def test_all_us_ssns(
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
# TODO If single-delimiter SSNs should be valid, fix SSN invalidator, and
#  update tests to include them again.

from pandas import Series
from presidio_analyzer import Column

# def test_column_valid_us_ssn_very_weak_match_no_title(recognizer):
#     col = Column(Series(['078-051120', '07805-1120']))
#     result_group = recognizer.analyze(
#         col, entities)
#
#     assert result_group is not None
#     assert len(result_group.recognizer_results) == 2
#
#     for result in result_group.recognizer_results:
#         assert result.score != 0
#         assert_result_within_score_range(
#             result, entities[0], 0, 10, 0, 0.3)

def test_column_valid_us_ssn_mixed_match_no_title(recognizer, entities):
    col = Column(Series([
        # '078-051121',   # very weak
        '078051121',    # weak
        '078-05-1121'   # medium
    ]))
    result_group = recognizer.analyze(
        col, entities)

    assert result_group is not None
    assert len(result_group.recognizer_results) == 2
    # assert_result_within_score_range(
    #     result_group.recognizer_results[0],
    #     entities[0], 0, 10, 0, 0.3)
    assert_result_within_score_range(
        result_group.recognizer_results[0],
        entities[0], 0, 9, 0.3, 0.4)
    assert_result_within_score_range(
        result_group.recognizer_results[1],
        entities[0], 0, 11, 0.49, 0.6)

def test_column_valid_us_ssn_mixed_with_related_title(recognizer, entities):
    col = Column(Series([
        # '078-051121',   # very weak
        '078051121',    # weak
        '078-05-1121'   # medium
    ], name='SSN'))
    result_group = recognizer.analyze(
        col, entities)

    assert result_group is not None
    assert len(result_group.recognizer_results) == 2

    # assert_result_within_score_range(
    #     result_group.recognizer_results[0],
    #     entities[0], 0, 10, 0.75, 0.8)
    assert result_group.recognizer_results[0].score == 1
    assert result_group.recognizer_results[1].score == 1

def test_column_mixed_valid_and_invalid_us_ssn(recognizer, entities):
    col = Column(Series([
        # '078-051121',   # very weak
        '078051121',    # weak
        '078-05-1121',  # medium
        '078-05-11201'  # invalid
    ]))
    result_group = recognizer.analyze(
        col, entities)

    assert result_group is None
