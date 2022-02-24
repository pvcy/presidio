import pytest

from presidio_analyzer.predefined_recognizers import UsPhoneRecognizer
from tests import assert_result_within_score_range
from pandas import Series
from presidio_analyzer import Column


@pytest.fixture(scope="module")
def recognizer():
    return UsPhoneRecognizer()


@pytest.fixture(scope="module")
def entities():
    return ["PHONE_NUMBER"]


@pytest.mark.parametrize(
    "text, expected_len, expected_positions, expected_score_ranges",
    [
        ("(425) 882 9090", 1, ((0, 14),), ((0.7, "max"),),),
        ("my phone number is: 110bcd25-a55d-453a-8046-1297901ea002", 0, (), (),),
        ("I am available at (425) 882-9090", 1, ((18, 32),), ((0.69, "max"),),),
        ("This is just a sentence (425) 882-9090", 1, ((24, 38),), ((0.69, "max"),),),
        ("425 8829090", 1, ((0, 11),), ((0.45, 0.6),),),
        ("This is just a sentence 425 8829090", 1, ((24, 35),), ((0.29, 0.51),),),
        ("4258829090", 1, ((0, 10),), ((0.0, 0.3),),),
    ],
)
def test_all_phone_numbers(
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

def test_columns_phone_number_strong_match_no_title(recognizer, max_score, entities):
    col = Column(Series([
        '(425) 882 9090',
        '(512) 449 8898',
        '(713) 335 8867'
    ]))
    result_group = recognizer.analyze(col, entities)

    assert result_group is not None
    assert len(result_group.recognizer_results) == 3

    for result in result_group.recognizer_results:
        assert result.score != 0
        assert_result_within_score_range(
            result, entities[0], 0, 14, 0.7, max_score)


def test_columns_phone_number_mixed_match_no_title(recognizer, max_score, entities):
    col = Column(Series([
        '(425) 882 9090',   # strong
        '425 8829090',      # medium
        '4258829090'        # weak
    ]))
    result_group = recognizer.analyze(col, entities)

    assert result_group is not None
    assert len(result_group.recognizer_results) == 3

    assert_result_within_score_range(
        result_group.recognizer_results[0],
        entities[0], 0, 14, 0.7, max_score)
    assert_result_within_score_range(
        result_group.recognizer_results[1],
        entities[0], 0, 11, 0.45, 0.6)
    assert_result_within_score_range(
        result_group.recognizer_results[2],
        entities[0], 0, 10, 0, 0.3)

def test_columns_phone_number_mixed_match_with_related_title(recognizer, max_score, entities):
    col = Column(Series([
        '(425) 882 9090',   # strong
        '425 8829090',      # medium
        '4258829090'        # weak
    ], name='phone_num'))
    result_group = recognizer.analyze(col, entities)

    assert result_group is not None
    assert len(result_group.recognizer_results) == 3

    assert_result_within_score_range(
        result_group.recognizer_results[0],
        entities[0], 0, 14,
        max_score,
        max_score)
    assert_result_within_score_range(
        result_group.recognizer_results[1],
        entities[0], 0, 11,
        max_score,
        max_score)
    assert_result_within_score_range(
        result_group.recognizer_results[2],
        entities[0], 0, 10, 0.7, 0.75)

def test_columns_phone_number_mixed_matching_and_nonmatch(recognizer, entities):
    col = Column(Series([
        '(425) 882 9090',   # strong
        '425 8829090',      # medium
        '4258829090',       # weak
        '441552213'         # non match
    ], name='phone_num'))
    result_group = recognizer.analyze(col, entities)

    assert result_group is None
