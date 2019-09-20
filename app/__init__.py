from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
import dash

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)


def register_dashboard(server):
    from app.dashboard.layout import layout
    from app.dashboard.callback import register_callbacks

    meta_viewport = {"name": "viewport", "content": "width=device-width, initial-scale=1, shrink-to-fit=yes"}

    dashboard = dash.Dash(__name__,
                          server=server,
                          url_base_pathname='/dashboard/',
                          meta_tags=[meta_viewport])

    with server.app_context():
        dashboard.title = 'Mario'
        dashboard.layout = layout
        register_callbacks(dashboard)


register_dashboard(app)

from app import routes, models
