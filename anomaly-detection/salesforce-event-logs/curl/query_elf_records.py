from simple_salesforce import Salesforce #pip install simple-salesforce
import datetime

# Salesforce login credentials
sf_username = 'your_salesforce_username'
sf_password = 'your_salesforce_password'
sf_security_token = 'your_salesforce_security_token'

# SOQL query parameters
start_date = datetime.date(2023, 1, 1)  # Example: January 1, 2023
end_date = datetime.date(2023, 1, 31)   # Example: January 31, 2023
event_type = 'Login'  # Example EventType
interval = 'Daily'  # Example interval

# Format dates for SOQL query
start_date_str = start_date.strftime('%Y-%m-%d')
end_date_str = end_date.strftime('%Y-%m-%d')

# Initialize Salesforce connection
sf = Salesforce(username=sf_username, password=sf_password, security_token=sf_security_token)

# SOQL query
query = f"""
SELECT Id, EventType, LogDate
FROM EventLogFile
WHERE EventType = '{event_type}'
AND LogDate >= {start_date_str}
AND LogDate <= {end_date_str}
AND Interval = '{interval}'
"""

# Execute the query
records = sf.query_all(query)
records = records['records']

# Print the records
for record in records:
    print(record)

