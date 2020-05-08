from unittest import TestCase

from assertions import assert_result
from presidio_analyzer.predefined_recognizers import SgFinRecognizer
from pandas import Series
from presidio_analyzer import Column

sg_fin_recognizer = SgFinRecognizer()
entities = ["FIN","NRIC"]


class TestSgFinRecognizer(TestCase):

    def test_valid_fin_with_allchars(self):
        num = 'G1122144L'
        results = sg_fin_recognizer.analyze(num, entities)
        assert len(results) == 2

    def test_invalid_fin(self):
        num = 'PA12348L'
        results = sg_fin_recognizer.analyze(num, entities)
        assert len(results) == 0


    # Column tests

    def test_column_valid_fin_mixed_no_title(self):
        col = Column(Series([
            'G1122144L',    # medium
            'a2509109d'     # weak
        ]))
        result_group = sg_fin_recognizer.analyze(col, entities)
        assert len([r for r in result_group.recognizer_results if r.index == 0]) == 2
        assert len([r for r in result_group.recognizer_results if r.index == 1]) == 1

    def test_column_valid_fin_mixed_with_relevant_title(self):
        col = Column(Series([
            'G1122144L',
            'a2509109d'
        ], name='fin#'))
        result_group = sg_fin_recognizer.analyze(col, entities)
        assert all([r.score == 1 for r in result_group.recognizer_results])

