import pytest

from pandas import Series
from presidio_analyzer import Column

from presidio_analyzer.predefined_recognizers import CreditCardRecognizer, \
    UsPhoneRecognizer, DomainRecognizer, UsItinRecognizer, \
    UsLicenseRecognizer, UsBankRecognizer, UsPassportRecognizer, \
    IpRecognizer, UsSsnRecognizer, SgFinRecognizer

ip_recognizer = IpRecognizer()
us_ssn_recognizer = UsSsnRecognizer()
phone_recognizer = UsPhoneRecognizer()
us_itin_recognizer = UsItinRecognizer()
us_license_recognizer = UsLicenseRecognizer()
us_bank_recognizer = UsBankRecognizer()
us_passport_recognizer = UsPassportRecognizer()
sg_fin_recognizer = SgFinRecognizer()
domain_recognizer = DomainRecognizer()
cc_recognizer = CreditCardRecognizer()

recognizer_test_data = [
    [ip_recognizer,         'IP_ADDRESS', 'ipv4', ['192.168.1.1', '192.168.0.1']],
    [us_ssn_recognizer,     'US_SSN', 'ssn', ['078-05-1121', '078051121']],
    [phone_recognizer,      'PHONE_NUMBER', 'phone#', ['425 8829090', '(512) 449 8898']],
    [us_itin_recognizer,    'US_ITIN', 'itin', ['911-701234', '911701234']],
    [us_license_recognizer, 'US_DRIVER_LICENSE', 'dl#', ['A*1234AB*CD9', 'H12234567']],
    [us_bank_recognizer,    'US_BANK_NUMBER', 'account', ['945456787654', '4164714570235']],
    [us_passport_recognizer, 'US_PASSPORT', 'passport', ['912803456', '432552424']],
    [sg_fin_recognizer,     'FIN', 'nric', ['G1122144L', 'a2509109d']],
    [domain_recognizer,     'DOMAIN_NAME', 'domain', ['microsoft.com', 'google.co.il']],
    [cc_recognizer,         'CREDIT_CARD', 'credit', ['4012888888881881', '5019717010103742']]
]


def test_column_with_relevant_title_improves_score():
    for recognizer, entities, title, values in recognizer_test_data:
        results_without_title = recognizer.analyze(Column(Series(values)), entities)
        results_with_title = recognizer.analyze(Column(Series(values, name=title)), entities)

        assert (len(results_without_title.recognizer_results)
                == len(results_with_title.recognizer_results))

        for i in range(len(results_without_title.recognizer_results)):
            assert (results_without_title.recognizer_results[i].score == 1 or
                    results_without_title.recognizer_results[i].score <
                        results_with_title.recognizer_results[i].score)


@pytest.mark.xfail(reason="Not yet implemented")
def test_column_with_irrelevant_title_removes_result():
    """
    TODO
      A positive recognizer result for a column should be rejected if it has a
      title that doesn't correspond to the matched entity. The motivation for
      this is to reduce false positives, but there are enough conceivable edge
      cases that it might result in false negatives. e.g. it would be difficult
      to account for machine-generated names like "TBLA_1234".

      Further experimentation and testing is needed to determine the an
      acceptable tradeoff between false positive/negative matching.

    """
    for recognizer, entities, title, values in recognizer_test_data:
        results_without_title = recognizer.analyze(Column(Series(values)), entities)
        results_with_title = recognizer.analyze(Column(Series(values, name='foo/bar')), entities)

        assert results_without_title is not None and results_with_title is None


def test_tokenize_title():
    """
    Column names are often bunched together words, similar to variable names.
    It is difficult to perform pattern matching word tokens within this type
    of naming convention, so titles should be tokenized and space-delimited
    to simplify pattern matching by downstream recognizers.
    """
    assert Column._tokenize_title('colname') == 'colname'
    assert Column._tokenize_title('colname with spaces') == 'colname with spaces'
    assert Column._tokenize_title('col_name') == 'col name'
    assert Column._tokenize_title('col-name') == 'col name'
    assert Column._tokenize_title('colName') == 'col Name'
    assert Column._tokenize_title('colNAME') == 'col NAME'
    assert Column._tokenize_title('COLname') == 'COL name'
    assert Column._tokenize_title('COLnameCOLname') == 'COL name COL name'
    assert Column._tokenize_title('ColName') == 'Col Name'
    assert Column._tokenize_title('ColNameColName') == 'Col Name Col Name'
    assert Column._tokenize_title('NameNameNameName') == 'Name Name Name Name'
    assert Column._tokenize_title('colname123') == 'colname 123'
    assert Column._tokenize_title('123colname') == '123 colname'
    assert Column._tokenize_title('123colName') == '123 col Name'
    assert Column._tokenize_title('123colName456') == '123 col Name 456'
    assert Column._tokenize_title('123col456name') == '123 col 456 name'
    assert Column._tokenize_title('123col456nameNAME') == '123 col 456 name NAME'

    # Not smart enough to detect upper initial follwed by capitalized name
    assert Column._tokenize_title('modelTFord') == 'model TF ord'
