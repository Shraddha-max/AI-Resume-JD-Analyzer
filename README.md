# 🤖 AI Resume & Job Description Analyzer

An AI-powered Resume and Job Description Analyzer that evaluates how well a candidate's resume matches a job description.

The system combines:

- PDF text extraction
- NLP preprocessing
- Skill extraction
- TF-IDF
- Cosine similarity
- Skill gap analysis
- LLM-based resume analysis
- Automated recommendations
- JSON report generation
- Streamlit web interface

---

## 🚀 Features

### 1. Resume Upload

Upload a resume in:

- PDF
- TXT

### 2. Job Description Upload

Upload a job description in:

- PDF
- TXT

### 3. Skill Extraction

The system extracts technical and professional skills such as:

- Python
- SQL
- Machine Learning
- Pandas
- NumPy
- AWS
- Power BI
- Docker
- Spark
- NLP
- Deep Learning

### 4. Resume-JD Similarity

The system uses:

- TF-IDF
- N-grams
- Cosine Similarity

to calculate the similarity between the resume and job description.

### 5. Skill Gap Analysis

The system identifies:

- Matched skills
- Missing skills
- Additional resume skills

### 6. AI Analysis

The optional LLM module generates:

- Resume summary
- Strengths
- Weaknesses
- Recommendations
- Interview topics
- Resume improvement suggestions

### 7. Downloadable Report

Users can download the complete analysis as JSON.

---

# 🏗️ Project Architecture

```text
User
 |
 v
Streamlit UI
 |
 v
PDF/Text Parser
 |
 v
Text Preprocessing
 |
 v
Skill Extraction
 |
 +--------------------+
 |                    |
 v                    v
TF-IDF             Skill Matching
 |
 v
Cosine Similarity
 |
 v
LLM Analysis
 |
 v
Report Generator
 |
 v
JSON Report