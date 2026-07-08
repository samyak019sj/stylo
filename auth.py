import bcrypt


def hash_password(password):
    """
    Hash a plain text password.
    """

    password = password.encode("utf-8")

    hashed = bcrypt.hashpw(
        password,
        bcrypt.gensalt()
    )

    return hashed


def verify_password(password, hashed_password):
    """
    Verify password.
    """

    password = password.encode("utf-8")

    if isinstance(hashed_password, str):
        hashed_password = hashed_password.encode("utf-8")

    return bcrypt.checkpw(
        password,
        hashed_password
    )
