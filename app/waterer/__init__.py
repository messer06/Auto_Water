"""Initialize Flask app."""
from flask import Flask
from flask_assets import Environment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.ext.automap import automap_base


def create_app():
    """Construct core Flask application with embedded Dash app."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    app.db = SQLAlchemy(app)

    Base = automap_base()
    # reflect the tables
    Base.prepare(app.db.engine, reflect=True)
    # MoistHist = Base.classes.MOISTHIST
    # WaterHist = Base.classes.WATERHIST

    assets = Environment()
    assets.init_app(app)
    migrate = Migrate(app,app.db)

    with app.app_context():
        # Import parts of our core Flask app
        from . import web_plants
        from .assets import compile_static_assets
        from .models import WaterHist, MoistHist

        app.db.WaterHist = WaterHist
        app.db.MoistHist = MoistHist

        # Import Dash application
        from .plotlydash.dashapp1 import create_dashboard
        app = create_dashboard(app)

        # Compile static assets
        compile_static_assets(assets)

        return app


