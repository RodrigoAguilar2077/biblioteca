import psycopg2
from flask import Flask, redirect, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import PasswordField, StringField, SubmitField

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('base.html')

@app.route('/libros')
def libros():
    #conectar con la base de datos
    conexion = psycopg2.connect(
        database="biblioteca3a", user="postgres", password="daftpunk2077", host="localhost", port="5432"
    )

    #crear un cursor (objeto para recorrer las tablas)

    cursor = conexion.cursor()
    #ejecutar un consulta en postgres
    cursor.execute('''SELECT * FROM libros_view''')
    #recuperar la informacion
    datos=cursor.fetchall()
    #cerrar cursor y conexion a la base de datos
    cursor.close()
    conexion.close()
    return render_template('libros.html', datos=datos)

@app.route('/autores')
def autores():
    #conectar con la base de datos
    conexion = psycopg2.connect(
        database="biblioteca3a", user="postgres", password="daftpunk2077", host="localhost", port="5432"
    )

    #crear un cursor (objeto para recorrer las tablas)

    cursor = conexion.cursor()
    #ejecutar un consulta en postgres
    cursor.execute('''SELECT * FROM autores_view''')
    #recuperar la informacion
    datos=cursor.fetchall()
    #cerrar cursor y conexion a la base de datos
    cursor.close()
    conexion.close()
    return render_template('autores.html', datos=datos)


@app.route('/paises')
def paises():
    #conectar con la base de datos
    conexion = psycopg2.connect(
        database="biblioteca3a", user="postgres", password="daftpunk2077", host="localhost", port="5432"
    )

    #crear un cursor (objeto para recorrer las tablas)

    cursor = conexion.cursor()
    #ejecutar un consulta en postgres
    cursor.execute('''SELECT * FROM pais''')
    #recuperar la informacion
    datos=cursor.fetchall()
    #cerrar cursor y conexion a la base de datos
    cursor.close()
    conexion.close()
    return render_template('paises.html', datos=datos)


@app.route('/delete_pais/<int:id_pais>', methods=['POST'])
def delete_pais(id_pais):
    #conectar con la base de datos
    conexion = psycopg2.connect(
        database="biblioteca3a", user="postgres", password="daftpunk2077", host="localhost", port="5432"
    )

    #crear un cursor (objeto para recorrer las tablas)

    cursor = conexion.cursor()
    #Borrar el registro con el id_pais seleccionado
    cursor.execute('''DELETE FROM pais WHERE id_pais=%s''', (id_pais,))
    conexion.commit()
    cursor.close()
    conexion.close()
    return redirect(url_for('index'))

@app.route('/update_pais/<int:id_pais>', methods=['GET', 'POST'])
def update1_pais(id_pais):
    #conectar con la base de datos
    conexion = psycopg2.connect(
        database="biblioteca3a", user="postgres", password="daftpunk2077", host="localhost", port="5432"
    )

    #crear un cursor (objeto para recorrer las tablas)

    cursor = conexion.cursor()
    #recuperar el registro del pais seleccionado
    cursor.execute('''SELECT * FROM pais WHERE id_pais=%s''', (id_pais,))
    cursor.close()
    conexion.close()
    return redirect(url_for('update2'))