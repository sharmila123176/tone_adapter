##### TASK-1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               COMPANY NAME : COURSEVITA

NAME : PULAMARASETTI SHARMILA

DOMAIN : TECH

DURATION : 3MONTHS

TRAINER NAME : RAKESH

### Tone Adaptation in AI Responses : Dataset Collection, Rubrics, and Modeling
This project focuses on studying tone adaptation in AI-generated responses, aiming to make machine-generated text more contextually appropriate and emotionally intelligent. The goal is to train and evaluate models that can adapt tone (e.g., formal, casual, empathetic, assertive) based on the user input or intent.

### Overview
This project explores how artificial intelligence systems (especially language models) can adapt tone and style in responses, making them more appropriate for different audiences, contexts, and intents. It includes:
A framework for studying tone variation in NLP responses
Custom-designed rubrics for tone classification (formal, casual, empathetic, assertive, etc.)
Tools to collect and label tone-specific datasets
Baseline models for tone classification and generation

### Technologies Used
Technology :	Purpose
Python :	Core programming language
Jupyter : Notebook	Experimentation and prototyping
Hugging Face Transformers :	Pre-trained models and pipelines
PyTorch / TensorFlow	Model : fine-tuning and deployment
Streamlit :	Optional web UI for demos
Scikit-learn :	Evaluation and data preprocessing
pandas / NumPy :	Data manipulation and analysis


### Rubric Template Example
yaml
Copy
Edit
ToneRubric:
  categories:
    - Formal
    - Informal
    - Empathetic
    - Encouraging
    - Sarcastic
    - Neutral
  dimensions:
    - Clarity
    - Politeness
    - Emotion Level
    - Professionalism
  scale:
    type: Likert
    range: 1 to 5


### Project Structure
arduino
Copy
Edit
tone-adaptation-ai/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── custom/          # Manually labeled tone data
│
├── models/
│   └── tone_classifier.py
│
├── notebooks/
│   ├── dataset_exploration.ipynb
│   ├── tone_rubric_analysis.ipynb
│
├── utils/
│   └── text_cleaning.py
│   └── rubric_loader.py
│
├── app/
│   └── streamlit_app.py  # Interactive tone detection
│
├── README.md
└── requirements.txt


### Tasks Completed
Literature review on tone in NLP (papers on politeness, formality, empathetic NLG)
Rubric design (Likert-based, tone categories, guidelines)
Dataset curation & preprocessing
Baseline tone classification using DistilBERT
Streamlit interface for demo

### Future Work
Fine-tuning GPT models for tone-controlled text generation
Training multilingual tone classifiers
Expanding custom datasets
Human-in-the-loop evaluation via feedback forms





