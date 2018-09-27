import mysql.connector

if __name__ == '__main__':
    dbconnection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="bltp"
    )
    dbcursor = dbconnection.cursor()
    dbcursor.execute("SELECT link FROM tpindextest")
    temp = dbcursor.fetchall()
    print(temp)
