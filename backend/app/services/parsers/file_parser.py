import os

from app.services.parsers.pdf_parser import PDFParser
from app.services.parsers.txt_parser import TXTParser


class FileParser:

    def __init__(self):
        self.pdf_parser = PDFParser()
        self.txt_parser = TXTParser()

    def parse(self, file_path: str, filename: str) -> str:
        extension = self._get_extension(filename)

        if extension == ".pdf":
            return self.pdf_parser.parse(file_path)

        elif extension == ".txt":
            return self.txt_parser.parse(file_path)

        else:
            raise ValueError(f"Formato de arquivo não suportado: {extension}")

    def _get_extension(self, filename: str) -> str:
        return os.path.splitext(filename)[1].lower()