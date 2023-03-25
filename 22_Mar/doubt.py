
import sqlite3
from Task_model import task,taskStatus
            


def isPresent(id):
    es=taskStatus(0, "Not Found", None)
    try:
        sqliteConnection = sqlite3.connect('test.db')
        cursor = sqliteConnection.cursor()
        sql_select_query = """select * from task where taskid = ?"""
        cursor.execute(sql_select_query, (id,))
        records = cursor.fetchall()
        print("Printing ID ", id)
        for row in records:
            found=True
            e= task(row[0],row[1],row[2],row[3])
            es.statuscode=1
            es.message="Task Found"
            es.taskobj="1"
        cursor.close()

    except sqlite3.Error as error:
        es.message=error
    finally:
        if sqliteConnection:
            sqliteConnection.close()
    return es


def insertVaribleIntoTable(e):
    try:
        sqliteConnection = sqlite3.connect('test.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_query = """INSERT INTO task
                          (id,taskname,description,priority) 
                           VALUES 
                          (?,?,?,?)"""

        data_tuple = (e.id, e.taskname, e.description, e.priority)
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
    return data_tuple

def updateSqliteTable(x):
    try:
        sqliteConnection = sqlite3.connect('test.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        # sql_update_query = """Update task set salary = ? where id = ?"""
        sql_update_query =  """Update task set taskname = ?, description = ?, priority = ? where id = ?"""
        data = (x.taskname, x.description, x.priority, id)
        cursor.execute(sql_update_query, data)
        sqliteConnection.commit()
        if cursor.rowcount != 0:
            print("update successful")
        else:
            print("no rows where found in the table matching the where condition")


        print("Record Updated successfully")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
    return data
    

def popTask(id):
    # DELETE FROM MySQL_table WHERE id=10;

    try:
        sqliteConnection = sqlite3.connect('test.db')
        cursor = sqliteConnection.cursor()
        sql_delete_query = """DELETE from task where id = ?"""
        cursor.execute(sql_delete_query,(id,))
        sqliteConnection.commit()
        print("Record deleted successfully ")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")



id=int(input("Enter the id: "))

res=popTask(id)
print(res,"\n")