def validate_email(email):
    index = 0

    if not email[index].isalpha():
        raise ValueError("Username should start with a letter")

    while email[index] != "@" and index < len(email):
        letter = email[index]
        if not letter.isalnum() and letter not in ("_", "-"):
            raise ValueError(
                "Username should contain only letters, "
                "digits, dashes or underscores"
            )
        index += 1

    index += 1  # @

    while email[index] != "." and index < len(email):
        letter = email[index]
        if not letter.isalnum():
            raise ValueError(
                "Website should contain only letters and digits"
            )
        index += 1

    index += 1  # .

    if len(email[index:]) > 3:
        raise ValueError("Extension maximum length is 3")

    return None
