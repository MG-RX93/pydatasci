import os
import subprocess
import sys
from aws_login import login_to_aws_via_sso
from convert_csv_to_parquet import convert_to_parquet
from delete_csv_after_upload import delete_corresponding_csv

def verify_directory_exists(directory):
    """Ensure that the specified directory exists.
    
    Args:
        directory (str): The path to the directory to verify.
    
    Raises:
        SystemExit: If the directory does not exist.
    """
    if not os.path.isdir(directory):
        print(f"Directory '{directory}' does not exist.")
        sys.exit(1)

def change_directory(directory):
    """Change the current working directory to the specified directory.
    
    Args:
        directory (str): The path to the directory to change to.
    
    Raises:
        SystemExit: If changing the directory fails.
    """
    try:
        os.chdir(directory)
    except Exception as e:
        print(f"Failed to change to directory '{directory}': {e}")
        sys.exit(1)

def upload_file_to_s3(local_path, s3_bucket_path, aws_profile):
    """Upload a file to an S3 bucket using the provided AWS profile.
    
    Args:
        local_path (str): The path to the local file to upload.
        s3_bucket_path (str): The S3 bucket path where the file will be uploaded.
        aws_profile (str): The AWS profile to use for authentication.
    
    Returns:
        bool: True if the upload was successful, False otherwise.
    """
    try:
        result = subprocess.run(
            ["aws", "s3", "cp", local_path, s3_bucket_path, "--profile", aws_profile],
            check=False
        )
        return result.returncode == 0
    except Exception as e:
        print(f"An error occurred during file upload: {e}")
        return False

def iterate_and_upload_files(directory, s3_bucket_path, aws_profile):
    """Iterate over Parquet files in the directory, upload them to S3, and delete the original CSV files.
    
    Args:
        directory (str): The directory to search for Parquet files.
        s3_bucket_path (str): The S3 bucket path where the files will be uploaded.
        aws_profile (str): The AWS profile to use for authentication.
    """
    parquet_files_found = False
    for file in os.listdir(directory):
        if file.endswith(".parquet"):
            parquet_files_found = True
            local_path = os.path.join(directory, file)
            try:
                upload_successful = upload_file_to_s3(local_path, s3_bucket_path, aws_profile)
                if upload_successful:
                    print(f"File '{local_path}' uploaded successfully to '{s3_bucket_path}'.")
                    delete_corresponding_csv(local_path)
                else:
                    print(f"File '{local_path}' failed to upload.")
            except Exception as e:
                print(f"An error occurred during upload of '{local_path}': {e}")

    if not parquet_files_found:
        print(f"No .parquet files found in '{directory}'.")


def main(directory, s3_bucket_path, aws_profile):
    """Main function to run the script's workflow.
    
    This function converts CSV files to Parquet format, uploads them to S3, and cleans up the CSV files.
    
    Args:
        directory (str): The directory where the CSV and Parquet files are located.
        s3_bucket_path (str): The S3 bucket path where the Parquet files will be uploaded.
        aws_profile (str): The AWS profile to use for authentication.
    """
    verify_directory_exists(directory)
    change_directory(directory)
    convert_to_parquet(directory)
    login_to_aws_via_sso(aws_profile)
    iterate_and_upload_files(directory, s3_bucket_path, aws_profile)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: script.py <directory> <s3_bucket_path> <aws_profile>")
        sys.exit(1)
    
    directory, s3_bucket_path, aws_profile = sys.argv[1:4]
    main(directory, s3_bucket_path, aws_profile)
