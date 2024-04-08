import subprocess

# Variables
my_domain_name = 'MyDomainName.my.salesforce.com'
version = 'v60.0'
event_log_file_ids = ['0AT30000000000uGAA', '0AT30000000000uGAB']  # Example IDs
output_directory = '~/downloads/'  # Adjust this path as necessary
bearer_token = 'your_bearer_token_here'  # Replace with your actual token

# Function to build and execute the curl command
def download_event_log_file(domain, version, file_id, output_path, token):
    url = f'https://{domain}/services/data/{version}/sobjects/EventLogFile/{file_id}/LogFile'
    output_file = f'{output_path}outputLogFile_{file_id}.csv'  # Dynamic output filename
    curl_command = [
        'curl', url,
        '-H', f'Authorization: Bearer {token}',
        '-H', 'X-PrettyPrint:1',
        '-o', output_file
    ]
    
    # Execute the curl command
    try:
        subprocess.run(curl_command, check=True)
        print(f'Download completed for file ID {file_id}.')
    except subprocess.CalledProcessError as e:
        print(f'Error downloading file ID {file_id}: {e}')

# Loop through the list of Event Log File IDs and download each one
for file_id in event_log_file_ids:
    download_event_log_file(my_domain_name, version, file_id, output_directory, bearer_token)
