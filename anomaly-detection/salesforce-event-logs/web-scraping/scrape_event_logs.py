import requests
import datetime

# Method to login and return session object
def login(username, password):
    login_url = 'https://salesforce-elf.herokuapp.com/event_log_files'
    session = requests.Session()
    login_data = {'username': username, 'password': password}
    response = session.post(login_url, data=login_data)
    if response.status_code == 200:
        return session
    else:
        print(f"Login failed: {response.status_code}")
        return None

# Method to download file for a given URL
def download_file(session, url):
    file_response = session.get(url)
    if file_response.status_code == 200:
        file_name = url.split('/')[-1]
        with open(file_name, 'wb') as f:
            f.write(file_response.content)
        print(f"File '{file_name}' downloaded successfully.")
    else:
        print(f"Failed to download file from '{url}'.")

# Main function
def main():
    # Define credentials
    username = ''
    password = ''
    
    # Login
    session = login(username, password)
    # if session:
    #     # Define date range and event types
    #     start_date = datetime.date(2024, 3, 1)
    #     end_date = datetime.date(2024, 3, 14)
    #     event_types = ['ApexExecution', 'ApexUnexpectedException']
        
    #     # Loop through date range and event types
    #     for event_type in event_types:
    #         date_range_url = f"https://salesforce-elf.herokuapp.com/event_log_files/?daterange={start_date}+to+{end_date}&eventtype={event_type}&interval=daily"
    #         download_file(session, date_range_url)

if __name__ == "__main__":
    main()
