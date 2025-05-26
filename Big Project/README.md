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
    # to reinstall the packages use the command pip install -r requirements.txt

Running the Code:
    # Two Cmder consoles required.
    # Navigate to "Big Project" in both consoles.
    # In one console run python Server.py
    # In second console run python -m http.server.
    # Open an incognito browser. This is optional depending on browser settings. 
    # in incognito browser open http://localhost:8000/recipe_viewer.html.
    # Smyth Family Recipes available

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

testrecipeDAO.py
this is to test the code. It was suggested by chat GPT as i couldnt ge the code to work initially. There was an issue with my-sql-connector-python not working or stalling silently. Swapped to PyMySQL and code worked and output generated.

test_mysql_connection.py
code to test the connection to MySQL.

dbconfig.py
configuration file for database

recipe_viewer.html

Hosted on-line at:
GraceMarySmyth1.pythonanywhere.com.


References:

initial code from:
https://github.com/andrewbeattycourseware/WSAA-Courseware

https://flask.palletsprojects.com/en/stable/quickstart/

https://flask.palletsprojects.com/en/stable/quickstart/#routing

https://flask.palletsprojects.com/en/stable/quickstart/#debug-mode

https://www.geeksforgeeks.org/use-jsonify-instead-of-json-dumps-in-flask/

https://medium.com/@sujathamudadla1213/jsonify-method-in-flask-ecfa5e483c29

Chat GPT

http://docs.sqlalchemy.org/en/latest/faq/sqlexpressions.html

https://docs.sqlalchemy.org/en/20/errors.html#error-e3q8

https://docs.sqlalchemy.org/en/20/core/pooling.html#pool-disconnects

https://packaging.python.org/en/latest/tutorials/installing-packages/

https://support.microsoft.com/en-us/office/import-or-link-to-data-in-an-sql-server-database-a5a3b4eb-57b9-45a0-b732-77bc6089b84e

https://docs.buildbot.net/latest/manual/configuration/dbconfig.html

https://www.digitalocean.com/community/tutorials/how-to-import-and-export-databases-in-mysql-or-mariadb

https://stackoverflow.com/questions/42906665/import-my-database-connection-with-python

https://developer.mozilla.org/en-US/docs/Web/CSS/background-color

https://www.w3schools.com/html/html_comments.asp

https://forum.freecodecamp.org/t/solved-fetch-api-not-working-at-all-or-working-only-half-the-time

https://www.geeksforgeeks.org/what-is-javascript-rendering/

https://crawlee.dev/js/docs/guides/javascript-rendering

https://www.youtube.com/watch?v=czZ1PvNW5hk
