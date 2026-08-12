import os
import json


def get_openai_client():

    """
    Create OpenAI client only when an API key exists.
    """

    api_key = os.getenv(
        "OPENAI_API_KEY"
    )

    if not api_key:

        return None


    try:

        from openai import OpenAI

        return OpenAI(
            api_key=api_key
        )

    except ImportError:

        return None


def create_analysis_prompt(
    resume_text,
    jd_text,
    resume_skills,
    jd_skills,
    similarity_score,
    skill_analysis
):

    prompt = f"""
You are an expert technical recruiter and resume analyst.

Analyze the following resume against the job description.

RESUME:
{resume_text[:12000]}

JOB DESCRIPTION:
{jd_text[:12000]}

RESUME SKILLS:
{", ".join(resume_skills)}

JOB DESCRIPTION SKILLS:
{", ".join(jd_skills)}

TEXT SIMILARITY SCORE:
{similarity_score}%

MATCHED SKILLS:
{", ".join(skill_analysis["matched_skills"])}

MISSING SKILLS:
{", ".join(skill_analysis["missing_skills"])}

Return ONLY valid JSON using this structure:

{{
    "summary": "short overall assessment",
    "strengths": [
        "strength 1",
        "strength 2",
        "strength 3"
    ],
    "weaknesses": [
        "weakness 1",
        "weakness 2"
    ],
    "recommendations": [
        "recommendation 1",
        "recommendation 2",
        "recommendation 3"
    ],
    "interview_topics": [
        "topic 1",
        "topic 2",
        "topic 3"
    ],
    "resume_improvements": [
        "improvement 1",
        "improvement 2"
    ]
}}

Do not invent experience that is not present in the resume.
Focus on the job requirements.
"""

    return prompt


def analyze_with_llm(
    resume_text,
    jd_text,
    resume_skills,
    jd_skills,
    similarity_score,
    skill_analysis
):

    """
    Analyze resume and JD using an LLM.

    Returns a dictionary if the API is configured.
    """

    client = get_openai_client()


    if client is None:

        return {
            "summary": (
                "AI analysis is unavailable because "
                "OPENAI_API_KEY is not configured."
            ),

            "strengths": [],

            "weaknesses": [],

            "recommendations": [
                "Configure OPENAI_API_KEY to enable AI analysis."
            ],

            "interview_topics": [],

            "resume_improvements": []
        }


    prompt = create_analysis_prompt(
        resume_text,
        jd_text,
        resume_skills,
        jd_skills,
        similarity_score,
        skill_analysis
    )


    try:

        response = client.responses.create(
            model=os.getenv(
                "OPENAI_MODEL",
                "gpt-5-mini"
            ),
            input=prompt
        )


        output_text = response.output_text.strip()


        try:

            return json.loads(
                output_text
            )

        except json.JSONDecodeError:

            return {
                "summary": output_text,

                "strengths": [],

                "weaknesses": [],

                "recommendations": [],

                "interview_topics": [],

                "resume_improvements": []
            }


    except Exception as error:

        return {
            "summary": (
                "The AI analysis could not be completed."
            ),

            "strengths": [],

            "weaknesses": [],

            "recommendations": [
                str(error)
            ],

            "interview_topics": [],

            "resume_improvements": []
        }
