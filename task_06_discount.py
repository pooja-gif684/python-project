"""Calculate a purchase discount and the final payable amount."""


def calculate_discount(amount):
    """Return the discount and payable amount for the given purchase amount."""
    if amount < 0:
        raise ValueError("Purchase amount cannot be negative.")

    if amount >= 5000:
        discount_rate = 0.20
    elif amount >= 3000:
        discount_rate = 0.10
    elif amount < 300:
        discount_rate = 0.05
    else:
        discount_rate = 0

    discount = amount * discount_rate
    return discount, amount - discount


def main():
    amount = float(input("Enter the purchase amount in rupees: "))
    discount, payable = calculate_discount(amount)
    print(f"Discount amount: ₹{discount:.2f}")
    print(f"Final payable amount: ₹{payable:.2f}")


if __name__ == "__main__":
    main()
