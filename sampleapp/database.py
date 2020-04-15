from flask_sqlalchemy impoer SQLAlachemy

db = SQLAlachemy()

def init_db(app):
    db.init_app(app)
    