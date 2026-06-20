# RecruitAI – Intelligent Resume Screening & Candidate Ranking System

RecruitAI is an NLP-powered candidate screening platform that automates resume parsing, skill extraction, and candidate-job matching using TF-IDF vectorization and cosine similarity techniques to process and rank multiple candidate resumes.

The project is designed to demonstrate how NLP techniques can assist recruiters in automating candidate shortlisting workflows.

## Key Features

* Automated resume parsing and preprocessing
* Skill extraction from candidate resumes
* Job description analysis and keyword identification
* Candidate-job matching using TF-IDF and cosine similarity
* * Automated ranking of multiple candidate resumes
* CSV export of candidate rankings
* Similarity score visualization

## Technical Approach

RecruitAI processes candidate resumes and job descriptions through an NLP pipeline involving preprocessing, skill extraction, TF-IDF vectorization, cosine similarity scoring, and candidate ranking. The system processes and ranks multiple resumes and generates recruiter-friendly reports and visualizations.

## Workflow

* Parse candidate resumes.
* Extract skills and keywords.
* Process the job description.
* Generate TF-IDF vectors.
* Compute cosine similarity scores.
* Rank candidates by relevance.
* Export reports and visualizations.

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* TF-IDF Vectorization
* Cosine Similarity
* Natural Language Processing (NLP)

## Project Structure

* resumes/ – Sample candidate resumes
* resume_parser.py – Resume parsing and preprocessing
* feature_extraction.py – Skill extraction and keyword identification
* ranking_model.py – Candidate ranking and similarity scoring
* ranking_results.csv – Candidate ranking report
* top_candidates.csv – Shortlisted candidates
* ranking_plot.png – Similarity score visualization
* main.py – Application entry point
* requirements.txt – Project dependencies 

## Getting Started

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

## Example Output

Candidates Processed: 20

Top Ranked Candidates:

1. Resume_01.txt – 0.xx
2. Resume_02.txt – 0.xx
3. Resume_03.txt – 0.xx

Generated Files:

* ranking_results.csv
* top_candidates.csv
* ranking_plot.png

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
