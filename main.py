from loan_predictor import LoanPredictor


predictor = LoanPredictor("loans.csv")

predictor.train_model()

print("\n===== ENTER APPLICANT DETAILS =====")

income = float(input("Income: ₹"))
credit_score = int(input("Credit Score: "))
loan_amount = float(input("Loan Amount: ₹"))
employment_years = int(input("Employment Years: "))
existing_loans = int(input("Existing Loans: "))

predictor.predict_approval(
    income,
    credit_score,
    loan_amount,
    employment_years,
    existing_loans
)