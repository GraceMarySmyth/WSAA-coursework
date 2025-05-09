## Big project for Web Services and Application
Lecturer: Andrew Beatty
Author: Grace Mary Smyth

As per the project outline: 

"Write a program that demonstrates that you understand creating and consuming RESTful APIs. I will allow a lot of flexibility in this project, so that you can use it as an opportunity to do something that is useful for your work.  If you cannot think of a project to do: Create a Web application in Flask that has a RESTful API, the application should link to one or more database tables. You should also create the web pages that can consume the API. I.e. performs CRUD operations on the data. "

Firstly a virtual environment was created using the  following commands: 
    # navigated to my project folder
      cd "C:\Users\grace\WSSAA-Coursework\WSAA-coursework-2\Big Project"  
    # creating a new virtual environment    
        python -m venv venv
    # Activating the virtual environment
        venv\Scripts\activate.bat
    # Installing flask and flask_sqlalchemy
        pip install flask flask_sqlalchemy
    # saved the requirements to requirements.txt
        pip freeze > requirements.txt



In this "Big Project" the following files are contained:
Readme.md
Lists all the files in the project and also contains References used to complete this project.

.gitignore
This is a list of all files and directories which are unnecessary to the project. This will be ignored by git once it is committed to the remote repository.

requirements.txt.
this file contains all the files and version numbers required to run the programme. pip freeze > requirements.txt was the command used to generate this file.

RecipeDAO.py

Server.py

recipe_viewer.html


References:

initial code from:
https://github.com/andrewbeattycourseware/WSAA-Courseware

https://developer.mozilla.org/en-US/docs/Web/CSS/background-color
