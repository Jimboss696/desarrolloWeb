from database.conexion import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # ID autoincremental
    nombre = db.Column(db.String(100), nullable=False)  # Nombre obligatorio
    email = db.Column(db.String(100), unique=True, nullable=False)  # Email único y obligatorio
    mensaje = db.Column(db.Text, nullable=False)  # Nuevo campo para mensajes

    def __repr__(self):
        return f"<Usuario {self.nombre}>"
