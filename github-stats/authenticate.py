import requests
from getpass import getpass

def authenticate(username, password, token, otp):
    session = requests.Session()
    session.auth = (username, f"{password}{token}")
    response = session.get('https://api.github.com/user')
    if response.status_code == 200:
        print("Authentication successful")
        return session
    elif response.status_code == 401 and 'X-GitHub-OTP' in response.headers:
        otp_code = input("Enter your two-factor authentication OTP: ")
        session.headers['X-GitHub-OTP'] = otp_code
        response = session.get('https://api.github.com/user')
        if response.status_code == 200:
            print("Authentication successful")
            return session
    print("Authentication failed")
    return None

def logout(session):
    session.close()
    print("Logged out successfully")

if __name__ == '__main__':
    username = input("Enter your GitHub username: ")
    password = getpass("Enter your GitHub password: ")
    token = getpass("Enter your personal access token: ")
    otp = input("Enter your two-factor authentication OTP: ")
    session = authenticate(username, password, token, otp)
    if session:
        # Use the authenticated session to make requests
        response = session.get('https://api.github.com/user')
        print(response.json())
        
        # Logout by closing the session
        logout(session)
