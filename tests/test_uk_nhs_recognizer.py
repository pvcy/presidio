import pytest

from tests import assert_result
from presidio_analyzer.predefined_recognizers import NhsRecognizer
from pandas import Series
from presidio_analyzer import Column

nhs_recognizer = NhsRecognizer()
entities = ["UK_NHS"]


@pytest.fixture(scope="module")
def recognizer():
    return NhsRecognizer()


@pytest.fixture(scope="module")
def entities():
    return ["UK_NHS"]


@pytest.mark.parametrize(
    "text, expected_len, expected_positions",
    [
        # valid NHS scores
        ("401-023-2137", 1, ((0, 12),),),
        ("221 395 1837", 1, ((0, 12),),),
        ("0032698674", 1, ((0, 10),),),
        # invalid NHS scores
        ("401-023-2138", 0, ()),
    ],
)
def test_all_uk_nhses(
    text, expected_len, expected_positions, recognizer, entities, max_score
):
    results = recognizer.analyze(text, entities)
    assert len(results) == expected_len
    for res, (st_pos, fn_pos) in zip(results, expected_positions):
        assert_result(res, entities[0], st_pos, fn_pos, max_score)


# Column tests

def test_column_valid_uk_nhs_mixed_no_title(entities):
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
