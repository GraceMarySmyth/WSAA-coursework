# Removed unused imports
import requests
#import json
#import git
#import os
from github import Github
from config import config as cfg


'''
# install on command line
pip install PyGithub
'''
apikey = cfg["githubkey"]

g = Github(apikey)
repo = g.get_user().get_repo('GraceMarySmyth/WSAA-coursework')
#print (repo.clone_url)

fileInfo = repo.get_contents('Assignments/assign4story.txt')
urlOfFile = fileInfo.download_url
#print (urlOfFile)
#print (fileinfo.path)
#print (fileInfo.type)

response = requests.get(urlOfFile) 
contentOfFile = response.text 
print (contentOfFile)

newContents = contentOfFile .replace('Andrew', 'Grace')
newContents = newContents.replace('he', 'she') 
newContents = newContents.replace('his', 'her')
newContents = newContents.replace('him', 'her')


# Update the file in the repository
#repo.update_file(fileInfo.path, "Updated file with new name", newContents, fileInfo.sha, branch="main", committer=None, author=None)
# Attempt using requests to get the file from the repo
gitHubResponse=repo.update_file(fileInfo.path,"updated by prog", newContents,fileInfo.sha) 
repo.update_file(fileInfo.path, "Updated file with new name", newContents, fileInfo.sha, branch="main", committer=None, author=None)
print (gitHubResponse) 

'''
filename = 'assign4story.json'

url = 'https://api.github.com/repos/GraceMarySmyth/WSAA-coursework/contents/Assignments/'

response = requests.get(url)
print (response.status_code)
repoJSON = response.json()
'''


'''
# Attempt using AI 

# Define the local repository path and files to modify and to modify the name Andrew
repo_path = 'local_repo'
file_name = 'assign4story.txt'
old_name = 'Andrew'
new_name = 'Grace'
old_gender= 'he'
new_gender= 'she'
old_pronoun = 'his'
new_pronoun = 'her'
old2_pronoun = 'him'
new2_pronoun = 'her'

# Clone the repository if it doesn't exist locally
try:
    if not os.path.exists(repo_path):
        git.Repo.clone_from('https://github.com/GraceMarySmyth/WSAA-coursework.git', repo_path)
    # Initialize the repository
    repo = git.Repo(repo_path)
except git.exc.GitCommandError as e:
    print(f"Error during repository cloning or initialization: {e}")
    exit(1)

# Read the file
file_path = os.path.join(repo_path, 'Assignments', file_name)
try:
    with open(file_path, 'r') as file:
        file_contents = file.read()
except FileNotFoundError:
    print(f"Error: The file {file_path} does not exist.")
    exit(1)

# Replace the old name with the new name
new_file_contents = file_contents.replace(old_name, new_name)
new_file_contents = new_file_contents.replace(old_gender, new_gender)
new_file_contents = new_file_contents.replace(old_pronoun, new_pronoun) 
new_file_contents = new_file_contents.replace(old2_pronoun, new2_pronoun)   
# Write the new file contents back to the file
with open(file_path, 'w') as file:
    file.write(new_file_contents)

# Commit the changes
repo.index.add([file_path])
try:
    origin.push()
except git.exc.GitCommandError as e:
    print(f"Error during push: {e}")
    exit(1)

# Push the changes
origin = repo.remote(name='origin')
origin.push()
'''
