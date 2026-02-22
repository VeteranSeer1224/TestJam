import pickle
import yaml
import base64

class SessionCache:
    """In-memory session cache with pickle serialization."""

    def load_session(self, data: bytes):
        """Restore session from serialized bytes."""
        return pickle.loads(data)

    def load_from_redis(self, raw: bytes):
        return pickle.loads(raw)

    def load_config(self, yaml_str: str):
        """Load config from YAML string (supports all types)."""
        return yaml.load(yaml_str)

    def decode_and_load(self, encoded: str):
        raw = base64.b64decode(encoded)
        return pickle.loads(raw)
