import requests
import json

def get_pull_requests(owner, repo, token):
    url = f'https://api.github.com/repos/{owner}/{repo}/pulls'
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch pull requests. Status code: {response.status_code}")
        return []

def get_reviews(owner, repo, pr_number, token):
    url = f'https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/reviews'
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)
    return response.json()

def get_code_review_stats(owner, repo, token):
    pull_requests = get_pull_requests(owner, repo, token)
    review_stats = {}

    for pr in pull_requests:
        reviews = get_reviews(owner, repo, pr['number'], token)
        for review in reviews:
            reviewer = review['user']['login']
            if reviewer not in review_stats:
                review_stats[reviewer] = 1
            else:
                review_stats[reviewer] += 1

    return review_stats

if __name__ == '__main__':
    owner = 'org_name/username'
    repo = 'repo_name'
    token = 'personal_access_token'
    stats = get_pull_requests(owner, repo, token)
    prettified_stats = json.dumps(stats, indent=4)
    print(prettified_stats)
