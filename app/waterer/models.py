from flask import current_app as app
from sqlalchemy.ext.automap import automap_base


Base = automap_base()
# reflect the tables
Base.prepare(app.db.engine, reflect=True)


class MoistHist(app.db.Model):
    id = app.db.Column(app.db.Integer, primary_key=True)
    eventtime = app.db.Column(app.db.DateTime, nullable=False)
    status = app.db.Column(app.db.Boolean, nullable=False)

    def __repr__(self):
        return '<MoistHist %r>' % self.eventtime


class WaterHist(app.db.Model):
    # __table__ = Table('MoistHist', Base.metadata,
    #                   autoload=True, autoload_with=app.db.engine)
    id = app.db.Column(app.db.Integer, primary_key=True)
    eventtime = app.db.Column(app.db.DateTime, nullable=False)
    duration = app.db.Column(app.db.Float, nullable=False)

    def __repr__(self):
        return '<MWaterHist %r>' % self.eventtime



