### Sample commands

- Download ELF Logs
```bash
python3 ./cURL/download_elf.py ./cURL/soql/event_logs.soql   
```

### Sample env file
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
```