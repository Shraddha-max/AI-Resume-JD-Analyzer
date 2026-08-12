import re


# ---------------------------------------------------------
# SKILL DATABASE
# ---------------------------------------------------------

SKILL_DATABASE = {

    "python": [
        "python"
    ],

    "sql": [
        "sql",
        "mysql",
        "postgresql",
        "postgres",
        "oracle sql",
        "sql server"
    ],

    "java": [
        "java"
    ],

    "c": [
        "c programming",
        "c language"
    ],

    "c++": [
        "c++"
    ],

    "javascript": [
        "javascript",
        "js"
    ],

    "typescript": [
        "typescript"
    ],

    "html": [
        "html",
        "html5"
    ],

    "css": [
        "css",
        "css3"
    ],

    "react": [
        "react",
        "reactjs"
    ],

    "node.js": [
        "node.js",
        "nodejs",
        "node js"
    ],

    "pandas": [
        "pandas"
    ],

    "numpy": [
        "numpy"
    ],

    "scikit-learn": [
        "scikit-learn",
        "sklearn"
    ],

    "tensorflow": [
        "tensorflow"
    ],

    "pytorch": [
        "pytorch"
    ],

    "keras": [
        "keras"
    ],

    "machine learning": [
        "machine learning",
        "machine-learning"
    ],

    "deep learning": [
        "deep learning"
    ],

    "natural language processing": [
        "natural language processing",
        "nlp"
    ],

    "computer vision": [
        "computer vision"
    ],

    "generative ai": [
        "generative ai",
        "genai",
        "generative artificial intelligence"
    ],

    "artificial intelligence": [
        "artificial intelligence",
        "artificial intelligence"
    ],

    "llm": [
        "llm",
        "large language model",
        "large language models"
    ],

    "data science": [
        "data science"
    ],

    "data analysis": [
        "data analysis",
        "data analytics"
    ],

    "data engineering": [
        "data engineering"
    ],

    "etl": [
        "etl",
        "extract transform load",
        "extract-transform-load"
    ],

    "elt": [
        "elt"
    ],

    "data visualization": [
        "data visualization",
        "data visualisation"
    ],

    "power bi": [
        "power bi",
        "powerbi"
    ],

    "tableau": [
        "tableau"
    ],

    "excel": [
        "excel",
        "microsoft excel"
    ],

    "aws": [
        "aws",
        "amazon web services"
    ],

    "azure": [
        "azure",
        "microsoft azure"
    ],

    "google cloud": [
        "google cloud",
        "gcp",
        "google cloud platform"
    ],

    "docker": [
        "docker"
    ],

    "kubernetes": [
        "kubernetes",
        "k8s"
    ],

    "git": [
        "git"
    ],

    "github": [
        "github"
    ],

    "linux": [
        "linux"
    ],

    "spark": [
        "spark",
        "apache spark",
        "pyspark"
    ],

    "hadoop": [
        "hadoop"
    ],

    "mongodb": [
        "mongodb",
        "mongo db"
    ],

    "postgresql": [
        "postgresql",
        "postgres"
    ],

    "flask": [
        "flask"
    ],

    "fastapi": [
        "fastapi"
    ],

    "streamlit": [
        "streamlit"
    ],

    "rest api": [
        "rest api",
        "restful api",
        "restful apis"
    ],

    "statistics": [
        "statistics",
        "statistical analysis"
    ],

    "feature engineering": [
        "feature engineering"
    ],

    "data preprocessing": [
        "data preprocessing",
        "data cleaning"
    ],

    "nlp": [
        "nlp",
        "natural language processing"
    ],

    "shap": [
        "shap",
        "explainable ai",
        "xai"
    ],

    "random forest": [
        "random forest",
        "randomforest"
    ],

    "xgboost": [
        "xgboost"
    ],

    "logistic regression": [
        "logistic regression"
    ],

    "linear regression": [
        "linear regression"
    ],

    "communication": [
        "communication skills",
        "communication"
    ],

    "problem solving": [
        "problem solving",
        "problem-solving"
    ],

    "teamwork": [
        "teamwork",
        "team work"
    ]

}


# ---------------------------------------------------------
# NORMALIZATION
# ---------------------------------------------------------

def normalize_skill_text(text):

    text = text.lower()

    text = text.replace(
        "–",
        "-"
    )

    text = text.replace(
        "—",
        "-"
    )

    return text


# ---------------------------------------------------------
# SKILL EXTRACTION
# ---------------------------------------------------------

def extract_skills(text):

    """
    Extract skills from text using a controlled skill dictionary.
    """

    if not text:

        return []


    normalized_text = normalize_skill_text(text)

    found_skills = set()


    for canonical_skill, aliases in SKILL_DATABASE.items():

        for alias in aliases:

            alias = alias.lower()

            # Create word-boundary pattern.
            pattern = r"(?<!\w)" + re.escape(alias) + r"(?!\w)"

            if re.search(
                pattern,
                normalized_text
            ):

                found_skills.add(
                    canonical_skill
                )

                break


    return sorted(
        found_skills
    )


# ---------------------------------------------------------
# COMPARE SKILLS
# ---------------------------------------------------------

def compare_skills(resume_skills, jd_skills):

    resume_set = {
        skill.lower()
        for skill in resume_skills
    }

    jd_set = {
        skill.lower()
        for skill in jd_skills
    }


    matched = sorted(
        resume_set.intersection(jd_set)
    )

    missing = sorted(
        jd_set.difference(resume_set)
    )

    additional = sorted(
        resume_set.difference(jd_set)
    )


    if jd_set:

        match_percentage = (
            len(matched) /
            len(jd_set)
        ) * 100

    else:

        match_percentage = 0


    return {

        "matched_skills": matched,

        "missing_skills": missing,

        "additional_skills": additional,

        "skill_match_percentage": round(
            match_percentage,
            2
        )

    }


# ---------------------------------------------------------
# ADD CUSTOM SKILLS
# ---------------------------------------------------------

def add_custom_skills(
    skill_dictionary
):

    """
    Allows future expansion of the skill database.
    """

    if not isinstance(
        skill_dictionary,
        dict
    ):

        raise ValueError(
            "Skill dictionary must be a dictionary."
        )


    SKILL_DATABASE.update(
        skill_dictionary
    )
