from flask import jsonify
from flask_restful import Resource

from app.save_princess.save_princess import save_princess
from app.models import ApiData, ApiDataSchema


class SavePrinces(Resource):

    def get(self, n=None, grid=None):
        """
        Get the path to reach princess
        :param n: size of the grid
        :param grid: The Grid
        :return: {'error_flag':True, 'path':[]} - if any of the constrains are violated.
                 {'error_flag':False, 'path':[]} - if all paths to princess are blocked by obstacles
                 {'error_flag':False, 'path':['DOWN', 'DOWN', 'LEFT']} - if we find a shortest path or
                  a possible path to princess
        """
        error_code, paths = save_princess(n, grid)
        return jsonify({'error_flag': error_code, 'paths': paths})


class ViewApiDataById(Resource):

    def get(self, _id=None):
        """
        Get the request api data based on id
        """
        api_data_schema = ApiDataSchema()
        api_data = ApiData.query.get(_id)
        return api_data_schema.dump(api_data)


class ViewApiData(Resource):

    def get(self, _id=None):
        """
        Get all request api data
        """
        api_data_schema = ApiDataSchema(many=True)
        api_data = ApiData.query.all()
        return api_data_schema.dump(api_data)
