- Sentiment Analysis for Mental Health Text Classification
- Project Overview

This project is a Machine Learning system that classifies mental health-related text into different emotional states such as stress, anxiety, or neutral feelings.

It uses Natural Language Processing (NLP) to process text and a trained classification model to predict the sentiment.

The system is also wrapped in a simple application (app.py) for real-time predictions.

📁 Repository Structure
├── sentiment-analysis-mental-health.ipynb   # Notebook (data analysis + training)
├── app.py                                   # Simple prediction app
├── model.pkl                                # Trained ML model
├── best_model.pkl                           # Best performing trained model
├── encoder.pkl                              # Label encoder for target classes
├── labels.pkl                               # Mapping of encoded labels
├── .gitignore
└── README.md
⚙️ How It Works
1. Data Preprocessing
Cleaning raw text (removing noise, symbols, etc.)
Converting text into numerical format
2. Feature Engineering
Transforming text using vectorization techniques (e.g., TF-IDF or similar)
3. Model Training
Training a classification model on mental health datasets
Saving the best model for deployment
4. Prediction
Input user text
Apply the same preprocessing steps
Predict mental health category using the trained model
🧠 Model Files Explained
model.pkl → Main trained ML model
best_model.pkl → Best optimized version of the model
encoder.pkl → Converts labels (e.g., stress → numeric label → class)
labels.pkl → Stores mapping of encoded classes for interpretation
🚀 How to Run the Project
1. Install dependencies
pip install -r requirements.txt
2. Run the application
python app.py
💬 Example Usage

Input:

I feel overwhelmed and anxious all the time

Output:

Predicted Class: Anxiety / Stress
🧪 Notebook Details

The file sentiment-analysis-mental-health.ipynb includes:

Data exploration
Data visualization
Text preprocessing pipeline
Model training
Evaluation metrics
🛠️ Technologies Used
Python 🐍
Scikit-learn
Pandas & NumPy
NLP (Natural Language Processing)
Pickle (Model Serialization)
Flask (if used in app.py)
