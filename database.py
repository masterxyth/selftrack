
#Python-SQL Library
import pymysql
#DB settings
import config

#database settings
connection = pymysql.connect(host='localhost', user=config.user, passwd=config.password)

#creating the database with try-except
try:
    with connection.cursor() as cursor:

        #creating DB

        sql = "CREATE DATABASE IF NOT EXISTS selftrack"
        cursor.execute(sql)

        #Company TABLE

        sql = """CREATE TABLE IF NOT EXISTS selftrack.exercise (id int NOT NULL AUTO_INCREMENT,
        type VARCHAR(128),
        timenote DATETIME,
        reps int(11),
        sets int(11),
        weight int(11),
        unit VARCHAR(10),
        PRIMARY KEY (id));"""
        cursor.execute(sql)


        #Commit queries
        connection.commit()
finally:
    #Close Connection
    connection.close()
