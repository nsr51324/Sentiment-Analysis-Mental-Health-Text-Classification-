# Sentiment Analysis for Mental Health Text Classification

## Project Overview
This project is a Machine Learning system designed to classify mental health-related text into emotional states such as stress, anxiety, or neutral feelings. It uses Natural Language Processing (NLP) for text preprocessing and a trained classification model to predict sentiment in real-time.

The system is wrapped in a simple Python application (`app.py`) for real-time predictions.

## 📁 Repository Structure
```
Plaintext
├── sentiment-analysis-mental-health.ipynb   # Jupyter Notebook (EDA + training)
├── app.py                                   # Simple real-time prediction app
├── model.pkl                                # Trained ML model
├── best_model.pkl                           # Best performing optimized model
├── encoder.pkl                              # Label encoder for target classes
├── labels.pkl                               # Mapping of encoded labels
├── .gitignore
└── README.md
```

## ⚙️ How It Works

### 1. Data Preprocessing
- Cleans raw text by removing noise, symbols, and unnecessary characters  
- Standardizes text for better model understanding  

### 2. Feature Engineering
- Converts text into numerical format using techniques like TF-IDF vectorization  

### 3. Model Training
- Trains a classification model on mental health text datasets  
- Evaluates performance using multiple metrics  
- Saves the best-performing model  

### 4. Prediction
- Accepts real-time user input  
- Applies the same preprocessing pipeline  
- Outputs predicted mental health category  

##  Model Files Explained

- **model.pkl** → Main trained machine learning model  
- **best_model.pkl** → Optimized version of the model  
- **encoder.pkl** → Encodes and decodes target labels  
- **labels.pkl** → Stores mapping of encoded classes  

## 🚀 How to Run the Project

### 1. Install Dependencies
```bash
pip install -r requirements.txt
