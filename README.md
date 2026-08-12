# 🤖 AI Resume & Job Description Analyzer

An AI-powered web application that analyzes the compatibility between a candidate's resume and a job description using **NLP, skill extraction, TF-IDF, cosine similarity, and optional LLM-based analysis**.

The application identifies matching skills, missing skills, calculates a resume-JD similarity score, and provides recommendations to help candidates improve their resume for a target job.

---

## 🚀 Live Demo

### 👉 [Launch AI Resume & JD Analyzer](https://ai-resume-jd-analyzer-explaination.streamlit.app)

[![Live Demo](https://img.shields.io/badge/Live-Demo-red?logo=streamlit)](https://ai-resume-jd-analyzer-explaination.streamlit.app)

---

## 💻 Source Code

### 👉 [View Project on GitHub](https://github.com/Shraddha-max/AI-Resume-JD-Analyzer)

---

## 📌 Project Overview

Recruiters often receive a large number of resumes for a single job opening. Candidates also need to understand whether their resume matches the requirements of a particular job description.

This project automates that initial analysis.

The user uploads:

- 📄 Resume
- 💼 Job Description

The system then:

1. Extracts text from the uploaded documents.
2. Cleans and preprocesses the text.
3. Extracts relevant skills.
4. Calculates resume-JD similarity.
5. Identifies matched skills.
6. Identifies missing skills.
7. Provides optional AI-powered recommendations.
8. Generates a downloadable analysis report.

---

## ✨ Key Features

### 📄 Resume PDF Processing

Extracts text from PDF resumes using `PyPDF2`.

### 💼 Job Description Analysis

Supports job descriptions provided as PDF or TXT files.

### 🧹 NLP Text Preprocessing

Cleans the extracted text by:

- Converting text to lowercase
- Removing URLs
- Removing email addresses
- Removing phone numbers
- Removing unnecessary characters
- Normalizing whitespace

### 🛠️ Skill Extraction

Identifies technical and professional skills using a controlled skill dictionary.

Examples include:

- Python
- SQL
- Java
- Pandas
- NumPy
- Scikit-learn
- Machine Learning
- Deep Learning
- NLP
- AWS
- Azure
- Google Cloud
- Docker
- Kubernetes
- Spark
- Power BI
- Tableau
- Git
- GitHub
- Streamlit
- Flask
- FastAPI
- XGBoost
- Random Forest
- SHAP

The skill database can also be expanded with additional skills.

### 📊 Resume-JD Similarity

The application uses:

- TF-IDF Vectorization
- Unigrams and bigrams
- Cosine Similarity

to calculate how closely the resume matches the job description.

### 🎯 Skill Gap Analysis

The system identifies:

- ✅ Matched skills
- ❌ Missing skills
- ➕ Additional skills present in the resume

### 🤖 AI-Powered Analysis

When LLM analysis is enabled and an API key is configured, the system can provide:

- Resume summary
- Strengths
- Weaknesses
- Recommendations
- Interview preparation topics
- Resume improvement suggestions

### 📥 Downloadable Report

Users can download the complete analysis as a JSON report.

---

## 🏗️ System Architecture

```text
                    USER
                      │
                      ▼
             ┌─────────────────┐
             │  Streamlit UI   │
             └────────┬────────┘
                      │
             ┌────────▼────────┐
             │  PDF/TXT Parser │
             └────────┬────────┘
                      │
             ┌────────▼─────────┐
             │ Text Preprocessing│
             └────────┬─────────┘
                      │
             ┌────────▼─────────┐
             │ Skill Extraction │
             └────────┬─────────┘
                      │
              ┌───────┴────────┐
              │                │
              ▼                ▼
       ┌─────────────┐   ┌──────────────┐
       │ TF-IDF +    │   │ Skill Match  │
       │ Cosine      │   │ & Gap        │
       │ Similarity  │   │ Analysis     │
       └──────┬──────┘   └──────┬───────┘
              │                 │
              └────────┬────────┘
                       ▼
              ┌─────────────────┐
              │ Optional LLM    │
              │ Analysis        │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │ Report Generator│
              └────────┬────────┘
                       │
                       ▼
                JSON Analysis
                   Report
```

---

## 📂 Project Structure

```text
AI-Resume-JD-Analyzer/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── src/
    ├── __init__.py
    ├── pdf_parser.py
    ├── text_preprocessing.py
    ├── skill_extractor.py
    ├── similarity.py
    ├── llm_analyzer.py
    └── report_generator.py
```

---

## 🔄 Application Workflow

```text
Resume PDF/TXT
       │
       ▼
Text Extraction
       │
       ▼
Text Preprocessing
       │
       ▼
Skill Extraction
       │
       ├───────────────┐
       │               │
       ▼               ▼
Resume Skills      JD Skills
       │               │
       └───────┬───────┘
               ▼
        Skill Comparison
               │
               ▼
       TF-IDF Similarity
               │
               ▼
       Cosine Similarity
               │
               ▼
       Match Score + Gaps
               │
               ▼
       Optional AI Analysis
               │
               ▼
        Final JSON Report
```

---

## 🧰 Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Frontend | Streamlit |
| PDF Processing | PyPDF2 |
| Data Processing | Pandas, NumPy |
| NLP | TF-IDF, Text Preprocessing |
| Similarity | Cosine Similarity |
| Machine Learning | Scikit-learn |
| AI/LLM | OpenAI API |
| Visualization | Matplotlib |
| Version Control | GitHub |
| Deployment | Streamlit Community Cloud |

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Shraddha-max/AI-Resume-JD-Analyzer.git
```

### 2. Navigate to the project

```bash
cd AI-Resume-JD-Analyzer
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS/Linux

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Locally

Start the Streamlit application:

```bash
python -m streamlit run app.py
```

The application will open in your browser.

Usually the local application will be available at:

```text
http://localhost:8501
```

---

## 🤖 Enable AI Analysis

The core resume-JD analysis works without an LLM API.

To enable the optional AI analysis, configure your API key as an environment variable.

Create a `.env` file locally:

```text
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-5-mini
```

Never commit your API key or `.env` file to GitHub.

For Streamlit Cloud, configure the API key through the application's **Secrets** settings rather than placing it directly in the source code.

---

## 📊 Example Analysis

A typical analysis can produce results such as:

```text
Resume-JD Match: 78.4%

Matched Skills:
✓ Python
✓ SQL
✓ Pandas
✓ Machine Learning
✓ AWS

Missing Skills:
✗ Docker
✗ Apache Spark

Additional Resume Skills:
✓ Streamlit
✓ Scikit-learn
```

With AI analysis enabled, the application can additionally provide:

```text
Strengths:
• Strong Python and SQL foundation
• Relevant machine learning experience

Weaknesses:
• Limited evidence of Docker experience
• No clear Spark project

Recommendations:
• Add a Docker-based deployment project
• Build a Spark/PySpark data pipeline project
• Quantify achievements in project descriptions

Interview Topics:
• Python
• SQL
• Machine Learning
• AWS
• Data Processing
```

---

## 🧠 Core Methodology

### 1. Text Extraction

Resume and job-description documents are converted into machine-readable text.

### 2. Text Preprocessing

The extracted text is normalized to reduce irrelevant variations.

### 3. Skill Extraction

The system searches the documents for predefined technical and professional skills and maps detected aliases to canonical skill names.

For example:

```text
Python
Python Programming
```

can be mapped to:

```text
python
```

### 4. TF-IDF Vectorization

The resume and job description are converted into numerical vectors using Term Frequency-Inverse Document Frequency.

### 5. Cosine Similarity

The vectors are compared to calculate the textual similarity between the resume and job description.

### 6. Skill Matching

The extracted skills are compared using set operations:

```text
Matched Skills = Resume Skills ∩ JD Skills

Missing Skills = JD Skills - Resume Skills

Additional Skills = Resume Skills - JD Skills
```

### 7. AI Analysis

The optional LLM layer interprets the analysis and generates human-readable recommendations.

---

## 🎯 Use Cases

This project can be useful for:

- Job seekers
- Students
- Fresh graduates
- Career coaches
- Resume optimization
- Recruiters
- Placement preparation
- Job-specific resume analysis

---

## 🔐 Privacy & Security

The application is designed to process uploaded documents for analysis.

Users should avoid uploading sensitive documents containing information they do not want processed.

API keys are not stored in the source code and should be managed using environment variables or Streamlit Secrets.

---

## 🚀 Deployment

The application is deployed using **Streamlit Community Cloud**.

### Live Application

👉 [Open AI Resume & JD Analyzer](https://ai-resume-jd-analyzer-explaination.streamlit.app)

### Deployment Architecture

```text
GitHub Repository
       │
       ▼
Streamlit Community Cloud
       │
       ▼
requirements.txt
       │
       ▼
app.py
       │
       ▼
Live Web Application
```

---

## 🔮 Future Improvements

Future versions can include:

- 🔍 Semantic similarity using Sentence Transformers
- 📈 Advanced ATS scoring
- 🧠 Machine-learning-based skill extraction
- 📑 Resume section detection
- 💼 Experience matching
- 🎓 Education requirement matching
- 🎯 Job recommendation system
- 📊 Multiple JD comparison
- 🏆 Resume ranking
- 💬 Automated interview question generation
- 📄 PDF report generation
- 🗄️ Database integration
- 🔐 User authentication
- 🐳 Docker deployment
- ☁️ AWS deployment
- 📱 Improved responsive UI

---

## 📈 Future AI Architecture

```text
Resume
   │
   ├── Personal Information
   ├── Education
   ├── Experience
   ├── Skills
   └── Projects
          │
          ▼
   Resume Understanding
          │
          ▼
   Job Description Understanding
          │
          ▼
   Semantic Embeddings
          │
          ▼
   Skill + Experience Matching
          │
          ▼
   ATS Score
          │
          ▼
   Skill Gap Detection
          │
          ▼
   AI Recommendations
          │
          ▼
   Personalized Resume Improvement
```

---

## 👩‍💻 Author

### Shraddha Gobare

Computer Science Engineering Graduate

Interested in:

- Data Science
- Machine Learning
- Data Engineering
- Artificial Intelligence
- NLP
- Business Intelligence

### Connect

- 🔗 [LinkedIn](https://linkedin.com/in/shraddha-gobare)

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

## 📜 License

This project is intended for educational, portfolio, and demonstration purposes.
