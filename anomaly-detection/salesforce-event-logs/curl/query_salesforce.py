import sys
import requests
import os
from dotenv import load_dotenv  # pip install python-dotenv
from salesforce_auth import get_access_token

# Load environment variables from .env file
load_dotenv()


def main(query_input):
    """
    Main function that processes the input to determine if it is a file path or a direct query string,
    then executes the query and returns the results.

    Parameters:
    - query_input: A string that can either be a file path to a .soql file containing a SOQL query or a direct SOQL query string.

    Returns:
    - A dictionary containing the query results.
    """
    soql_query = query_input
    if os.path.isfile(query_input):
        soql_query = get_soql_query_from_file(query_input)

    return execute_soql_query(soql_query)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <PATH_TO_QUERY_FILE>.soql")
        sys.exit(1)

    query_file = sys.argv[1]

    try:
        query_result = main(query_file)
        print(query_result)  # Print the query result to the console
    except FileNotFoundError:
        print(f"The file {query_file} does not exist.")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"Query failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
