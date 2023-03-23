import sqlite3
from TaskModel import task

def insertVaribleIntoTable(task):
    try:
        sqliteConnection = sqlite3.connect('test.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_query = """INSERT INTO task
                          (is,taskname,description,priority) 
                           VALUES 
                          (?,?,?,?)"""

        data_tuple = (task.id,task.taskname,task.description,task.priority)
        cursor.execute(sqlite_insert_query, data_tuple)
        #print(cursor.rowcount)
        sqliteConnection.commit()
        print("Python Variables inserted successfully into SqliteDb_developers table")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
task1=task(1,"project","nothing",5)
task2=task(2,"Project 2","nOOO",4)
insertVaribleIntoTable(task1)
insertVaribleIntoTable(task2)