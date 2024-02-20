# class parses csv files and create quote objects.

from typing import List

import pandas as pd

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """Class to parse csv files and create quote objects."""

    allowed_extensions = ["csv"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the csv file at the path and return QuoteModel objects."""
        if not cls.can_ingest(path):
            raise Exception("Cannot ingest exception")

        quotes_list = []
        df = pd.read_csv(path, header=0, sep=",")
        for _, row in df.iterrows():
            quote = QuoteModel(row["body"], row["author"])
            quotes_list.append(quote)

        return quotes_list
