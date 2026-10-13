"""Perform one arithmetic operation selected by an operator."""


def calculate(a, operator, b):
    """Calculate a supported operation, raising errors for invalid input."""
    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b
    if operator == "/":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
    if operator == "//":
        if b == 0:
            raise ZeroDivisionError("Cannot floor-divide by zero.")
        return a // b
    if operator == "%":
        if b == 0:
            raise ZeroDivisionError("Cannot find a remainder with a divisor of zero.")
        return a % b
    if operator == "**":
        return a**b
    raise ValueError(f"Invalid operator: {operator}")


def main():
    a = float(input("Enter the first number: "))
    operator = input("Enter an operator (+, -, *, /, //, %, **): ").strip()
    b = float(input("Enter the second number: "))
    print(calculate(a, operator, b))


if __name__ == "__main__":
    main()
