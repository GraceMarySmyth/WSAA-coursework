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

Server.py
This is where Flask was used to create an app server. The flask API is for frontend/backend interactions.

RecipeDAO.py
"Data Access Object" It is used to separate database logic or operations from the rest of the app. This allows a clearer interaction with the MySQL databse that holds the recipe data. This handles raw SQL database operations.

sql.py
This programme loads the data directly from a SQL database. It configures how the SQL connection and query work using "sqlConfig" and implements how to read and convert the query results into the dataset. this is the custom loader for datasets (used for data science, analysis, etc.)

recipe_viewer.html


References:

initial code from:
https://github.com/andrewbeattycourseware/WSAA-Courseware

https://flask.palletsprojects.com/en/stable/quickstart/

https://flask.palletsprojects.com/en/stable/quickstart/#routing

https://flask.palletsprojects.com/en/stable/quickstart/#debug-mode

https://www.geeksforgeeks.org/use-jsonify-instead-of-json-dumps-in-flask/

https://medium.com/@sujathamudadla1213/jsonify-method-in-flask-ecfa5e483c29

http://docs.sqlalchemy.org/en/latest/faq/sqlexpressions.html

https://developer.mozilla.org/en-US/docs/Web/CSS/background-color
