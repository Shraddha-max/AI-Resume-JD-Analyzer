import io

from PyPDF2 import PdfReader


def extract_text_from_pdf(file):

    """
    Extract text from an uploaded PDF file.

    Parameters
    ----------
    file:
        Streamlit UploadedFile or file-like object.

    Returns
    -------
    str
        Extracted text.
    """

    try:

        if hasattr(file, "getvalue"):

            pdf_bytes = file.getvalue()

            reader = PdfReader(
                io.BytesIO(pdf_bytes)
            )

        else:

            reader = PdfReader(file)


        extracted_text = []

        for page in reader.pages:

            text = page.extract_text()

            if text:

                extracted_text.append(text)


        return "\n".join(extracted_text).strip()


    except Exception as error:

        raise RuntimeError(
            f"PDF extraction failed: {error}"
        )


def extract_text_from_pdf_path(file_path):

    """
    Extract text from a PDF stored on disk.
    """

    try:

        reader = PdfReader(file_path)

        pages = []

        for page in reader.pages:

            text = page.extract_text()

            if text:

                pages.append(text)


        return "\n".join(pages).strip()


    except Exception as error:

        raise RuntimeError(
            f"Could not read PDF file: {error}"
        )
