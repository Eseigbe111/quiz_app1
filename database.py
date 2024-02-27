import sqlite3 # this is bcos we used sqlite3 to create the backend database
from flask import g # "g" is a global variable used for database connection


def connect_to_database():
    sql = sqlite3.connect("C:/Users/GUDNES/Desktop/quiz_app1/quizapp.db")
    sql.row_factory = sqlite3.Row
    return sql

def getDatabase():
    if not hasattr(g, "quizapp_db"): # this checks if g does not have an attribute called quizapp_db
         # creating the attribute if it does not exist
         g.quizapp_db = connect_to_database() # connecting it to the database gotten above to access the database 
    return g.quizapp_db # returning the stored database