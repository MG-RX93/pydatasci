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


def is_token_expired() -> bool:
    """
    Determines if the cached access token has expired.

    Returns:
        bool: True if the token has expired, False otherwise.
    """
    global _token_expiry
    return datetime.now() >= _token_expiry


def authenticate_with_salesforce() -> tuple:
    """
    Authenticates with Salesforce to obtain a new access token and instance URL.

    Returns:
        tuple: A tuple containing the new access token and the Salesforce instance URL.

    Raises:
        Exception: If the authentication request to Salesforce fails or the response format is unexpected.
    """
    # Salesforce OAuth endpoints
    auth_url = os.getenv("SF_AUTH_URL")

    # Retrieve credentials and settings from environment variables
    client_id = os.getenv("SF_CONSUMER_KEY")
    client_secret = os.getenv("SF_CONSUMER_SECRET")
    username = os.getenv("SF_USERNAME")
    password = os.getenv("SF_PASSWORD")

    # Prepare data payload for authentication request
    data = {
        "grant_type": "password",
        "client_id": client_id,
        "client_secret": client_secret,
        "username": username,
        "password": password,
    }

    # Make the authentication request to Salesforce
    response = requests.post(auth_url, data=data)
    if response.status_code != 200:
        raise Exception(f"Authentication failed: {response.text}")

    auth_response = response.json()

    # Check for the presence of required keys in the response
    if (
        "access_token" not in auth_response
        or "instance_url" not in auth_response
        or "issued_at" not in auth_response
    ):
        raise Exception(
            "Unexpected response format received from Salesforce authentication endpoint"
        )

    return (
        auth_response["access_token"],
        auth_response["instance_url"],
        auth_response["issued_at"],
    )


def cache_access_token(token: str, instance_url: str, issued_at: str):
    """
    Caches the Salesforce access token and calculates the expiration time.

    Parameters:
        token (str): The access token received from Salesforce.
        instance_url (str): The instance URL received from Salesforce.
        issued_at (str): The timestamp when the token was issued.
    """
    global _cached_token, _token_expiry, _instance_url
    token_lifetime = int(
        os.getenv("SF_TOKEN_LIFETIME", "3600")
    )  # Default to 1 hour if not set

    _cached_token = token
    _instance_url = instance_url
    issued_at_datetime = datetime.fromtimestamp(int(issued_at) / 1000)
    _token_expiry = issued_at_datetime + timedelta(seconds=token_lifetime)


def get_access_token() -> tuple:
    """
    Retrieves or refreshes the Salesforce access token as needed. Uses the cached token if it is still valid,
    or authenticates with Salesforce to obtain a new token.

    Returns:
        tuple: A tuple containing the access token and the Salesforce instance URL.
    """
    global _cached_token, _instance_url

    if _cached_token and not is_token_expired():
        return _cached_token, _instance_url

    token, instance_url, issued_at = authenticate_with_salesforce()
    cache_access_token(token, instance_url, issued_at)

    return token, instance_url
