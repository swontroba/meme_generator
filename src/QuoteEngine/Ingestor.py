# class is a subclass of IngestorInterface for parsing file.

from typing import List

from .CSVIngestor import CSVIngestor
from .DOCXIngestor import DOCXIngestor
from .IngestorInterface import IngestorInterface
from .PDFIngestor import PDFIngestor
from .QuoteModel import QuoteModel
from .TXTIngestor import TXTIngestor


class Ingestor(IngestorInterface):
    """Subclass of IngestorInterface for parsing file."""

    ingestors = [DOCXIngestor, CSVIngestor, PDFIngestor, TXTIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Class method to parse file at given path and type."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)