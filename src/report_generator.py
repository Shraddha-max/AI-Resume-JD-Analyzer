import json
import re
from datetime import datetime


def create_report(
    resume_file_name,
    jd_file_name,
    similarity_score,
    similarity_label,
    resume_skills,
    jd_skills,
    skill_analysis,
    llm_result=None
):

    """
    Create a structured analysis report.
    """

    report = {

        "project": "AI Resume & Job Description Analyzer",

        "generated_at": datetime.now().isoformat(),

        "resume_file": resume_file_name,

        "job_description_file": jd_file_name,

        "similarity_score": similarity_score,

        "similarity_label": similarity_label,

        "resume_skills": resume_skills,

        "jd_skills": jd_skills,

        "skill_analysis": skill_analysis,

        "llm_result": llm_result

    }


    return report


def report_to_json(report):

    """
    Convert report dictionary into JSON text.
    """

    return json.dumps(
        report,
        indent=4,
        ensure_ascii=False
    )


def save_report(
    report,
    output_path
):

    """
    Save report as JSON.
    """

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            report,
            file,
            indent=4,
            ensure_ascii=False
        )


def create_download_filename(
    resume_filename
):

    """
    Create safe downloadable report filename.
    """

    base_name = resume_filename.rsplit(
        ".",
        1
    )[0]


    base_name = re.sub(
        r"[^a-zA-Z0-9_-]+",
        "_",
        base_name
    )


    return (
        f"{base_name}_analysis_report.json"
    )
