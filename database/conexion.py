from flask_sqlalchemy import SQLAlchemy
import pymysql  # Asegura que pymysql está importado

pymysql.install_as_MySQLdb()  # Necesario para evitar errores con MySQLdb

db = SQLAlchemy()

def init_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/mi_sistema"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    # Crear las tablas automáticamente si no existen
    with app.app_context():
        db.create_all()
