# class parses pdf files and create quote objects.

import os
import random
import subprocess
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """Class to parse pdf files and create quote objects."""

    allowed_extensions = ["pdf"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the file at the given path and return QuoteModel objects."""
        quotes_list = []
        if not cls.can_ingest(path):
            raise Exception("Cannot ingest exception")

        tmp = f"./tmp/{random.randint(0, 1000)}.txt"
        try:
            _ = subprocess.call(["pdftotext", path, tmp])
            with open(tmp, "r") as file:
                file_lines_content = file.readlines()
        except FileNotFoundError as file_not_found_error:
            print(f"Error: {file_not_found_error}")
            return quotes_list

        for line in file_lines_content:
            line = line.strip("\n\r").strip()
            line_length = len(line)
            if line_length > 0:
                parsed_line = line.split(" - ")
                quote_model = QuoteModel(parsed_line[0], parsed_line[1])
                quotes_list.append(quote_model)

        file.close()
        os.remove(tmp)
        return quotes_list
