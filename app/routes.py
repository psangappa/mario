from app import app
from flask_restful import Api
from app.endpoints import SavePrinces, ViewApiData, ViewApiDataById
from flask import request

from app import db
from app.models import ApiData

api = Api(app, catch_all_404s=True)
api.add_resource(SavePrinces, '/api/v1/mario/<int:n>/<string:grid>')
api.add_resource(ViewApiDataById, '/api/v1/logs/<int:_id>')
api.add_resource(ViewApiData, '/api/v1/logs')


@app.before_request
def log_requests():
    """ Store the request data in the app_data table whenever user makes a request to save princess """
    if request.endpoint == 'saveprinces':
        url = request.url
        remote_address = request.remote_addr
        n = request.view_args['n']
        grid = request.view_args['grid']
        api_data = ApiData(n=n, grid=grid, url=url, remote_address=remote_address)
        db.session.add(api_data)
        db.session.commit()
