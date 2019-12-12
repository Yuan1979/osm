from flask import abort
from domain import db

class DatabaseService(object):

    """
    class:`Service` instance encapsulates common SQLAlchemy model
    operations in the context of a :class:`Flask` application.
    """

    def __init__(self, model):
        self._model = model

    
    def get(self):
        """
        Returns an instance of the service's model with the specified id.
        Returns `None` if an instance with the specified id does not exist.
        :param id: the instance id
        """
        with self._begin_transaction():
            return self._model.query.all()
    
    def _begin_transaction(self):
        return db.session.begin(subtransactions=True)

    