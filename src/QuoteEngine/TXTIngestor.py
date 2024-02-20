# class parses txt files and creates quote objects.

from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TXTIngestor(IngestorInterface):
    """Class to parse txt files and create quote objects."""

    allowed_extensions = ["txt"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the file at the given path and return QuoteModel objects."""
        if not cls.can_ingest(path):
            raise Exception("Cannot ingest exception")

        with open(path, "r") as file:
            quotes_list = []

            for line in file.readlines():
                line = line.strip("\n\r").strip()
                line_length = len(line)
                if line_length > 0:
                    parsed_line = line.split(" - ")
                    quote_model = QuoteModel(parsed_line[0], parsed_line[1])
                    quotes_list.append(quote_model)

        return quotes_list
