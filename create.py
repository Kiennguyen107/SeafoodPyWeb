from flask import Flask
from models import *  # import file models.py previously created

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:kiennguyen1106@localhost:5432/Main"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)  # tie db with flask app


def main():
    db.drop_all()
    db.create_all()


if __name__ == "__main__":
    with app.app_context():  # allow developer interact with flask via command line
        main()
