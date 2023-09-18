#!/usr/bin/env python
# coding: utf-8

# # Change Private Repositories into Public

# In[ ]:


# !pip install requests
# !pip install pygithub


# In[ ]:


import requests

# Replace these with your GitHub username and personal access token
username = "YOUR_USERNAME"
access_token = "YOUR_ACCESSTOKEN"

# Define the API endpoint for listing user repositories, including private ones
url = f"https://api.github.com/user/repos?type=private"

# Set up headers with the access token for authentication
headers = {
    "Authorization": f"token {access_token}",
    "Accept": "application/vnd.github.v3+json"  # Specify API version
}

# Send a GET request to the GitHub API to list private repositories
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    repositories = response.json()

    # Print the names of your private repositories
    print("Your private GitHub repositories:")
    for index, repo in enumerate(repositories):
        print(f"{index + 1}. {repo['name']}")

    # Change the visibility of odd-numbered repositories to public
    for index, repo in enumerate(repositories):
        repo_name = repo["name"]
        visibility_url = f"https://api.github.com/repos/{username}/{repo_name}"
        visibility_payload = {
            "private": False
        }
        visibility_response = requests.patch(visibility_url, headers=headers, json=visibility_payload)
        if visibility_response.status_code == 200:
            print(f"Changed visibility of '{repo_name}' to public.")
        else:
            print(f"Failed to change visibility of '{repo_name}' to public. Status code: {visibility_response.status_code}")
else:
    print(f"Failed to retrieve private repositories. Status code: {response.status_code}")

