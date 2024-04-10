### Setup env file
- Use the below sample
```env
# .env
SF_CONSUMER_KEY=placeholder
SF_CONSUMER_SECRET=placeholder
SF_USERNAME=placeholder
SF_PASSWORD=placeholder
SF_AUTH_URL=https://yourdomain.sandbox.my.salesforce.com/services/oauth2/token
SF_VERSION_NUMBER=59.0
SF_TOKEN_LIFETIME=3600
SF_DOMAIN_NAME=yourdomain.sandbox.my.salesforce.com
OUTPUT_DIRECTORY=placeholder
CURRENT_SPRINT_DIRECTORY=placeholder
EVENT_LOG_BASE_DIR=placeholder
```

### Sample commands

- Create Directories
```bash
python3 ./scripts/python/cURL/create_directories.py FY2024 Q3  SPRINT_T                                                                                                                                                                                                                                            
```

- Download ELF Logs
Set the CURRENT_SPRINT_DIRECTORY value before 
```bash
python3 ./scripts/python/cURL/download_elf.py ./scripts/python/cURL/soql/event_logs.soql   
```