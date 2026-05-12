# RecruitAI – NLP-Based Recruitment Screening System

An NLP-based system that automatically analyzes resumes and ranks candidates
based on job descriptions using text similarity techniques.

## Features
- Resume text parsing and preprocessing
- Skill and keyword extraction from candidate resumes
- Candidate ranking based on similarity with job descriptions
- Automated screening support for recruiters

## Methods Used
- TF-IDF vectorization to represent resume and job description text
- Cosine similarity scoring to measure candidate-job relevance
- Basic NLP preprocessing using lowercase text normalization and skill extraction

## Tech Stack
Python, Scikit-learn, NLP (TF-IDF, Cosine Similarity)

## Project Structure
- resume_parser.py        # Extracts and preprocesses resume text
- feature_extraction.py   # Extracts candidate skills from resume text
- ranking_model.py        # Computes TF-IDF vectors and similarity scores
- sample_resume.txt       # Sample candidate resume
- main.py                 # Runs the candidate ranking pipeline

## How to Run

Install dependencies:
pip install -r requirements.txt

Run the application:
python main.py

## Future Improvements
- Integration with real recruitment datasets
- Semantic matching using transformer-based embeddings
- Web interface for recruiter interaction
