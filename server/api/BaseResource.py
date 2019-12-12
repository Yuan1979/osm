from service.database.DatabaseServiceFactory import DatabaseServiceFactory
from flask_restful import Resource

class BaseResource(Resource):

    def __init__(self):
        self._database_service_factory = DatabaseServiceFactory()