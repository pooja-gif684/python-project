"""Determine placement eligibility and experience category."""


def check_placement(age, marks, attendance, experience, has_backlogs):
    """Return placement eligibility and category based on the stated criteria."""
    if age < 0 or experience < 0:
        raise ValueError("Age and experience cannot be negative.")

    if experience < 1:
        category = "fresher"
    elif experience <= 2:
        category = "junior"
    else:
        category = "experienced"

    eligible = marks >= 60 and attendance >= 75 and not has_backlogs
    return {
        "placement_eligible": "yes" if eligible else "no",
        "candidate_category": category,
    }


def main():
    age = int(input("Enter age: "))
    marks = float(input("Enter marks: "))
    attendance = float(input("Enter attendance percentage: "))
    experience = float(input("Enter years of experience: "))
    has_backlogs = input("Does the candidate have backlogs? (yes/no): ").strip().lower() == "yes"
    result = check_placement(age, marks, attendance, experience, has_backlogs)
    print(f"placement eligible: {result['placement_eligible']}")
    print(f"candidate category: {result['candidate_category']}")


if __name__ == "__main__":
    main()
