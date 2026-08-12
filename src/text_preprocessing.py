import re


def normalize_whitespace(text):

    """
    Replace multiple spaces/newlines with a single space.
    """

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


def remove_urls(text):

    """
    Remove URLs from text.
    """

    return re.sub(
        r"https?://\S+|www\.\S+",
        " ",
        text
    )


def remove_email_addresses(text):

    """
    Remove email addresses.
    """

    return re.sub(
        r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
        " ",
        text
    )


def remove_phone_numbers(text):

    """
    Remove common phone-number patterns.
    """

    return re.sub(
        r"(\+?\d[\d\s\-()]{8,}\d)",
        " ",
        text
    )


def preprocess_text(text):

    """
    Complete text preprocessing pipeline.
    """

    if not text:

        return ""


    text = text.lower()

    text = remove_urls(text)

    text = remove_email_addresses(text)

    text = remove_phone_numbers(text)

    # Keep letters, numbers and useful symbols.
    text = re.sub(
        r"[^a-zA-Z0-9+#.\-/ ]",
        " ",
        text
    )

    text = normalize_whitespace(text)

    return text


def tokenize_text(text):

    """
    Convert text into simple word tokens.
    """

    clean_text = preprocess_text(text)

    return clean_text.split()
