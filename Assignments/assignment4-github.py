import os
import git
import requests
import json

filename = 'assign4story.txt'

url = 'https://github.com/GraceMarySmyth/WSAA-coursework/tree/main/Assignments?'
response = requests.get(url)
print (response.status_code) # 200 shows code so far is working
repojson = response.json()
# Print the JSON response to inspect its structure
print(json.dumps(repojson, indent=4))

# Access the correct key if it exists, or handle the error
if 'assign4story.txt' in repojson:
    print(repojson['assign4story.txt'])
else:
    print("Key 'assign4story.txt' not found in the response.")



'''
# Define the repository path and files to modify and to modify the name Andrew
repo_path = 'https://github.com/GraceMarySmyth/WSAA-coursework/tree/main/Assignments'
file_name = '/assign4story.txt'
old_name = 'Andrew'
new_name = 'Grace'
old_gender= 'he'
new_gender= 'she'
old_pronown= 'his'
new_pronown= 'her'
old2_pronown= 'him'
new2_pronown= 'her'

# Initialize the repository
repo = git.Repo(repo_path)

# Read the file
file_path = os.path.join(repo_path, file_name)
with open(file_path, 'r') as file:
    file_contents = file.read()

# Replace the old name with the new name
new_file_contents = file_contents.replace(old_name, new_name)
new_file_contents = new_file_contents.replace(old_gender, new_gender)
new_file_contents = new_file_contents.replace(old_pronown, new_pronown) 
new_file_contents = new_file_contents.replace(old2_pronown, new2_pronown)   
# Write the new file contents back to the file
with open(file_path, 'w') as file:
    file.write(new_file_contents)

# Commit the changes
repo.index.add([file_name])
repo.index.commit('Replaced instances of Andrew with Grace')

# Push the changes
origin = repo.remote(name='origin')
origin.push()
'''
