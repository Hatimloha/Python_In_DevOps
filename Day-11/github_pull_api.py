import requests

response = requests.get("https://api.github.com/repos/Hatimloha/Python_In_DevOps/pulls")

complete_details = requests.json()

for i in range(len(complete_details)):
    print(complete_details[i])import requests

# Make a GET request to the GitHub API for pull requests
response = requests.get("https://api.github.com/repos/Hatimloha/Python_In_DevOps/pulls")

# Convert the response to JSON format
complete_details = response.json()

# Iterate through the list of pull requests
for i in range(len(complete_details)):
    print(complete_details[i])
