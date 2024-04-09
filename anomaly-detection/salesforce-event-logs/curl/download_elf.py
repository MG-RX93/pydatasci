import sys
import subprocess
import os
from dotenv import load_dotenv
from query_salesforce import main as get_salesforce_data

# Load environment variables from .env file
load_dotenv()

# Load configurations from .env file
domain_name = os.getenv("SF_DOMAIN_NAME")
api_version = os.getenv("SF_VERSION_NUMBER")
output_directory = os.getenv("OUTPUT_DIRECTORY")

def download_event_log_files(query_file):
    record_ids, access_token = get_salesforce_data(query_file)

    for record_id in record_ids:
        # Construct the URL to download the EventLogFile
        download_url = f"https://{domain_name}/services/data/{api_version}/sobjects/EventLogFile/{record_id}/LogFile"
        
        # Ensure the output directory exists
        os.makedirs(os.path.expanduser(output_directory), exist_ok=True)
        
        # Specify the output file path, ensuring directories in the path are expanded properly
        output_file = os.path.expanduser(f"{output_directory}/outputLogFile_{record_id}.csv")
        
        # Construct the cURL command with authorization header and output file path
        curl_command = [
            "curl", download_url,
            "-H", f"Authorization: Bearer {access_token}",
            "-H", "X-PrettyPrint:1",
            "-o", output_file
        ]

        # Enhance the print statement for better readability
        curl_command_str = ' '.join(curl_command[:2]) + ' ' + \
            ' '.join([f'"{arg}"' if ' ' in arg else arg for arg in curl_command[2:]])
        print(curl_command_str)
        
        # Execute the cURL command
        try:
            subprocess.run(curl_command, check=True, stdout=subprocess.PIPE, universal_newlines=True)
            print(f"Downloaded {record_id} to {output_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error downloading {record_id}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <PATH_TO_QUERY_FILE>.soql")
        sys.exit(1)

    query_file = sys.argv[1]
    download_event_log_files(query_file)
