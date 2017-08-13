import datetime

import config

import pymysql

#DB Settings
connect = pymysql.connect(host='localhost', user=config.user, password=config.password, db=config.db, autocommit=True, cursorclass=pymysql.cursors.DictCursor)

#DB Commands Class
class DBQ():

    #DB Connection Function
    def connect(self, database="selftrack"):
        return pymysql.connect(host='localhost', user=config.user, password=config.password, db=config.db, autocommit=True, cursorclass=pymysql.cursors.DictCursor)

    def create_exercise(self, type, timenote, reps, sets, weight, unit):
        conn = self.connect()
        try:
            query = "INSERT INTO exercise (type,timenote, reps, sets, weight, unit)\
             VALUES (%s,%s,%s,%s, %s, %s);"
            with conn.cursor() as cursor:
                cursor.execute(query, (type,timenote, reps, sets, weight, unit))
        except Exception as e:
            print(e)
        finally:
            conn.close()
