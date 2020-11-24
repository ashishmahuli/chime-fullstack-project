from flask import Flask
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
    db.session.add(tag1)
    db.session.commit()
    return {
        "results": "you did it"
    }, 200





with app.app_context():
	db.create_all()

if __name__ == "__main__":
    app.run()
