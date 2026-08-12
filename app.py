import streamlit as st
import json
from datetime import datetime

from src.pdf_parser import extract_text_from_pdf
from src.text_preprocessing import preprocess_text
from src.skill_extractor import extract_skills, compare_skills
from src.similarity import calculate_similarity, get_similarity_label
from src.llm_analyzer import analyze_with_llm
from src.report_generator import (
    create_report,
    report_to_json,
    create_download_filename
)



# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="AI Resume & JD Analyzer",
    page_icon="📄",
    layout="wide"
)


# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------

st.markdown(
    """
    <style>

    .main-title {
        font-size: 40px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        color: #666666;
        margin-bottom: 30px;
    }

    .score-box {
        padding: 25px;
        border-radius: 12px;
        text-align: center;
        background-color: #f5f7fa;
        margin-bottom: 20px;
    }

    .score-number {
        font-size: 42px;
        font-weight: bold;
    }

    .section-title {
        font-size: 25px;
        font-weight: 600;
        margin-top: 25px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

st.markdown(
    '<div class="main-title">🤖 AI Resume & Job Description Analyzer</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Analyze resume-job compatibility using NLP, skill extraction, '
    'semantic similarity and AI-powered recommendations.'
    '</div>',
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

with st.sidebar:

    st.header("⚙️ Settings")

    use_llm = st.checkbox(
        "Enable AI Analysis",
        value=False,
        help="Uses the configured LLM API for deeper resume analysis."
    )

    st.markdown("---")

    st.subheader("Analysis Pipeline")

    st.write("1. 📄 PDF/Text Extraction")
    st.write("2. 🧹 Text Preprocessing")
    st.write("3. 🛠️ Skill Extraction")
    st.write("4. 📊 Similarity Analysis")
    st.write("5. 🤖 AI Analysis")
    st.write("6. 📑 Report Generation")


# ---------------------------------------------------------
# FILE UPLOAD
# ---------------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    st.subheader("📄 Upload Resume")

    resume_file = st.file_uploader(
        "Upload your resume",
        type=["pdf", "txt"],
        key="resume"
    )


with col2:

    st.subheader("💼 Upload Job Description")

    jd_file = st.file_uploader(
        "Upload job description",
        type=["pdf", "txt"],
        key="jd"
    )


# ---------------------------------------------------------
# TEXT EXTRACTION FUNCTION
# ---------------------------------------------------------

def extract_uploaded_text(uploaded_file):

    if uploaded_file is None:
        return ""

    file_name = uploaded_file.name.lower()

    try:

        if file_name.endswith(".pdf"):

            return extract_text_from_pdf(uploaded_file)

        elif file_name.endswith(".txt"):

            return uploaded_file.read().decode(
                "utf-8",
                errors="ignore"
            )

        return ""

    except Exception as error:

        st.error(f"Could not read {uploaded_file.name}: {error}")

        return ""


# ---------------------------------------------------------
# ANALYZE BUTTON
# ---------------------------------------------------------

if st.button(
    "🚀 Analyze Resume",
    type="primary",
    use_container_width=True
):

    if resume_file is None:

        st.warning("Please upload a resume.")

        st.stop()

    if jd_file is None:

        st.warning("Please upload a job description.")

        st.stop()

    with st.spinner("Analyzing resume and job description..."):

        # -------------------------------------------------
        # STEP 1: EXTRACT TEXT
        # -------------------------------------------------

        resume_text = extract_uploaded_text(resume_file)

        jd_text = extract_uploaded_text(jd_file)

        if not resume_text.strip():

            st.error("No readable text was found in the resume.")

            st.stop()

        if not jd_text.strip():

            st.error(
                "No readable text was found in the job description."
            )

            st.stop()


        # -------------------------------------------------
        # STEP 2: PREPROCESS TEXT
        # -------------------------------------------------

        clean_resume_text = preprocess_text(resume_text)

        clean_jd_text = preprocess_text(jd_text)


        # -------------------------------------------------
        # STEP 3: EXTRACT SKILLS
        # -------------------------------------------------

        resume_skills = extract_skills(resume_text)

        jd_skills = extract_skills(jd_text)


        # -------------------------------------------------
        # STEP 4: COMPARE SKILLS
        # -------------------------------------------------

        skill_analysis = compare_skills(
            resume_skills,
            jd_skills
        )


        # -------------------------------------------------
        # STEP 5: SIMILARITY
        # -------------------------------------------------

        similarity_score = calculate_similarity(
            clean_resume_text,
            clean_jd_text
        )

        similarity_label = get_similarity_label(
            similarity_score
        )


        # -------------------------------------------------
        # STEP 6: LLM ANALYSIS
        # -------------------------------------------------

        llm_result = None

        if use_llm:

            llm_result = analyze_with_llm(
                resume_text=resume_text,
                jd_text=jd_text,
                resume_skills=resume_skills,
                jd_skills=jd_skills,
                similarity_score=similarity_score,
                skill_analysis=skill_analysis
            )


        # -------------------------------------------------
        # STEP 7: CREATE REPORT
        # -------------------------------------------------

        report = create_report(
            resume_file_name=resume_file.name,
            jd_file_name=jd_file.name,
            similarity_score=similarity_score,
            similarity_label=similarity_label,
            resume_skills=resume_skills,
            jd_skills=jd_skills,
            skill_analysis=skill_analysis,
            llm_result=llm_result
        )


        # -------------------------------------------------
        # SAVE TO SESSION
        # -------------------------------------------------

        st.session_state["report"] = report


# ---------------------------------------------------------
# DISPLAY RESULTS
# ---------------------------------------------------------

if "report" in st.session_state:

    report = st.session_state["report"]

    st.markdown("---")

    st.markdown(
        '<div class="section-title">📊 Analysis Results</div>',
        unsafe_allow_html=True
    )


    # -----------------------------------------------------
    # SCORE
    # -----------------------------------------------------

    score = report["similarity_score"]

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Resume-JD Match",
            f"{score:.1f}%"
        )

    with col2:

        st.metric(
            "Resume Skills",
            len(report["resume_skills"])
        )

    with col3:

        st.metric(
            "Required Skills",
            len(report["jd_skills"])
        )


    st.info(
        f"Match Level: **{report['similarity_label']}**"
    )


    # -----------------------------------------------------
    # SKILLS
    # -----------------------------------------------------

    st.markdown(
        '<div class="section-title">🛠️ Skill Analysis</div>',
        unsafe_allow_html=True
    )

    skill_analysis = report["skill_analysis"]


    col1, col2 = st.columns(2)

    with col1:

        st.subheader("✅ Matched Skills")

        if skill_analysis["matched_skills"]:

            for skill in skill_analysis["matched_skills"]:

                st.success(skill)

        else:

            st.write("No matching skills found.")


    with col2:

        st.subheader("❌ Missing Skills")

        if skill_analysis["missing_skills"]:

            for skill in skill_analysis["missing_skills"]:

                st.error(skill)

        else:

            st.success("No major missing skills detected.")


    # -----------------------------------------------------
    # RESUME SKILLS
    # -----------------------------------------------------

    with st.expander("📄 Resume Skills"):

        st.write(
            ", ".join(report["resume_skills"])
            if report["resume_skills"]
            else "No skills detected."
        )


    # -----------------------------------------------------
    # JD SKILLS
    # -----------------------------------------------------

    with st.expander("💼 Job Description Skills"):

        st.write(
            ", ".join(report["jd_skills"])
            if report["jd_skills"]
            else "No skills detected."
        )


    # -----------------------------------------------------
    # LLM RESULT
    # -----------------------------------------------------

    if report["llm_result"]:

        st.markdown(
            '<div class="section-title">🤖 AI Analysis</div>',
            unsafe_allow_html=True
        )

        llm_result = report["llm_result"]


        if isinstance(llm_result, dict):

            if "summary" in llm_result:

                st.subheader("Summary")

                st.write(llm_result["summary"])


            if "strengths" in llm_result:

                st.subheader("💪 Strengths")

                for item in llm_result["strengths"]:

                    st.success(item)


            if "weaknesses" in llm_result:

                st.subheader("⚠️ Weaknesses")

                for item in llm_result["weaknesses"]:

                    st.warning(item)


            if "recommendations" in llm_result:

                st.subheader("🚀 Recommendations")

                for item in llm_result["recommendations"]:

                    st.info(item)


            if "interview_topics" in llm_result:

                st.subheader("🎯 Interview Topics")

                for item in llm_result["interview_topics"]:

                    st.write(f"• {item}")

        else:

            st.write(llm_result)


    # -----------------------------------------------------
    # REPORT DOWNLOAD
    # -----------------------------------------------------

    st.markdown(
        '<div class="section-title">📥 Download Report</div>',
        unsafe_allow_html=True
    )

    json_report = report_to_json(report)

    download_name = create_download_filename(
        resume_file.name
    )

    st.download_button(
        label="📥 Download JSON Report",
        data=json_report,
        file_name=download_name,
        mime="application/json",
        use_container_width=True
    )


    # -----------------------------------------------------
    # RAW REPORT
    # -----------------------------------------------------

    with st.expander("🔍 View Complete JSON Report"):

        st.json(report)
