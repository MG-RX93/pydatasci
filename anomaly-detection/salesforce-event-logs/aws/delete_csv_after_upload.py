import os

def delete_local_file(local_path):
    """Delete a local file and handle potential errors."""
    try:
        os.remove(local_path)
        print(f"File '{local_path}' deleted successfully.")
    except OSError as e:
        print(f"Failed to delete file '{local_path}': {e}")

def delete_corresponding_csv(local_parquet_path):
    """Delete the original CSV file that corresponds to a given Parquet file."""
    csv_file_path = local_parquet_path.rsplit(".", 1)[0] + ".csv"
    delete_local_file(csv_file_path)
