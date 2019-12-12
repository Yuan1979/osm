from service.database.DatabaseService import DatabaseService
from domain.NodeModel import NodeModel

class DatabaseServiceFactory(object):
    @staticmethod
    def get(type):
        if type == 'Nodes':
            return DatabaseService(NodeModel)
        else:
            raise Exception("Trying to get unknown database service: " + str(type))