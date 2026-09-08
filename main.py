def driving_license_eligibility(age: int) -> str:
    if age < 16:
        return "Not eligible for driving license"
    if age < 18:
        return "Eligible for learner's license"
    return "Eligible for driving license"


age = 19
print(driving_license_eligibility(age))
    