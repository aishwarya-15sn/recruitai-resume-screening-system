# RecruitAI – Intelligent Resume Screening & Candidate Ranking System

RecruitAI is an NLP-based candidate screening platform that automates resume analysis, skill extraction, and candidate-job matching using TF-IDF vectorization and cosine similarity techniques. The system assists recruiters in identifying relevant candidates by comparing resume content against job requirements and generating relevance-based rankings.

## Features

* Automated resume parsing and preprocessing
* Skill extraction from candidate resumes
* Job description analysis and keyword identification
* Candidate-job matching using NLP similarity scoring
* Relevance-based candidate ranking
* Automated recruiter screening workflow

## System Architecture

```text
+------------------+
|   Resume Input   |
+------------------+
          ↓
+----------------------+
| Text Preprocessing   |
+----------------------+
          ↓
+----------------------+
|   Skill Extraction   |
+----------------------+
          ↓
+----------------------+
| TF-IDF Vectorization |
+----------------------+
          ↓
+----------------------+
| Cosine Similarity    |
|      Matching        |
+----------------------+
          ↓
+----------------------+
| Candidate Ranking    |
+----------------------+
          ↓
+----------------------+
| Recruiter Decision   |
|       Support        |
+----------------------+
```

## Methods Used

* Text preprocessing and normalization
* TF-IDF vectorization for document representation
* Cosine similarity scoring for candidate-job matching
* Skill extraction using keyword-based NLP techniques
* Automated relevance scoring and ranking pipeline

## Tech Stack

* Python
* Scikit-learn
* NumPy
* NLP (TF-IDF, Cosine Similarity)

## Project Structure

* resume_parser.py        → Resume parsing and preprocessing
* feature_extraction.py   → Skill extraction and keyword identification
* ranking_model.py        → TF-IDF vectorization and similarity scoring
* sample_resume.txt       → Sample candidate resume
* main.py                 → Candidate ranking pipeline
* requirements.txt        → Project dependencies

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

## Use Cases

* Resume screening automation
* Candidate shortlisting
* Skill-based hiring support
* Initial recruitment filtering
* HR decision support systems

## Future Enhancements

* PDF and DOCX resume parsing
* Semantic candidate matching using transformer embeddings
* Interactive recruiter dashboard
* Applicant Tracking System (ATS) integration
* LLM-powered candidate profile summarization

## Author

**Aishwarya S Ningappanavar**

B.E. Electronics and Communication Engineering  
Nitte Meenakshi Institute of Technology (NMIT), Bengaluru

* GitHub: https://github.com/aishwarya-15sn
* LinkedIn: https://www.linkedin.com/in/snaishwarya
