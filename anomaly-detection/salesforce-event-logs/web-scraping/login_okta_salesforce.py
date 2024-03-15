import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs

# Method to login and return session object
def login(username, password):
    # URL for the Salesforce login page
    login_url = 'https://salesforce-elf.herokuapp.com'

    # Create session
    session = requests.Session()

    # Navigate to Salesforce login page
    response = session.get(login_url)
    print(response)
    if response.status_code != 200:
        print(f"Failed to access Salesforce login page: {response.status_code}")
        return None

    # Extract redirect URL
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup.find('a', attrs={"class": "btn btn-primary"}).get('href'))
    redirect_url = login_url+soup.find('a', attrs={"class": "btn btn-primary"}).get('href')
    print(redirect_url)
    # redirect_url = soup.find('a', attrs={"class": "btn btn-primary"}).get('href')    
    # redirect_url = redirect_url.split("'")[1]

    # Navigate to the redirect URL
    response = session.get(redirect_url)
    if response.status_code != 200:
        print(f"Failed to access redirect URL: {response.status_code}")
        return None

    # Extract form data for login
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup)
    login_form = soup.find('form')
    print(login_form)
    login_action = login_form['action']
    login_data = {input_tag['name']: input_tag.get('value', '') for input_tag in login_form.find_all('input')}

    # Update login data with username and password
    login_data['username'] = username
    login_data['password'] = password

    # Perform login request
    response = session.post(login_action, data=login_data)
    if response.status_code == 200:
        print("Login successful")
        return session
    else:
        print(f"Login failed: {response.status_code}")
        return None

# Main function
def main():
    # Define credentials
    username = ''
    password = ''

    # Login to Salesforce
    session = login(username, password)
    if session:
        print(session)
        # Continue with other tasks (e.g., accessing protected resources)

if __name__ == "__main__":
    main()