import sqlite3 as dbapi2

from sqlalchemy.ext.automap import automap_base
# import os

Base = automap_base()
# reflect the tables
Base.prepare(app.db.engine, reflect=True)

MoistHist = Base.classes.MOISTHIST
WaterHist = Base.classes.WATERHIST
# class MoistHist(db.Model):
#     __table__ = Table('mytable', Base.metadata,
#                     autoload=True, autoload_with=some_engine)
#     id = db.Column(db.Integer, primary_key=True)
#     eventtime = db.Column(db.DateTime, nullable=False)
#     status = db.Column(db.Integer, nullable=False)
#
#     def __repr__(self):
#         return '<MoistHist %r>' % self.eventtime
#
#     # def add_obs(self, eventtime, status):
#     #     self.add()
#
# class WaterHist(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     eventtime = db.Column(db.DateTime, nullable=False)
#     status = db.Column(db.Float, nullable=False)
#
#     def __repr__(self):
#         return '<MWaterHist %r>' % self.eventtime
    #
    # # def init_db(self):
    # #     with
    # #         "CREATE TABLE IF NOT EXISTS MOISTHIST (KEY integer PRIMARY KEY,eventtime datetime NOT NULL,status INTEGER NOT NULL);"
    # #         "CREATE TABLE IF NOT EXISTS WATERHIST (KEY integer PRIMARY KEY,eventtime datetime NOT NULL,DURATION FLOAT NOT NULL);"
    # def add_obs(self, status):
    #     with dbapi2.connect(self.dbfile) as connection:
    #         cursor = connection.cursor()
    #         query = "INSERT INTO MOISTHIST (EVENTTIME, STATUS) VALUES (?, ?);"
    #         cursor.execute(query, (status["eventtime"], status["status"]))
    #         connection.commit()
    #         self.last_key = cursor.lastrowid
    #
    # def delete_obs(self, key):
    #     with dbapi2.connect(self.dbfile) as connection:
    #         cursor = connection.cursor()
    #         query = "DELETE FROM MOISTHIST WHERE (ID = ?)"
    #         cursor.execute(query, (key,))
    #         connection.commit()
    #
    # def correct_obs(self, key, status):
    #     with dbapi2.connect(self.dbfile) as connection:
    #         cursor = connection.cursor()
    #         query = "UPDATE MOISTHIST SET EVENTTIME = ?, STATUS = ? WHERE (ID = ?)"
    #         cursor.execute(query, (status["eventtime"], status["status"], key))
    #         connection.commit()
    #
    # def get_numobs(self, numobs):
    #     with dbapi2.connect(self.dbfile) as connection:
    #         cursor = connection.cursor()
    #         query = "SELECT KEY, EVENTTIME,STATUS FROM MOISTHIST ORDER BY EVENTTIME DESC LIMIT ?"
    #         cursor.execute(query, [numobs])
    #         moist_hist = cursor.fetchall()
    #     return moist_hist
    #
    # def get_timeobs(self, obssince):
    #     with dbapi2.connect(self.dbfile) as connection:
    #         cursor = connection.cursor()
    #         query = "SELECT KEY, EVENTTIME,STATUS FROM MOISTHIST WHERE EVENTTIME > ?"
    #         cursor.execute(query, [obssince])
    #         moist_hist = cursor.fetchall()
    #     return moist_hist
    #
    # def get_allobs(self):
    #     with dbapi2.connect(self.dbfile) as connection:
    #         cursor = connection.cursor()
    #         query = "SELECT KEY, EVENTTIME,STATUS FROM MOISTHIST ORDER BY EVENTTIME DESC"
    #         cursor.execute(query)
    #         moist_hist = [(key, eventtime, status)
    #                       for key, eventtime, status in cursor]
    #         return moist_hist
    #
    # def add_water(self, status):
    #     with dbapi2.connect(self.dbfile) as connection:
    #         cursor = connection.cursor()
    #         query = "INSERT INTO WATERHIST (EVENTTIME, DURATION) VALUES (?, ?);"
    #         cursor.execute(query, (status["eventtime"], status["duration"]))
    #         connection.commit()
    #         self.last_key = cursor.lastrowid
    #
    # def get_numwater(self, numobs):
    #     with dbapi2.connect(self.dbfile) as connection:
    #         cursor = connection.cursor()
    #         query = "SELECT KEY, EVENTTIME,DURATION FROM WATERHIST ORDER BY  EVENTTIME DESC LIMIT ?"
    #         cursor.execute(query, [numobs])
    #         water_hist = cursor.fetchall()
    #     return water_hist
    #
    # def get_timewater(self, obssince):
    #     with dbapi2.connect(self.dbfile) as connection:
    #         cursor = connection.cursor()
    #         query = "SELECT KEY, EVENTTIME,DURATION FROM WATERHIST WHERE EVENTTIME > ?"
    #         cursor.execute(query, [obssince])
    #         water_hist = cursor.fetchall()
    #     return water_hist
    #
    # def get_allwater(self):
    #     with dbapi2.connect(self.dbfile) as connection:
    #         cursor = connection.cursor()
    #         query = "SELECT KEY, EVENTTIME, DURATION FROM WATERHIST ORDER BY  EVENTTIME DESC"
    #         cursor.execute(query)
    #         water_hist = cursor.fetchall()
    #         return water_hist