def check_financial_aid_status(student):

    # 1. Age check
    if not (18 <= student["age"] <= 24):
        return "Not Eligible"

    # 2. Residency check
    residency_met = (
        student["years_in_ca"] >= 2 or
        student["worked_months_in_ca"] >= 6 or
        student["parents_years_in_ca"] >= 1 or
        student["volunteer_proof"] is True
    )

    if residency_met:
        return "Eligible"

    # 3. Dean's consideration
    if student["household_income"] < 5000:
        return "Deferred for Dean's Consideration"

    return "Not Eligible"


# Test Case 1: (Expected: Eligible)
student1 = {
    "age": 20,
    "years_in_ca": 3,
    "worked_months_in_ca": 0,
    "parents_years_in_ca": 0,
    "volunteer_proof": False,
    "household_income": 20000
}

# Test Case 2: (Expected: Deferred for Dean's Consideration)
student2 = {
    "age": 22,
    "years_in_ca": 0,
    "worked_months_in_ca": 0,
    "parents_years_in_ca": 0,
    "volunteer_proof": False,
    "household_income": 3000
}

# Test Case 3 (Expected: Eligible)
student3 = {
    "age": 23,
    "years_in_ca": 0,
    "worked_months_in_ca": 0,
    "parents_years_in_ca": 0,
    "volunteer_proof": True,
    "household_income": 15000
}


print("Student 1:", check_financial_aid_status(student1))
print("Student 2:", check_financial_aid_status(student2))
print("Student 3:", check_financial_aid_status(student3))