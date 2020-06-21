import sqlite3 as dbapi2

class Moist_Hist:
    def __init__(self, dbfile):
        self.dbfile = dbfile
        self.last_key = None

    def add_obs(self, status):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO MOISTHIST (EVENTTIME, STATUS) VALUES (?, ?);"
            cursor.execute(query, (status["eventtime"], status["status"]))
            connection.commit()
            self.last_key = cursor.lastrowid

    def delete_obs(self, key):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM MOISTHIST WHERE (ID = ?)"
            cursor.execute(query, (key,))
            connection.commit()

    def correct_obs(self, key, status):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "UPDATE MOISTHIST SET EVENTTIME = ?, STATUS = ? WHERE (ID = ?)"
            cursor.execute(query, (status["eventtime"], status["status"], key))
            connection.commit()

    def get_numobs(self, numobs):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT KEY, EVENTTIME,STATUS FROM MOISTHIST ORDER BY EVENTTIME DESC LIMIT ?"
            cursor.execute(query, [numobs])
            moist_hist = cursor.fetchall()
        return moist_hist

    def get_timeobs(self, obssince):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT KEY, EVENTTIME,STATUS FROM MOISTHIST WHERE EVENTTIME > ?"
            cursor.execute(query, [obssince])
            moist_hist = cursor.fetchall()
        return moist_hist

    def get_allobs(self):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT KEY, EVENTTIME,STATUS FROM MOISTHIST ORDER BY EVENTTIME DESC"
            cursor.execute(query)
            moist_hist = [(key, eventtime, status)
                          for key, eventtime, status in cursor]
            return moist_hist

    def add_water(self, status):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO WATERHIST (EVENTTIME, DURATION) VALUES (?, ?);"
            cursor.execute(query, (status["eventtime"], status["duration"]))
            connection.commit()
            self.last_key = cursor.lastrowid

    def get_numwater(self, numobs):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT KEY, EVENTTIME,DURATION FROM WATERHIST ORDER BY  EVENTTIME DESC LIMIT ?"
            cursor.execute(query, [numobs])
            water_hist = cursor.fetchall()
        return water_hist

    def get_timewater(self, obssince):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT KEY, EVENTTIME,DURATION FROM WATERHIST WHERE EVENTTIME > ?"
            cursor.execute(query, [obssince])
            water_hist = cursor.fetchall()
        return water_hist

    def get_allwater(self):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT KEY, EVENTTIME, DURATION FROM WATERHIST ORDER BY  EVENTTIME DESC"
            cursor.execute(query)
            water_hist = cursor.fetchall()
            return water_hist