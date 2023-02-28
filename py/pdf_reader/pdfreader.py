import pdfreader
from pdfreader import PDFDocument


def main():
    fn = "doc.pdf"
    f = open(fn, "rb")
    
    doc = PDFDocument(f)
