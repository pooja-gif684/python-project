"""Determine a student's result from their marks."""


def get_result(marks):
    """Return distinction, pass, or fail based on marks."""
    if marks >= 75:
        return "distinction"
    if marks >= 35:
        return "pass"
    return "fail"


def main():
    marks = float(input("Enter the student's marks: "))
    print(get_result(marks))


if __name__ == "__main__":
    main()
