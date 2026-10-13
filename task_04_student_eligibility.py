"""Check student eligibility using marks, attendance, and backlog status."""


def check_eligibility(marks, attendance, has_backlog):
    """Return eligible only if all three stated conditions are satisfied."""
    if marks >= 60 and attendance >= 75 and not has_backlog:
        return "eligible"
    return "not eligible"


def main():
    marks = float(input("Enter marks: "))
    attendance = float(input("Enter attendance percentage: "))
    has_backlog = input("Does the student have a backlog? (yes/no): ").strip().lower() == "yes"
    print(check_eligibility(marks, attendance, has_backlog))


if __name__ == "__main__":
    main()
