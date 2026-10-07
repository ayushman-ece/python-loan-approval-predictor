# 💳 Loan Approval Predictor

A beginner-friendly Machine Learning project that predicts whether a loan application is likely to be **Approved** or **Rejected** using a **Random Forest Classifier**.

The model uses applicant information such as:

- Income
- Credit Score
- Loan Amount
- Employment Years
- Existing Loans

This project is part of my Python → Data Science → Machine Learning learning journey.

---

## 🚀 Project Overview

The **Loan Approval Predictor** uses Machine Learning to classify loan applications into two categories:

```text
APPROVED
REJECTED
```

The project demonstrates a basic Random Forest classification workflow:

```text
Loan Dataset
      ↓
Feature Selection
      ↓
Train/Test Split
      ↓
Random Forest Classifier
      ↓
Model Training
      ↓
Accuracy Evaluation
      ↓
New Applicant Input
      ↓
APPROVED / REJECTED Prediction
```

---

## 🎯 Objective

The main objective of this project is to understand how **Random Forest Classification** works.

The project demonstrates:

- Feature selection
- Target selection
- Train/test splitting
- Random Forest classification
- Multiple Decision Trees
- Model training
- Model prediction
- Accuracy evaluation
- Using a trained model for new data

---

## 🧠 Machine Learning Concepts

### 1. Features

The model uses five features:

```text
Income
CreditScore
LoanAmount
EmploymentYears
ExistingLoans
```

These features describe the applicant and their financial situation.

In Machine Learning:

```text
X → Input Features
```

---

### 2. Target

The target column is:

```text
Approved
```

The values are:

```text
0 → Rejected
1 → Approved
```

The model learns patterns between applicant information and the loan approval decision.

---

## 🌲 Random Forest Classifier

This project uses:

```python
RandomForestClassifier()
```

Random Forest is an ensemble Machine Learning algorithm that combines multiple Decision Trees.

Instead of relying on one Decision Tree:

```text
Decision Tree
      ↓
Prediction
```

Random Forest uses many trees:

```text
             Random Forest
                  │
       ┌──────────┼──────────┐
       ↓          ↓          ↓
    Tree 1     Tree 2     Tree 3
       ↓          ↓          ↓
   APPROVED   APPROVED   REJECTED
       │          │          │
       └──────────┼──────────┘
                  ↓
          Combined Decision
                  ↓
              APPROVED
```

The individual trees contribute to the final prediction.

---

## 🌳 Number of Trees

The model uses:

```python
n_estimators=100
```

This means the Random Forest contains **100 Decision Trees**.

More trees can provide a more stable prediction, although increasing the number of trees also increases computation.

---

## 🔀 Train/Test Split

The dataset is divided into:

```text
80% → Training Data
20% → Testing Data
```

The training data is used to train the Random Forest.

The testing data is used to evaluate the model on unseen examples.

The project uses:

```python
random_state=42
```

to make the random split reproducible.

---

## 📈 Model Evaluation

The project uses **Accuracy** to evaluate the classifier.

Accuracy represents the percentage of test predictions that were correct.

The current educational dataset produced:

```text
Accuracy: 100%
```

> **Important:** This does not mean the model is 100% accurate in real-world loan decisions. The dataset contains only 30 sample records, so the evaluation result is not statistically reliable.

---

## 📊 Dataset

The project uses a sample dataset containing 30 loan applications.

Example:

```csv
ApplicantID,Income,CreditScore,LoanAmount,EmploymentYears,ExistingLoans,Approved
L001,30000,580,500000,1,2,0
L002,55000,720,300000,5,1,1
L003,45000,680,400000,3,1,1
L004,25000,540,600000,1,3,0
L005,80000,760,350000,8,0,1
```

### Dataset Columns

| Column | Description |
|---|---|
| ApplicantID | Unique applicant identifier |
| Income | Applicant income |
| CreditScore | Applicant credit score |
| LoanAmount | Requested loan amount |
| EmploymentYears | Years of employment |
| ExistingLoans | Number of existing loans |
| Approved | Target: 0 = Rejected, 1 = Approved |

`ApplicantID` is not used as a model feature because it is only an identifier and does not provide meaningful predictive information.

---

## 🧪 Example Prediction

The program asks for new applicant information:

```text
===== ENTER APPLICANT DETAILS =====

Income: ₹70000
Credit Score: 740
Loan Amount: ₹400000
Employment Years: 7
Existing Loans: 0
```

The trained Random Forest then produces:

```text
===== LOAN APPROVAL PREDICTION =====

Income            : ₹70000.0
Credit Score      : 740
Loan Amount       : ₹400000.0
Employment Years  : 7
Existing Loans    : 0
Predicted Result  : APPROVED
```

---

## 🗂️ Project Structure

```text
python-loan-approval-predictor/
│
├── main.py
├── loan_predictor.py
├── loans.csv
├── requirements.txt
├── .gitignore
└── README.md
```

### `main.py`

Responsible for:

- Creating the predictor
- Training the model
- Taking applicant information
- Calling the prediction method

### `loan_predictor.py`

Contains the Machine Learning logic:

- Loading the dataset
- Preparing features and target
- Splitting the dataset
- Creating the Random Forest
- Training the model
- Evaluating accuracy
- Predicting loan approval

### `loans.csv`

Contains the loan application training dataset.

### `requirements.txt`

Contains the required Python libraries.

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/ayushman-ece/python-loan-approval-predictor.git
```

Move into the project directory:

```bash
cd python-loan-approval-predictor
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

Run:

```bash
python main.py
```

The model will train and display its accuracy.

The program will then ask for a new applicant's information.

Example:

```text
Income: ₹70000
Credit Score: 740
Loan Amount: ₹400000
Employment Years: 7
Existing Loans: 0
```

The program will return:

```text
Predicted Result : APPROVED
```

---

## 🧰 Technologies Used

- Python
- Pandas
- Scikit-learn
- Random Forest
- Decision Trees
- Machine Learning
- Classification
- CSV

---

## 📦 Requirements

The project requires:

```text
pandas
scikit-learn
```

Install them using:

```bash
pip install -r requirements.txt
```

---

## 📚 What I Learned

Through this project, I learned:

1. What ensemble learning means
2. How Random Forest works
3. How Random Forest uses multiple Decision Trees
4. What `n_estimators` means
5. How to select meaningful features
6. How to select a target variable
7. How to split data into training and testing sets
8. How to train a Random Forest classifier
9. How to evaluate a classification model
10. How to make predictions for new applicants
11. Why small datasets can produce unreliable evaluation results

---

## 🔄 Machine Learning Progress

This project follows my previous Machine Learning projects.

### Project #50 — Linear Regression

```text
Employee Information
        ↓
Linear Regression
        ↓
Salary
```

Used for predicting a numerical value.

### Project #51 — Logistic Regression

```text
Student Information
        ↓
Logistic Regression
        ↓
PASS / FAIL
```

Used for classification.

### Project #52 — Decision Tree

```text
Customer Information
        ↓
Decision Tree
        ↓
CHURN / STAY
```

Introduced tree-based classification.

### Project #53 — Random Forest

```text
Loan Applicant Information
        ↓
Multiple Decision Trees
        ↓
Random Forest
        ↓
APPROVED / REJECTED
```

Introduces ensemble learning.

---

## ⚠️ Limitations

This is an educational Machine Learning project.

Limitations include:

- Only 30 sample records are used.
- The dataset is synthetic/sample data.
- The 100% accuracy result is not reliable real-world performance.
- Real loan decisions depend on many additional financial factors.
- The model has not been validated on a large real-world dataset.
- The current application has basic input validation.

This model should **not be used for real financial or lending decisions**.

---

## 🔮 Future Improvements

Possible improvements include:

- Use a large real-world dataset
- Add debt-to-income ratio
- Add credit history length
- Add employment type
- Add number of dependents
- Add loan purpose
- Add more financial features
- Add confusion matrix
- Add precision, recall, and F1-score
- Compare Random Forest with Decision Tree
- Tune Random Forest hyperparameters
- Use cross-validation
- Handle class imbalance
- Add feature importance visualization
- Build a Streamlit web application
- Deploy the model as an API

---

## 👨‍💻 Author

**Ayushman Tiwari**

GitHub:

https://github.com/ayushman-ece

---

## 🛣️ Learning Journey

This project is part of my long-term journey:

```text
Python
   ↓
Data Analysis
   ↓
Data Science
   ↓
Machine Learning
   ↓
Deep Learning
   ↓
NLP
   ↓
LLMs
   ↓
RAG
   ↓
Agentic AI
```

The goal is to build practical projects while understanding the concepts behind them step-by-step.