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
    [us_ssn_recognizer,     'US_SSN', 'ssn', ['078-051120', '078051120']],
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


def test_column_with_irrelevant_title_removes_result():
    for recognizer, entities, title, values in recognizer_test_data:
        results_without_title = recognizer.analyze(Column(Series(values)), entities)
        results_with_title = recognizer.analyze(Column(Series(values, name='foo/bar')), entities)

        assert results_without_title is not None and results_with_title is None
