from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(
    resume_text,
    jd_text
):

    """
    Calculate TF-IDF cosine similarity.

    Returns
    -------
    float
        Similarity score from 0 to 100.
    """

    if not resume_text or not jd_text:

        return 0.0


    documents = [
        resume_text,
        jd_text
    ]


    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2),
        max_features=10000
    )


    try:

        tfidf_matrix = vectorizer.fit_transform(
            documents
        )

    except ValueError:

        return 0.0


    similarity_matrix = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )


    score = similarity_matrix[0][0] * 100


    return round(
        float(score),
        2
    )


def get_similarity_label(score):

    """
    Convert similarity score into a human-readable category.
    """

    if score >= 80:

        return "Excellent Match"

    elif score >= 65:

        return "Strong Match"

    elif score >= 50:

        return "Moderate Match"

    elif score >= 35:

        return "Weak Match"

    else:

        return "Low Match"


def calculate_skill_weighted_score(
    similarity_score,
    skill_match_percentage,
    similarity_weight=0.5,
    skill_weight=0.5
):

    """
    Combine text similarity and skill similarity.

    This gives a more useful overall score than
    pure TF-IDF similarity.
    """

    overall_score = (
        similarity_score * similarity_weight
        +
