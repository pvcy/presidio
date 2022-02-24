import pytest

from tests import assert_result
from presidio_analyzer.predefined_recognizers import EmailRecognizer
from pandas import Series
from presidio_analyzer import Column

@pytest.fixture(scope="module")
def recognizer():
    return EmailRecognizer()


@pytest.fixture(scope="module")
def entities():
    return ["EMAIL_ADDRESS"]


@pytest.mark.parametrize(
    "text, expected_len, expected_positions",
    [
        # valid email addresses
        ("info@presidio.site", 1, ((0, 18),),),
        ("my email address is info@presidio.site", 1, ((20, 38),),),
        (
            "try one of these emails: info@presidio.site or anotherinfo@presidio.site",
            2,
            ((25, 43), (47, 72),),
        ),
        # invalid email address
        ("my email is info@presidio.", 0, ()),
    ],
)
def test_all_email_addresses(
    text, expected_len, expected_positions, recognizer, entities, max_score
):
    results = recognizer.analyze(text, entities)
    assert len(results) == expected_len
    for res, (st_pos, fn_pos) in zip(results, expected_positions):
        assert_result(res, entities[0], st_pos, fn_pos, max_score)

# Column tests

def test_column_valid_email_no_title(recognizer, entities, max_score):
    col = Column(Series([
        'info@presidio.site',
        'admin@mydomain.ly'
    ]))
    result_group = recognizer.analyze(col, entities)

    assert len(result_group.recognizer_results) == 2
    assert_result(result_group.recognizer_results[0],
                  entities[0], 0, 18, max_score)
    assert_result(result_group.recognizer_results[1],
                  entities[0], 0, 17, max_score)

def test_column_valid_email_with_relevant_title(recognizer, entities, max_score):
    col = Column(Series([
        'info@presidio.site',
        'admin@mydomain.ly'
    ], name='e-mail'))
    result_group = recognizer.analyze(col, entities)

    assert len(result_group.recognizer_results) == 2
    assert_result(result_group.recognizer_results[0],
                  entities[0], 0, 18, max_score)
    assert_result(result_group.recognizer_results[1],
                  entities[0], 0, 17, max_score)

def test_column_mixed_valid_and_invalid_email_no_title(recognizer, entities, max_score):
    col = Column(Series([
        'info@presidio.site',
        'admin@mydomain.ly',
        'info@presidio.'
    ]))
    result_group = recognizer.analyze(col, entities)

    assert result_group is None
