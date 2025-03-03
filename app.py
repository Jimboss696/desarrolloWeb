from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Necesario para usar formularios de Flask-WTF


# Definición del formulario de contacto
class ContactForm(FlaskForm):
    name = StringField("Nombre", validators=[DataRequired()])
    email = EmailField("Correo Electrónico", validators=[DataRequired(), Email()])
    message = TextAreaField("Mensaje", validators=[DataRequired()])
    submit = SubmitField("Enviar")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/productos")
def productos():
    return render_template("productos.html")


@app.route("/contacto", methods=["GET", "POST"])
def contacto():
    form = ContactForm()
    if form.validate_on_submit():
        flash(f"Mensaje enviado por {form.name.data} ({form.email.data})", "success")
        return redirect(url_for("index"))
    return render_template("contacto.html", form=form)


@app.route("/usuario/<nombre>")
def usuario(nombre):
    return render_template("usuario.html", nombre=nombre)


if __name__ == "__main__":
    app.run(debug=True)
