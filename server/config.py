import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:admin@db/osm-data"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    os.environ["PGPASSWORD"] = 'admin'