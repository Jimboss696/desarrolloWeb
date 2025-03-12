from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

class ContactoForm(FlaskForm):
    nombre = StringField("Nombre", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired(), Email()])
    mensaje = TextAreaField("Mensaje", validators=[DataRequired()])
    submit = SubmitField("Enviar")
