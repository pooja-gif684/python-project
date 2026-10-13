"""Validate the exercise's username and password."""


def is_valid_user(username, password):
    """Return whether the supplied credentials match the required values."""
    return username == "Admin" and password == "python123"


def main():
    username = input("Enter username: ")
    password = input("Enter password: ")
    print("valid" if is_valid_user(username, password) else "invalid")


if __name__ == "__main__":
    main()
