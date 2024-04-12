import pandas as pd
import os
# pip install pandas
# pip install fastparquet


def convert_file(csv_file_path):
    # Assuming the CSV does not contain an index column at the first position
    df = pd.read_csv(csv_file_path)

    # Construct the Parquet file path
    parquet_file_path = csv_file_path.rsplit(".", 1)[0] + ".parquet"

    # Convert and save as Parquet
    df.to_parquet(parquet_file_path, engine="fastparquet", index=False)

    print(f"Converted {csv_file_path} to {parquet_file_path}")

def convert_to_parquet(directory):
    """Check for CSV files and convert them to Parquet format."""
    csv_files_found = False
    for file in os.listdir(directory):
        if file.endswith(".csv"):
            csv_files_found = True
            csv_file_path = os.path.join(directory, file)
            convert_file(csv_file_path)

    if csv_files_found:
        print("CSV files converted to Parquet format.")
    else:
        print("No CSV files found for conversion.")
