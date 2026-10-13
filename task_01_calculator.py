"""Calculate the basic arithmetic results for two numbers."""


def calculate_all(a, b):
    """Return addition, subtraction, multiplication, division, floor division, and remainder."""
    return {
        "addition": a + b,
        "subtraction": a - b,
        "multiplication": a * b,
        "division": a / b,
        "floor_division": a // b,
        "remainder": a % b,
    }


def main():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    for operation, result in calculate_all(a, b).items():
        print(f"{operation.replace('_', ' ').title()}: {result}")


if __name__ == "__main__":
    main()
