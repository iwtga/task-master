# task-master
A simple to-do list web application built using the Flask web framework and utilizes the Sqlite3 database.

## Installation:
1. Create an virtual environment ```python -m venv venv```
2. Activate the [virtual environment](https://docs.python.org/3/tutorial/venv.html). 
3. ```pip install -r requirements.txt```
4. Create a .env file for storing environment variables:
```
FLASK_APP=run
FLASK_ENV=development
SECRET_KEY=EnterAnyRandomKeyHere
DATABASE_URI_LOCAL=sqlite:///main.db
```
5. Create Tables: ```python3 db_create.py```
6. ```flask run```
