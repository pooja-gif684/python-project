"""Check an integer's parity and divisibility."""


def check_number(number):
    """Return whether number is even or odd and whether it is divisible by 3 and 5."""
    return {
        "parity": "even" if number % 2 == 0 else "odd",
        "divisible_by_3": number % 3 == 0,
        "divisible_by_5": number % 5 == 0,
    }


def main():
    number = int(input("Enter an integer: "))
    result = check_number(number)
    print(f"The number is {result['parity']}.")
    print(f"Divisible by 3: {result['divisible_by_3']}")
    print(f"Divisible by 5: {result['divisible_by_5']}")


if __name__ == "__main__":
    main()
