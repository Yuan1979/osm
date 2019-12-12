from sqlalchemy import Column, Integer, String
from domain import Sharp2Entity

class NodeModel(Sharp2Entity):
    __tablename__ = "public.planet_osm_point"
    osm_id = Column(Integer, primary_key=True)