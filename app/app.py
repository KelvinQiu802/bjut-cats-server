from flask import Flask
from blueprints import cats, users, images, articles, auth, imageLikes
from extentions import db
from config.config import DIALECT, USER_NAME, PASSWORD, HOST, DATABASE, PORT
from flask_cors import CORS


app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

db_url = f'{DIALECT}://{USER_NAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'
app.config["SQLALCHEMY_DATABASE_URI"] = db_url
db.init_app(app)

app.register_blueprint(cats.cats, url_prefix='/api/cats')
app.register_blueprint(users.users, url_prefix='/api/users')
app.register_blueprint(images.images, url_prefix='/api/images')
app.register_blueprint(articles.articles, url_prefix='/api/articles')
app.register_blueprint(auth.auth, url_prefix='/api')
app.register_blueprint(imageLikes.imageLikes, url_prefix='/api/imageLikes')

# Init the DB
with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True, port=7070)
