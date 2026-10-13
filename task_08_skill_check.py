"""Look up a skill in the acquired skills list."""

ACQUIRED_SKILLS = ["python", "MySQL", "git", "HTML"]


def check_skill(skill_name):
    """Return whether skill_name is in the acquired skills list."""
    return "skill available" if skill_name in ACQUIRED_SKILLS else "skill not available"


def main():
    skill_name = input("Enter a skill name: ")
    print(check_skill(skill_name))


if __name__ == "__main__":
    main()
