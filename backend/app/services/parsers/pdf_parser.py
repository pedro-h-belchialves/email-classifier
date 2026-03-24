from pypdf import PdfReader

class PDFParser:

    def parse(self, file_path: str) -> str:
        reader = PdfReader(file_path)

        text = ""

        for page in reader.pages:
            content = page.extract_text()
            if content:
                text += content + "\n"

        return text