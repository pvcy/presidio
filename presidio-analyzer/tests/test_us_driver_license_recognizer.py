import pytest

from presidio_analyzer.predefined_recognizers import UsLicenseRecognizer
from tests import assert_result_within_score_range
from pandas import Series
from presidio_analyzer import Column


@pytest.fixture(scope="module")
def recognizer():
    return UsLicenseRecognizer()


@pytest.fixture(scope="module")
def entities():
    return ["US_DRIVER_LICENSE"]


@pytest.mark.parametrize(
    "text, expected_len, expected_positions, expected_score_ranges",
    [
        # WA license tests
        (
            "AA1B2**9ABA7 A*1234AB*CD9",
            2,
            ((0, 12), (13, 25),),
            ((0.3, 0.4), (0.3, 0.4),),
        ),
        ("3A1B2**9ABA7", 0, (), (),),
        # Other states license weak tests
        ("H12234567", 1, ((0, 9),), ((0.3, 0.4),),),
        ("C12T345672", 0, (), (),),
        # invalid license that should fail, but doesn't do to context
        # ("my driver's license is C12T345672", 0, (), (),),
        # Other states license very weak tests
        (
            "123456789 1234567890 12345679012 123456790123 1234567901234 1234",
            5,
            ((0, 9), (10, 20), (21, 32), (33, 45), (46, 59),),
            ((0.0, 0.02), (0.0, 0.02), (0.0, 0.02), (0.0, 0.02), (0.0, 0.02),),
        ),
        ("ABCDEFG ABCDEFGH ABCDEFGHI", 0, (), (),),
        ("ABCD ABCDEFGHIJ", 0, (), (),),
        # The following fails due to keyphrases not yet supported
        # ("my driver license: ABCDEFG", 1, ((19, 25),), ((0.5, 0.91),),),
    ],
)
def test_all_us_driver_licenses(
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

def test_column_valid_us_driver_license_weak_WA_no_title(recognizer, entities):
    col = Column(Series([
        'AA1B2**9ABA7',
        'A*1234AB*CD9'
    ]))
    result_group = recognizer.analyze(col, entities)

    assert len(result_group.recognizer_results) == 2
    for result in result_group.recognizer_results:
        assert_result_within_score_range(
            result, entities[0], 0, 12, 0.3, 0.4)

def test_column_valid_us_driver_license_very_weak_with_relevant_title(recognizer, entities):
    col = Column(Series([
        '12345679012',
        '67891023467'
    ], name='license_num'))
    result_group = recognizer.analyze(col, entities)

    assert len(result_group.recognizer_results) == 2
    for result in result_group.recognizer_results:
        assert_result_within_score_range(
            result, entities[0], 0, 11, 0.7, 0.75)

def test_column_valid_us_driver_license_mixed_no_title(recognizer, entities):
    col = Column(Series([
        'AA1B2**9ABA7', # weak_WA
        'H12234567',    # weak alpha
        '12345679012'   # very weak digits
    ]))
    result_group = recognizer.analyze(col, entities)

    assert len(result_group.recognizer_results) == 3
    assert_result_within_score_range(
        result_group.recognizer_results[0], entities[0], 0, 12, 0.3, 0.4)
    assert_result_within_score_range(
        result_group.recognizer_results[1], entities[0], 0, 9, 0.29, 0.49)
    assert_result_within_score_range(
        result_group.recognizer_results[2], entities[0], 0, 11, 0, 0.02)

def test_column_mixed_valid_and_invalid_us_driver_license_no_title(recognizer, entities):
    col = Column(Series([
        '12345679012',  # very weak
        '67891023467'   # very weak
        'C12T345672'    # invalid
    ]))
    result_group = recognizer.analyze(col, entities)

    assert result_group is None
