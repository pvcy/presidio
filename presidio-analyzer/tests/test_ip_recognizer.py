import pytest

from tests import assert_result_within_score_range
from presidio_analyzer.predefined_recognizers import IpRecognizer
from pandas import Series
from presidio_analyzer import Column

@pytest.fixture(scope="module")
def recognizer():
    return IpRecognizer()


@pytest.fixture(scope="module")
def entities():
    return ["IP_ADDRESS"]


@pytest.mark.parametrize(
    "text, expected_len, expected_positions, expected_score_ranges",
    [
        # IPv4 tests
        ("microsoft.com 192.168.0.1", 1, ((14, 25),), ((0.6, 0.81),),),
        ("my ip: 192.168.0", 0, (), (),),
        # IPv6 tests  TODO IPv6 regex needs to be fixed
        # ("microsoft.com 684D:1111:222:3333:4444:5555:6:77", 1, ((14, 46),), ((0.59, 0.81),),),  # noqa: E501
        # ("my ip: 684D:1111:222:3333:4444:5555:6:77", 1, ((7, 39),), ((0.79, "max"),),),  # noqa: E501
        ("684D:1111:222:3333:4444:5555:77", 0, (), (),),
    ],
)
def test_all_ips(
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

def test_column_valid_ipv4_no_title(recognizer, entities):
    col = Column(Series([
        '192.168.0.1',
        '192.168.1.100'
    ]))

    result_group = recognizer.analyze(col, entities)
    assert len(result_group.recognizer_results) == 2
    assert_result_within_score_range(result_group.recognizer_results[0],
        entities[0], 0, 11, 0.6, 0.81)
    assert_result_within_score_range(result_group.recognizer_results[1],
        entities[0], 0, 13, 0.6, 0.81)

def test_column_valid_ipv4_with_relevant_title(recognizer, entities):
    col = Column(Series([
        '192.168.0.1',
        '192.168.1.100'
    ], name='IP'))

    result_group = recognizer.analyze(col, entities)
    assert len(result_group.recognizer_results) == 2
    assert_result_within_score_range(result_group.recognizer_results[0],
        entities[0], 0, 11, 1, 1)
    assert_result_within_score_range(result_group.recognizer_results[1],
        entities[0], 0, 13, 1, 1)
