## Anomaly Detection using Event Log Files

### Requirements
- Salesforce Event Types
  - Apex Execution
  - Apex Trigger
  - Flow Execution

- Data Storage
  - AWS S3

- Database
  - Snowflake

- Visualization
  - Tableau

- Machine Learning models.
  - Isolation Forest
  - DBScan

### Downloading Salesforce Event Logs
- Query the EventLogFile object to get a list of Ids based on the following filters.
  - StartDate
  - EndDate
  - Interval(Daily)
  - EventType(See Requirements - Salesforce Event Types)

- Run cURL commands
  - Loop through the list of Ids and dynamically create the cURL commands to execute for downloading the Event Log Files.
  - Ensure the Files are downloaded into their respective Sprint folders.
  - Set the start and end dates based on the Sprint.

### Uploading to AWS S3
  - Create folders in the following order
    - FY Quarter => Sprint Name => Event Type
  - Run commands that upload the Event Log Files stored locally to the S3 buckets based on the FY Quarter => Sprint Name => Event Type combination.
    - Already created bash scripts to run the uploads.
      - This is run as a single script that sownloads, converts to parquet format, uploads to AWS and deletes the files (csv) locally.
    - Create the same as a py script. (*)
  - **Probably this is the most important step in this whole process - the conversion of file format from CSV to parquet.**
    - Using a Py script that is called from the bash script we execute to upload documents.
    - This converts files to parquet before uploading.


### Creating Snowflake Tables
  - Each Event type needs its own Sprint Table.
    - So ApexExecution Event Type for Sprint Apple would be: SPRINT_APPLE_APEX_EXECUTION
  - Created bash scripts that uses Snowflake CLI to create the tables.
  - Create the same as a py script. (*)

### Loading into Snowflake Tables
  - As all of the data is in AWS S3 and because the stage is already setup in Snowflake, the only thing left to do is loading data from the right set of files in S3 stage to the right table.
  - Created a bash script that uses Snowflake CLI to load data into table from S3 stage.

### Creating Dashboards in Tableau
  - The next step would be connecting the Snowflake Tables to Tableau.
    - See Tableau docs for detailed steps around connecting.
  - Once connected, we can create any charts we wish and add them to a dash that tracks the changes in perfromance Sprint over Sprint or data/stats specific to a Sprint.
    - Sprint over Sprint performance dashboard is created using the max, mean values of each of the Event Types every Sprint and this data 


### Running Anomaly Detection
  - 