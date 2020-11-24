from sqlalchemy import Column, Integer,String
from sqlalchemy.orm import relationship
from .Base import ma
from .Base import db
from .Item import Item
from flask_marshmallow import Marshmallow

class Tag(db.Model):
    __tablename__ = "tags"
    tag_id = Column(Integer, primary_key = True)
    tag_name = Column(String)
    items = relationship("Item")

class TagSchema(ma.Schema):
    class Meta:
        fields = ("tag_id", "tag_name", "items")