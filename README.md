# RecruitAI – Intelligent Resume Screening & Candidate Ranking System

RecruitAI is an intelligent candidate screening platform that automates resume analysis, skill extraction, and candidate-job matching using Natural Language Processing (NLP) techniques. The system assists recruiters in identifying relevant candidates by comparing resume content against job requirements and generating relevance-based rankings.

---

## Overview

Modern recruitment processes often involve reviewing large numbers of resumes manually, making candidate shortlisting time-consuming and inefficient.

RecruitAI addresses this challenge by automating resume analysis and candidate-job matching using NLP-based text processing techniques. The system extracts candidate skills, analyzes job descriptions, computes similarity scores, and ranks candidates based on their relevance to specific job requirements.

---

## Features

* Automated resume parsing and preprocessing
* Skill extraction from candidate resumes
* Job description analysis and keyword identification
* Candidate-job matching using NLP similarity scoring
* Relevance-based candidate ranking
* Automated recruiter screening workflow
* Candidate evaluation support for hiring decisions

---

## System Architecture

```text
Resume Input
      ↓
Text Preprocessing
      ↓
Skill Extraction
      ↓
TF-IDF Vectorization
      ↓
Cosine Similarity Matching
      ↓
Candidate Ranking
      ↓
Recruiter Decision Support
```

---

## Methods Used

### Text Preprocessing

* Text normalization
* Lowercase conversion
* Noise reduction
* Keyword extraction

### Feature Representation

* TF-IDF (Term Frequency–Inverse Document Frequency) vectorization
* Numerical representation of resumes and job descriptions

### Similarity Analysis

* Cosine Similarity
* Candidate-job relevance scoring
* Ranking generation

### Skill Extraction

* Identification of technical skills and keywords
* Resume content analysis
* Automated candidate profiling

---

## Tech Stack

* Python
* Scikit-learn
* NumPy
* NLP Techniques
* TF-IDF Vectorization
* Cosine Similarity

---

## Project Structure

```text
resume_parser.py
│
├── Extracts and preprocesses resume text

feature_extraction.py
│
├── Extracts candidate skills and keywords

ranking_model.py
│
├── Computes TF-IDF vectors and similarity scores

sample_resume.txt
│
├── Sample candidate resume

main.py
│
├── Executes the candidate ranking pipeline

requirements.txt
│
└── Project dependencies
```

---

## How It Works

1. Candidate resume is provided as input.
2. Resume content is cleaned and preprocessed.
3. Skills and relevant keywords are extracted.
4. Job description is processed and vectorized.
5. TF-IDF vectors are generated.
6. Cosine similarity scores are calculated.
7. Candidates are ranked based on relevance scores.
8. Recruiters receive ranked candidate recommendations.

---

## Use Cases

* Resume screening automation
* Candidate shortlisting
* Skill-based hiring support
* Initial recruitment filtering
* HR decision support systems
* Recruitment workflow optimization

---

## Future Enhancements

* Resume parsing from PDF and DOCX files
* Semantic candidate matching using transformer embeddings
* Interactive recruiter dashboard
* Integration with Applicant Tracking Systems (ATS)
* LLM-powered candidate profile summarization
* Hybrid retrieval using embeddings and keyword matching
* Multi-candidate comparative analysis

---

## Learning Outcomes

Through this project, I gained practical experience in:

* Natural Language Processing (NLP)
* Information Retrieval
* TF-IDF Vectorization
* Cosine Similarity
* Text Processing Pipelines
* Candidate Ranking Systems
* Applied Machine Learning Workflows

---

## Author

**Aishwarya S Ningappanavar**

B.E. Electronics and Communication Engineering

Nitte Meenakshi Institute of Technology (NMIT), Bengaluru

GitHub: https://github.com/aishwarya-15sn
