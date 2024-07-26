import psycopg2
from flask import Flask, request, redirect, render_template, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import PasswordField, StringField, SubmitField
import db
from forms import LibrosForm
# from flask_wtf import CSRFProtect


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY']= 'SUPER SECRETO'
# csrf = CSRFProtect(app)


@app.route('/')
def index():
    return render_template('base.html')

@app.errorhandler(404)
def error404(error):
    return render_template('404.html')


@app.route('/libros')
def libros():
    conn = db.conectar()
    #crear un cursor (objeto para recorrer las tablas)

    cursor = conn.cursor()
    #ejecutar un consulta en postgres
    cursor.execute('''SELECT * FROM libros_view''')
    #recuperar la informacion
    datos=cursor.fetchall()
    #cerrar cursor y conexion a la base de datos
    cursor.close()
    db.desconectar(conn)
    return render_template('libros.html', datos=datos)


@app.route('/insertar_libro', methods=['GET', 'POST'])
def insertar_libro():
    form = LibrosForm()
    if form.validate_on_submit():
        titulo = form.titulo.data
        fk_autor = form.fk_autor.data  # Cambio aquí
        fk_editorial = form.fk_editorial.data
        edicion = form.edicion.data
        conn = db.conectar()
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO libro (titulo, fk_autor, fk_editorial, edicion)
                     VALUES (%s, %s, %s, %s)
        ''', (titulo, fk_autor, fk_editorial, edicion))
        conn.commit()
        cursor.close()
        db.desconectar(conn)  # Cambio aquí
        flash('LIBRO AÑADIDO CORRECTAMENTE')
        return redirect(url_for('libros'))  # Corrige el nombre de la función para redirigir

    return render_template('insertar_libro.html', form=form)



@app.route('/autores')
def autores():
    conn = db.conectar()
    #conectar con la base de datos

    #crear un cursor (objeto para recorrer las tablas)

    cursor = conn.cursor()
    #ejecutar un consulta en postgres
    cursor.execute('''SELECT * FROM autores_view ORDER BY id_autor''')
    #recuperar la informacion
    datos=cursor.fetchall()
    #cerrar cursor y conexion a la base de datos
    cursor.close()
    db.desconectar(conn)

    return render_template('autores.html', datos=datos)


@app.route('/paises')
def paises():
    conn = db.conectar()
    #conectar con la base de datos

    #crear un cursor (objeto para recorrer las tablas)

    cursor = conn.cursor()
    #ejecutar un consulta en postgres
    cursor.execute('''SELECT * FROM pais ORDER BY id_pais''')
    #recuperar la informacion
    datos=cursor.fetchall()
    #cerrar cursor y conexion a la base de datos
    cursor.close()
    db.desconectar(conn)

    return render_template('paises.html', datos=datos)


@app.route('/delete_pais/<int:id_pais>', methods=['POST'])
def delete_pais(id_pais):
    conn = db.conectar()
    #conectar con la base de datos

    #crear un cursor (objeto para recorrer las tablas)

    cursor = conn.cursor()
    #Borrar el registro con el id_pais seleccionado
    cursor.execute('''DELETE FROM pais WHERE id_pais=%s''', (id_pais,))
    conn.commit()
    cursor.close()
    db.desconectar(conn)

    return redirect(url_for('index'))

@app.route('/update1_pais/<int:id_pais>', methods=['POST'])
def update1_pais(id_pais):
    conn = db.conectar()
    #conectar con la base de datos
    #crear un cursor (objeto para recorrer las tablas)
    cursor = conn.cursor()
    #recuperar el registro del pais seleccionado
    cursor.execute('''SELECT * FROM pais WHERE id_pais=%s''', (id_pais,))
    datos=cursor.fetchall()
    cursor.close()
    db.desconectar(conn)

    return render_template('editar_pais.html', datos=datos)

@app.route('/update2_pais/<int:id_pais>', methods=['POST'])
def update2_pais(id_pais):
    conn = db.conectar()
    nombre = request.form['nombre']
    #conectar con la base de datos
    #crear un cursor (objeto para recorrer las tablas)
    cursor = conn.cursor()
    cursor.execute('''UPDATE pais SET nombre=%s WHERE id_pais=%s''', (nombre, id_pais))
    conn.commit()
    cursor.close()
    return redirect(url_for('index'))

@app.route('/update1_libro/<int:id_libro>', methods=['POST'])
def update1_libro(id_libro):
    conn = db.conectar()
    #conectar con la base de datos
    #crear un cursor (objeto para recorrer las tablas)
    cursor = conn.cursor()
    #recuperar el registro del pais seleccionado
    cursor.execute('''SELECT * FROM libro WHERE id_libro=%s''', (id_libro,))
    datos=cursor.fetchall()
    cursor.close()
    db.desconectar(conn)

    return render_template('editar_libro.html', datos=datos)

@app.route('/update2_libro/<int:id_libro>', methods=['POST'])
def update2_libro(id_libro):
    conn = db.conectar()
    nombre = request.form['nombre']
    #conectar con la base de datos
    #crear un cursor (objeto para recorrer las tablas)
    cursor = conn.cursor()
    cursor.execute('''UPDATE libro SET nombre=%s WHERE id_libro=%s''', (nombre, id_libro))
    conn.commit()
    cursor.close()
    return redirect(url_for('index'))

@app.route('/delete_libro/<int:id_libro>', methods=['POST'])
def delete_libro(id_libro):
    conn = db.conectar()
    #conectar con la base de datos

    #crear un cursor (objeto para recorrer las tablas)

    cursor = conn.cursor()
    #Borrar el registro con el id_pais seleccionado
    cursor.execute('''DELETE FROM libro WHERE id_libro=%s''', (id_libro,))
    conn.commit()
    cursor.close()
    db.desconectar(conn)

    return redirect(url_for('index'))