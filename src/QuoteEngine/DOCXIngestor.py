# class parses docx files and create quote objects.

from typing import List

import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DOCXIngestor(IngestorInterface):
    """Class to parse docx files and create quote objects."""

    allowed_extensions = ["docx"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the file at the given path and return QuoteModel objects."""
        if not cls.can_ingest(path):
            raise Exception("Cannot ingest exception")

        docx_file = docx.Document(path)
        quotes_list = []
        for para in docx_file.paragraphs:
            if para.text != "":
                parsed_text = para.text.split(" - ")
                quote_model = QuoteModel(parsed_text[0], parsed_text[1])
                quotes_list.append(quote_model)

        return quotes_list
