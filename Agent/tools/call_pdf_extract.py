import fitz  # PyMuPDF
import requests
import os
import re

def sanitize_name(name):
    """
    Sanitize the name to create a safe filename.
    """
    # Remove any characters that are not alphanumeric, spaces, or underscores
    safe_name = re.sub(r'[^a-zA-Z0-9_\s]', '_', name)
    # Replace spaces with underscores
    safe_name = safe_name.replace(' ', '_')
    return safe_name

def download_pdf(pdf_link, name):
    response = requests.get(pdf_link, stream=True)
    
    if response.status_code != 200:
        raise Exception(f"Failed to download PDF: {response.status_code}")
    
    if 'application/pdf' not in response.headers.get('Content-Type', ''):
        raise Exception(f"URL does not point to a PDF. Content-Type: {response.headers.get('Content-Type')}")

    safe_name = sanitize_name(name)
    pdf_file_path = f"{safe_name}.pdf"

    with open(pdf_file_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    return pdf_file_path


def extract_text_from_pdf(pdf_file_path):
    """
    Extract text from a PDF file using PyMuPDF.
    """
    doc = fitz.open(pdf_file_path)
    text = ""
    
    for page in doc:
        text += page.get_text()
    
    doc.close()
    
    return text

def extract_pdf_text(pdf_link,name):
    """
    Extract text from a PDF file given its link.
    """
    # Download the PDF file
    pdf_file_path = download_pdf(pdf_link,name)
    
    # Extract text from the PDF file
    text = extract_text_from_pdf(pdf_file_path)
    
    # Clean up the downloaded PDF file
    os.remove(pdf_file_path)
    
    return text    