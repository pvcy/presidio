import pytest

from tests import assert_result
from presidio_analyzer.predefined_recognizers import UsBankRecognizer
from pandas import Series
from presidio_analyzer import Column


@pytest.fixture(scope="module")
def recognizer():
    return UsBankRecognizer()


@pytest.fixture(scope="module")
def entities():
    return ["US_BANK_NUMBER"]


@pytest.mark.parametrize(
    "text, expected_len, expected_positions, expected_score",
    [
        # valid bank accounts
        ("945456787654", 1, ((0, 12),), 0.05),
        # invalid bank accounts
        ("1234567", 0, (), -1.0),
    ],
)
def test_all_us_banks(
    text, expected_len, expected_positions, expected_score, recognizer, entities
):
    results = recognizer.analyze(text, entities)
    assert len(results) == expected_len
    for res, (st_pos, fn_pos) in zip(results, expected_positions):
        assert_result(res, entities[0], st_pos, fn_pos, expected_score)


# Column tests

def test_column_us_bank_account_no_title(recognizer, entities):
    col = Column(Series([
        '945456787654',
        '4164714570235',
        '98407500'
    ]))
    result_group = recognizer.analyze(col, entities)

    assert len(result_group.recognizer_results) == 3
    assert_result(result_group.recognizer_results[0], entities[0], 0, 12, 0.05)
    assert_result(result_group.recognizer_results[1], entities[0], 0, 13, 0.05)
    assert_result(result_group.recognizer_results[2], entities[0], 0, 8, 0.05)

def test_column_us_bank_account_with_relevant_title(recognizer, entities):
    col = Column(Series([
        '945456787654',
        '4164714570235',
        '98407500'
    ], name='acctnum'))
    result_group = recognizer.analyze(col, entities)

    assert len(result_group.recognizer_results) == 3
    assert_result(result_group.recognizer_results[0], entities[0], 0, 12, 0.75)
    assert_result(result_group.recognizer_results[1], entities[0], 0, 13, 0.75)
    assert_result(result_group.recognizer_results[2], entities[0], 0, 8, 0.75)

def test_column_us_bank_account_valid_and_invalid_no_title(recognizer, entities):
    col = Column(Series([
        '945456787654',
        '4164714570235',
        '98407500',
        '1234567'   #invalid
    ], name='acctnum'))
    result_group = recognizer.analyze(col, entities)

    assert result_group is None
