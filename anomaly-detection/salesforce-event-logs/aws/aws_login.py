import subprocess
import os

def is_aws_logged_in(aws_profile):
    """Check if the user is logged in to AWS."""
    with open(os.devnull, 'w') as devnull:
        result = subprocess.run(
            ["aws", "sts", "get-caller-identity", "--profile", aws_profile],
            stdout=devnull,
            stderr=devnull
        )
    return result.returncode == 0

def login_to_aws_via_sso(aws_profile):
    """Login to AWS using SSO if not already logged in."""
    if is_aws_logged_in(aws_profile):
        print("You are already logged into AWS.")
    else:
        print("Logging into AWS using SSO...")
        subprocess.run(["aws", "sso", "login", "--profile", aws_profile])
