"""Determine whether a person should be granted access."""


def check_access(age, has_id, is_employee):
    """Allow adults with ID or any employee."""
    if (age >= 18 and has_id) or is_employee:
        return "access granted"
    return "access denied"


def main():
    age = int(input("Enter age: "))
    has_id = input("Do you have an ID? (yes/no): ").strip().lower() == "yes"
    is_employee = input("Are you an employee? (yes/no): ").strip().lower() == "yes"
    print(check_access(age, has_id, is_employee))


if __name__ == "__main__":
    main()
