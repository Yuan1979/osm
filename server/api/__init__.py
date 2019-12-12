from flask_restful import Api

from api.NodeResource import NodeResource

def create_api(app):
    api = Api(app)

    api_version = '0.1'

    api.add_resource(NodeResource, '/api/%s/nodes' % api_version)

    return api