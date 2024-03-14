import requests

def send_to_slack(webhook_url, message):
    payload = {'text': message}
    try:
        response = requests.post(webhook_url, json=payload)
        if response.status_code == 200:
            print("Message sent successfully to Slack")
        else:
            print(f"Failed to send message to Slack. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error occurred while sending message to Slack: {e}")

# Example usage
webhook_url = 'placeholder'
message = 'test'
send_to_slack(webhook_url, message)
