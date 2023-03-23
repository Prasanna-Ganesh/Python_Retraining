import sqlite3
from emp_model import emp,EmployeeStatusCode

def insertVaribleIntoTable(e):
    try:
        sqliteConnection = sqlite3.connect('test.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_query = """INSERT INTO emp
                          (empno,empname,salary,designation,deptno) 
                           VALUES 
                          (?,?,?,?,?)"""

        data_tuple = (e.empno, e.empname, e.empsalary, e.empdesignation, e.empsalary)
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



def getEmployeeInfo(id):
    es=EmployeeStatusCode(0, "Not Found", None)
    try:
        sqliteConnection = sqlite3.connect('test.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_select_query = """select * from emp where empno = ?"""
        cursor.execute(sql_select_query, (id,))
        records = cursor.fetchall()
        print("Printing ID ", id)
        for row in records:
            found=True
            e= emp(row[0],row[1],row[2],row[3],row[4])
            es.statuscode=1
            es.message="Employee Found"
            es.empobj=e
        cursor.close()

    except sqlite3.Error as error:
        # print("Failed to read data from sqlite table", error)
        es.message=error
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            # print("The SQLite connection is closed")
    return es

def getDeptInfo(id):
    el = []
    try:
        sqliteConnection = sqlite3.connect('test.db')
        cursor = sqliteConnection.cursor()
        sql_select_query = """select * from emp where deptno = ?"""
        cursor.execute(sql_select_query, (id,))
        records = cursor.fetchall()
        for row in records:
            t = emp(row[0],row[1],row[2],row[3],row[4])
            el.append(t)
        cursor.close()
    except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
    return el
    

    