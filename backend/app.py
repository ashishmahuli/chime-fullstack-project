from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

# import db & models
from models import db, ExampleModel, Item, Tag, ItemSchema, TagSchema

app = Flask(__name__.split('.')[0])
CORS(app)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "menu.db")

db.init_app(app)

tag_schema = TagSchema()
tags_schema = TagSchema(many = True)

item_schema = ItemSchema()
items_schema = ItemSchema(many = True)



@app.route("/api/example", methods=["GET", "POST", "PUT", "DELETE"])
def ExampleEndpoint():
    result = db.session.query(ExampleModel).filter(ExampleModel.number > 1)
    tag1 = Tag(tag_name = "soup")
    tag2 = Tag(tag_name = "meat")
    db.session.add(tag1)
    db.session.add(tag2)
    db.session.commit()
    return {
        "results": "you did it"
    }, 200


@app.route("/tags_all", methods = ["GET"])
def getAllTags():
    tagList = db.session.query(Tag).all()
    result = tags_schema.dump(tagList)
    return jsonify(result)


@app.route("/tags_add", methods = ["POST"])
def addTag():
    tagName = request.json["tag_name"]
    newTag = Tag(tag_name = tagName)
    db.session.add(newTag)
    db.session.commit()
    return jsonify(tag_schema.dump(newTag))


@app.route("/items_all", methods = ["GET"])
def getAllItems():
    itemList = db.session.query(Item).all()
    result = items_schema.dump(itemList)
    return jsonify(result)


@app.route("/items_add", methods = ["POST"])
def addItems():
    
    itemName = request.json["item_name"]
    tagName = request.json["tag_name"]
    newItem = Item(item_name = itemName)
    if tagName != "":
        tag = db.session.query(Tag).filter_by(tag_name = tagName).first()
        tag.items.append(newItem)
    else:
        db.session.add(newItem)
        
    db.session.commit()

    return jsonify(item_schema.dump(newItem))



with app.app_context():
	db.create_all()

if __name__ == "__main__":
    app.run()
