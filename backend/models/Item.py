from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from .Base import db
from .Base import ma

class Item(db.Model):
    __tablename__ = "menu_items"
    id = Column(Integer, primary_key = True)
    tag_id = Column(Integer, ForeignKey("tags.tag_id"))
    item_name = Column(String)


class ItemSchema(ma.Schema):
    class Meta: 
        fields = ("id", "item_name", "tag_id")