# using the GitHub API and the JIRA API. This code will create a JIRA issue whenever a new GitHub issue is created.

Prereqs:
pip install requests
Set up environment variables:
GITHUB_TOKEN: Your GitHub personal access token.
JIRA_URL: The URL of your JIRA instance (e.g., https://your-domain.atlassian.net).
JIRA_EMAIL: Your JIRA account email.
JIRA_API_TOKEN: Your JIRA API token.

import os
import requests

# Set up environment variables
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
JIRA_URL = os.getenv('JIRA_URL')
JIRA_EMAIL = os.getenv('JIRA_EMAIL')
JIRA_API_TOKEN = os.getenv('JIRA_API_TOKEN')

# GitHub API URL for fetching issues
GITHUB_REPO = 'your-github-username/your-repo'
GITHUB_API_URL = f'https://api.github.com/repos/{GITHUB_REPO}/issues'

# JIRA API URL for creating issues
JIRA_API_URL = f'{JIRA_URL}/rest/api/2/issue/'

# Function to get GitHub issues
def get_github_issues():
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    response = requests.get(GITHUB_API_URL, headers=headers)
    return response.json()

# Function to create a JIRA issue
def create_jira_issue(title, description):
    issue_data = {
        "fields": {
            "project": {"key": "YOUR_PROJECT_KEY"},  # Replace with your JIRA project key
            "summary": title,
            "description": description,
            "issuetype": {"name": "Task"},  # Change to the appropriate issue type if needed
        }
    }
    response = requests.post(JIRA_API_URL, json=issue_data, auth=(JIRA_EMAIL, JIRA_API_TOKEN))
    return response.json()

# Main function to sync GitHub issues to JIRA
def sync_issues():
    github_issues = get_github_issues()
    for issue in github_issues:
        if not issue.get('pull_request'):  # Skip pull requests
            jira_response = create_jira_issue(issue['title'], issue['body'])
            print(f'Created JIRA issue: {jira_response.get("key")} for GitHub issue: {issue["title"]}')

if __name__ == "__main__":
    sync_issues()

Explanation of the Code
Imports:

The code uses the os module to access environment variables and the requests library for making HTTP requests.
Environment Variables:

The code retrieves necessary credentials and tokens from environment variables for security.
API URLs:

GITHUB_API_URL: Constructs the URL for accessing issues in the specified GitHub repository.
JIRA_API_URL: Constructs the URL for creating issues in JIRA.
Functions:

get_github_issues(): Fetches all issues from the specified GitHub repository using the GitHub API.
create_jira_issue(title, description): Creates a new JIRA issue using the JIRA API. It sends a POST request with the issue data, including the project key, title, description, and issue type.
sync_issues():

Retrieves GitHub issues and creates corresponding JIRA issues for each non-pull request issue. It prints the key of the created JIRA issue for reference.
Main Execution:

The sync_issues() function is called when the script runs.
How to Use
Replace the placeholders in the code (like your-github-username, your-repo, and YOUR_PROJECT_KEY) with actual values.
Set up your environment variables with your credentials.
Run the script, and it will sync GitHub issues to JIRA.
