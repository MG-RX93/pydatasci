import os
import requests
from dotenv import load_dotenv
from datetime import datetime, timedelta

# Load environment variables from .env file
load_dotenv()

# Globals for caching
_cached_token = None
_token_expiry = datetime.now()
_instance_url = None


def get_access_token() -> tuple:
    """
    Retrieves the current Salesforce access token, either from cache or by requesting a new one.

    Returns:
        tuple: A tuple containing the access token and Salesforce instance URL.
    """
    global _instance_url
    access_token = get_cached_access_token()

    if access_token is None:
        access_token, instance_url, issued_at = request_new_access_token()
        cache_access_token(access_token, instance_url, issued_at)
        _instance_url = instance_url

    return access_token, _instance_url

def get_cached_access_token() -> str:
    """
    Retrieves the cached access token if it is still valid.

    Returns:
        str: The cached access token, or None if the token has expired or is not cached.
    """
    if _cached_token and not is_token_expired():
        return _cached_token
    return None

def is_token_expired() -> bool:
    """
    Checks if the cached access token has expired.

    Returns:
        bool: True if the token has expired; False otherwise.
    """
    global _token_expiry
    return datetime.now() >= _token_expiry
