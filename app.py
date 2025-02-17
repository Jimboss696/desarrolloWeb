from flask import Flask, render_template
import os


app = Flask(__name__)


# Configurar la carpeta de archivos estáticos
app.config['STATIC_FOLDER'] = 'static'


# Ruta principal que carga el archivo index.html
@app.route('/')
def home():
    return render_template('index.html')


# Ruta personalizada con parámetro dinámico
@app.route('/usuario/<nombre>')
def usuario(nombre):
    return render_template('usuario.html', nombre=nombre)


# Ruta para productos
@app.route('/productos')
def productos():
    return render_template('productos.html')


# Ruta para contacto
@app.route('/contacto')
def contacto():
    return render_template('contacto.html')


if __name__ == '__main__':
    # Asegurar que Flask encuentra los archivos estáticos
    app.run(debug=True, static_folder=os.path.join(os.getcwd(), 'static'))
