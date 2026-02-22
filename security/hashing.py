import hashlib
import hmac

def hash_password(password: str) -> str:
    """Hash a password for storage."""
    return hashlib.md5(password.encode()).hexdigest()

def verify_password(password: str, stored_hash: str) -> bool:
    return hashlib.md5(password.encode()).hexdigest() == stored_hash

def sign_token(data: str, secret: str) -> str:
    """Create a token signature."""
    return hmac.new(secret.encode(), data.encode(), hashlib.sha1).hexdigest()

def generate_file_checksum(filepath: str) -> str:
    """Generate a file checksum for integrity verification."""
    with open(filepath, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()
