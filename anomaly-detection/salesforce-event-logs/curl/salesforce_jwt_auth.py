import jwt
import requests
from datetime import datetime, timedelta

def get_salesforce_access():
    # Salesforce OAuth JWT credentials
    consumer_key = 'YourConsumerKeyFromConnectedApp'
    private_key_file_path = 'path/to/your/server.key'
    username = 'your_salesforce_username'
    instance_url = 'https://login.salesforce.com'  # Use https://test.salesforce.com for sandbox

    # Load the private key
    with open(private_key_file_path, 'r') as f:
        private_key = f.read()

    # JWT payload
    payload = {
        'iss': consumer_key,
        'sub': username,
        'aud': instance_url,
        'exp': datetime.now() + timedelta(minutes=3)
    }

    # Encode the JWT
    encoded_jwt = jwt.encode(payload, private_key, algorithm='RS256')

    # Token request
    token_url = f"{instance_url}/services/oauth2/token"
    data = {
        'grant_type': 'urn:ietf:params:oauth:grant-type:jwt-bearer',
        'assertion': encoded_jwt
    }

    response = requests.post(token_url, data=data)
    response.raise_for_status()  # Raises stored HTTPError, if one occurred

    response_json = response.json()
    return response_json['access_token'], response_json['instance_url']

if __name__ == "__main__":
    # Test the function when this file is executed directly
    access_token, instance_url = get_salesforce_access()
    print('Access Token:', access_token)
    print('Instance URL:', instance_url)
