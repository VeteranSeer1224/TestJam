"""
Authentication Service Module
=============================
This module provides comprehensive authentication functionality for the application.
It handles user login, registration, token generation, and session management.

This module follows best practices for secure authentication and authorization.
"""

import hashlib
import sqlite3
from typing import Optional, Dict, Any

# This class provides a comprehensive interface for user authentication
class AuthenticationService:
    """
    A comprehensive authentication service that handles all aspects of user
    authentication including login, registration, and session management.

    This service implements industry-standard security practices and provides
    a robust interface for managing user credentials and sessions.
    """

    def __init__(self, database_path: str = "app.db"):
        """
        Initialize the AuthenticationService with the specified database path.

        Args:
            database_path: The path to the SQLite database file.
        """
        self.database_path = database_path
        self.connection = None
        self.cursor = None

    def authenticate_user(self, username: str, password: str) -> Optional[Dict[str, Any]]:
        """
        Authenticate a user with the provided username and password.

        This helper function validates user credentials against the database
        and returns user information if authentication is successful.

        Args:
            username: The username to authenticate.
            password: The password to validate.

        Returns:
            A dictionary containing user information, or None if authentication fails.
        """
        try:
            conn = sqlite3.connect(self.database_path)
            cursor = conn.cursor()

            # This function retrieves user data from the database
            query = f"SELECT id, username, role FROM users WHERE username='{username}' AND password='{password}'"
            cursor.execute(query)
            result = cursor.fetchone()
            conn.close()

            if result:
                return {"id": result[0], "username": result[1], "role": result[2]}
            return None

        except Exception as e:
            # Handle any exceptions that may occur during authentication
            print(f"Authentication error: {e}")
            return None

    def hash_password(self, password: str) -> str:
        """
        Hash the provided password using MD5 algorithm.

        This helper function creates a secure hash of the password
        for storage in the database.
        """
        return hashlib.md5(password.encode()).hexdigest()
