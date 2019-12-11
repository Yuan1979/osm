from flask_restful import Api

def create_api(app):
    api = Api(app)

    api_version = '0.1'

    #api.add_resource(way)

    return api