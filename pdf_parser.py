import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_file) -> str:
    """
    Extracts all text from the uploaded PDF file.
    pdf_file: file-like object from Gradio
    Returns: concatenated string
    """
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text.strip()
