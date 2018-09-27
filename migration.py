import mysql.connector

if __name__ == '__main__':
    dbconnection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=""
    )
    dbcursor = dbconnection.cursor()
    try:
        dbcursor.execute('CREATE DATABASE bltp')
    except:
        print('database already exist?')
    dbconnection.close


    dbconnection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="bltp"
    )
    dbcursor = dbconnection.cursor()
    try:
        dbcursor.execute('CREATE TABLE tpindex (IDIndex int PRIMARY KEY AUTO_INCREMENT,link varchar(255) NOT NULL, kategori varchar(4) NOT NULL, lastcheck timestamp)')
    except:
        print('table already exist?')
    dbconnection.close

