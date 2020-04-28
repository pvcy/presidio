from abc import abstractmethod
from dataclasses import dataclass
from presidio_analyzer import RecognizerResultGroup
from typing import Mapping

@dataclass
class EntitySource:
    """
    Base class encapsulating behavior of any data source to be analyzed.
    """
    title: str = None
    text: Mapping[int, str] = None
    text_has_context: bool = False

    @abstractmethod
    def items(self):
        """
        Iterable of (index, text_value) tuples.
        TODO Enforce function signature typing
        """

    @abstractmethod
    def postprocess_results(self, results):
        """
        Apply source-specific rules to analysis results.
        :param results: list of RecognizerResult
        :return list of RecognizerResult
        """
    @abstractmethod
    def replace(self, __old, __new):
        """
        Apply the equivalent of str.replace across the source text.
        """

class Column(EntitySource):

    def __init__(self, series, sample_size=None, **kwargs):
        super().__init__(
            title=series.name,
            text=series.sample(sample_size).astype(str),
            **kwargs
        )
        self.sample_size = sample_size

    def items(self):
        return self.text.items

    def postprocess_results(self, results):
        if len(results) == self.sample_size: # Req every sample to match
            return RecognizerResultGroup(results) # TODO Or just add col_index?

    def replace(self, __old, __new):
        return self.text.replace(__new, __old)


class Text(EntitySource):

    def __init__(self, text: str, **kwargs):
        super().__init__(
            text=[text],
            **kwargs
        )

    def items(self):
        return enumerate(self.text)

    def postprocess_results(self, results):
        return results

    def replace(self, __old, __new):
        return [t.replace(__old, __new) for t in self.text]
