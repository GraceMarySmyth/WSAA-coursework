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

# Replace the old name with the new name
new_file_contents = file_contents.replace(old_name, new_name)

# Write the new file contents back to the file
with open(file_path, 'w') as file:
    file.write(new_file_contents)

# Commit the changes
repo.index.add([file_name])
repo.index.commit('Replaced instances of Andrew with Grace')

# Push the changes
origin = repo.remote(name='origin')
origin.push()
