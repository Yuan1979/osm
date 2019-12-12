from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(session_options={'autocommit': True})

def session():
    with _begin_transaction():
        return db.session


def _begin_transaction():
    return db.session.begin(subtransactions=True)

class Sharp2Entity(db.Model):
    __abstract__ = True