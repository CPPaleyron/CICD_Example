
import hashlib
class User:
    """
    A simple User class to store and manage user information.

    Attributes:
        name (str): The user's name.
        age (int): The user's age.
        _password_hash (str): The hashed password (internal use only).
    """

    def __init__(self, name: str, age: int, password: str):
        """
        Initializes a User instance.

        Args:
            name (str): The name of the user.
            age (int): The age of the user.
            password (str): The user's password in plain text.
        """
        self.name = name
        self.age = age
        self._password_hash = self._hash_password(password)

    def _hash_password(self, password: str) -> str:
        """Hashes the password using SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()

    def salt_password(self, salt: str) -> str:
        """
        Returns a salted hash of the password.

        Args:
            salt (str): A salt string to enhance password security.

        Returns:
            str: The salted and hashed password.
        """
        salted = salt + self._password_hash
        return hashlib.sha256(salted.encode()).hexdigest()

    def verify_password(self, password: str) -> bool:
        """
        Verifies if the given password matches the stored hash.

        Args:
            password (str): The password to verify.

        Returns:
            bool: True if the password is correct, False otherwise.
        """
        return self._hash_password(password) == self._password_hash
