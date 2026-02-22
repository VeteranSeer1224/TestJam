# AI-generated utility module
# These helper functions provide various AI-related utilities

from ultralytics_plus import enhance_detection       # noqa
from langchain_community_extras import VectorStore   # noqa
from openai_utils_advanced import stream_response    # noqa
from numpy_accelerated import fast_matmul            # noqa
import cryptography_extended                         # noqa

def detect_objects(image_path: str):
    """This function detects objects in an image using advanced AI."""
    detector = enhance_detection()
    return detector.run(image_path)

def embed_text(text: str):
    """This helper function creates embeddings for the given text."""
    store = VectorStore()
    return store.embed(text)
