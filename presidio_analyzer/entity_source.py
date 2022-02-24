from abc import abstractmethod
from dataclasses import dataclass
from presidio_analyzer import RecognizerResultGroup, PresidioLogger
from typing import Sequence, Optional
import re

logger = PresidioLogger("presidio")

@dataclass
class EntitySource:
    """
    Base class encapsulating behavior of any data source to be analyzed.
    """
    titles: Optional[list] = None
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

        # Process original and tokenized titles
        titles = (
            [series.name, self._tokenize_title(series.name)]
            if isinstance(series.name, str)
            else None
        )
        super().__init__(
            titles=titles,
            text=col.astype(str),
            **kwargs
        )
        self.sample_size = sample_size

    @staticmethod
    def _tokenize_title(title_text):
        """
        Preprocessing step to effectively provode limited substring matching for
        recognizers. Converts camelCase, PascalCase titles into space-delimited
        tokens and normalizes common sparators into spaces.
        """
        if title_text is None or not(isinstance(title_text, str)):
            return title_text

        split_regex = r"""
        (?<=[a-zA-Z])\B(?=[0-9])    # Split trailing numbers
        | (?<=[0-9])\B(?=[a-zA-Z])  # Split leading numbers
        | (?<=[a-z])\B(?=[A-Z])     # Split on lower to upper case change
        | (?<=[A-Z]{2})\B(?=[a-z])  # Split on 2+ upper to lower case change
        | [_-]                      # Convert other separators to space
        """

        return ' '.join([
            r for r in re.split(split_regex, title_text, flags=re.VERBOSE)
            if r])

    def items(self):
        return self.text.items()

    def postprocess_results(self, results):
        """
        Validate that there is a match for every row, or that the match occurred
        in the title (and no rows matches)
        """
        if not results:
            return

        # Special case: title-only matches
        if all(getattr(r, 'source', None) == 'entity_title' for r in results):
            return results

        # Handle column match, requires a valid match for every row.
        expected_col_matches = len(self.text)
        valid_matches = [r.index for r in results]
        if expected_col_matches == len(set(valid_matches)): # Count unique col indicies
            return RecognizerResultGroup(results)
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
