import os
import git

# Define the repository path and file to modify and to modify the name Andrew
repo_path = '/path/to/your/repository'
file_name = 'assign4story.txt'
old_name = 'Andrew'
new_name = 'Grace'

# Initialize the repository
repo = git.Repo(repo_path)

# Read the file
file_path = os.path.join(repo_path, file_name)
with open(file_path, 'r') as file:
    file_contents = file.read()