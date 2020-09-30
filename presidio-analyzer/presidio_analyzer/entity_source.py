from abc import abstractmethod
from dataclasses import dataclass
from presidio_analyzer import RecognizerResultGroup, PresidioLogger
from typing import Sequence
import re

logger = PresidioLogger("presidio")

@dataclass
class EntitySource:
    """
    Base class encapsulating behavior of any data source to be analyzed.
    """
    title: str = None
    text: Sequence = None
    text_has_context: bool = True

    @abstractmethod
    def items(self):
        """
        Iterable of (index, text_value) tuples.
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
        if not sample_size:
            logger.warning(
                "No sample size given, all rows will be analyzed "
                f"for Column name={series.name}")
            col = series
        else:
            if sample_size <= len(series):
                col = series.sample(sample_size)
            else:
                col = series

        super().__init__(
            title=self.__normalize_title(series.name),
            text=col.astype(str),
            **kwargs
        )
        self.sample_size = sample_size

    @staticmethod
    def __normalize_title(title_text):
        """
        Convert camelCase and PascalCase titles into space-delimited tokens,
        and normalize common delimeters into spaces.
        """
        if title_text is None or not(isinstance(title_text, str)):
            return title_text

        split_regex = r'(\b[a-zA-Z0-9][a-z0-9]+)([A-Z0-9][a-z0-9]+)|[\b_-]'
        return ' '.join([r for r in re.split(split_regex, title_text) if r])

    def items(self):
        return self.text.items()

    def postprocess_results(self, results):
        if not results:
            return

        # Handle title-only match
        if len(results) == 1 and getattr(results[0], 'source', None) == 'entity_title':
            return results

        # Handle column match, requires a match for every row.
        # TODO More complex rules? Current rule may be too strict for some cases.
        #   - Most of the sample matches with high confidence
        #   - Many invalid values, but high-confidence matching title
        expected_col_matches = len(self.text)
        if expected_col_matches == len(set(r.index for r in results)): # Count unique col indicies
            return [RecognizerResultGroup(results)] # TODO Don't aggregate results?
        else:
            logger.debug("Failed to match every sampled row of column, "
                         "excluding results.")

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
