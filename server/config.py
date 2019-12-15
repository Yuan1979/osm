import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:admin@127.0.0.1/postgres"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    os.environ["PGPASSWORD"] = 'admin'
