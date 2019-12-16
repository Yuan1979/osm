from api.BaseResource import BaseResource 
from domain import NodeModel


class NodeResource(BaseResource):
    def __init__(self):
        super(self.__class__, self).__init__()
        self._node_service = self._database_service_factory.get('Nodes')

    def get(self):
        nodes = self._node_service.get()
        return len(nodes)
