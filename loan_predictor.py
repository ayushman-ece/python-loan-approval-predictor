import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
class LoanPredictor:

    def __init__(self, file_name):
        self.data = pd.read_csv(file_name)
        
    def prepare_data(self):
            X = self.data[
                [
                    "Income",
                    "CreditScore",
                    "LoanAmount",
                    "EmploymentYears",
                    "ExistingLoans"
                ]
            ]

            y = self.data["Approved"]

            return X, y
    
    def train_model(self):
        X, y = self.prepare_data()

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )

        self.model = RandomForestClassifier(
            n_estimators=100,
            random_state=42
        )

        self.model.fit(X_train, y_train)

        predictions = self.model.predict(X_test)

        accuracy = accuracy_score(y_test, predictions)

        print("\n===== MODEL TRAINED =====")
        print("Random Forest model trained successfully. ✅")

        print("\n===== MODEL EVALUATION =====")
        print(f"Accuracy: {accuracy * 100:.2f}%")
    
    def predict_approval(
        self,
        income,
        credit_score,
        loan_amount,
        employment_years,
        existing_loans
    ):
        new_applicant = pd.DataFrame({
            "Income": [income],
            "CreditScore": [credit_score],
            "LoanAmount": [loan_amount],
            "EmploymentYears": [employment_years],
            "ExistingLoans": [existing_loans]
        })

        prediction = self.model.predict(new_applicant)

        result = "APPROVED" if prediction[0] == 1 else "REJECTED"

        print("\n===== LOAN APPROVAL PREDICTION =====")
        print(f"Income            : ₹{income}")
        print(f"Credit Score      : {credit_score}")
        print(f"Loan Amount       : ₹{loan_amount}")
        print(f"Employment Years  : {employment_years}")
        print(f"Existing Loans    : {existing_loans}")
        print(f"Predicted Result  : {result}")