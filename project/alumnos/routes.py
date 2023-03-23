from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask import Blueprint
from project.models import db, Alumnos
import project.forms as forms

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/crear_alumnos',methods = ['GET', 'POST'])
def crear():
    create_form = forms.AlumnosForm(request.form)
    if request.method == 'POST':
        alu = Alumnos(nombre = create_form.nombre.data,
                      apaterno = create_form.apaterno.data,
                      amaterno = create_form.amaterno.data,
                      email = create_form.email.data,
                      carrera = create_form.carrera.data)
        db.session.add(alu)
        db.session.commit()
        return redirect(url_for('auth.leer'))
    return render_template('crear_alumnos.html',form = create_form)

@auth.route('/leer_alumnos',methods = ['GET', 'POST'])
def leer():
    read_form = forms.AlumnosForm(request.form)
    alumnos = Alumnos.query.all()
    return render_template('leer_alumnos.html', form = read_form, alumnos = alumnos)

@auth.route('/actualizar_alumnos',methods = ['GET', 'POST'])
def actualizar():
    update_form = forms.AlumnosForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')

        alu = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        update_form.id.data = request.args.get('id')
        update_form.nombre.data = alu.nombre
        update_form.apaterno.data = alu.apaterno
        update_form.amaterno.data = alu.amaterno
        update_form.email.data = alu.email
        update_form.carrera.data = alu.carrera

    if request.method == 'POST':
        id = update_form.id.data
        alum = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        alum.nombre = update_form.nombre.data
        alum.apaterno = update_form.apaterno.data
        alum.amaterno = update_form.amaterno.data
        alum.email = update_form.email.data
        alum.carrera = update_form.carrera.data

        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('auth.leer'))
    
    return render_template('actualizar_alumnos.html',form = update_form)

@auth.route('/eliminar_alumnos',methods = ['GET', 'POST'])
def eliminar():
    delete_form = forms.AlumnosForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')

        alu = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        delete_form.id.data = request.args.get('id')
        delete_form.nombre.data = alu.nombre
        delete_form.apaterno.data = alu.apaterno
        delete_form.amaterno.data = alu.amaterno
        delete_form.email.data = alu.email
        delete_form.carrera.data = alu.carrera

    if request.method == 'POST':
        id = delete_form.id.data
        alum = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        alum.nombre = delete_form.nombre.data
        alum.apaterno = delete_form.apaterno.data
        alum.amaterno = delete_form.amaterno.data
        alum.email = delete_form.email.data
        alum.carrera = delete_form.carrera.data

        db.session.delete(alum)
        db.session.commit()
        
        return redirect(url_for('auth.leer'))
    return render_template('eliminar_alumnos.html', form = delete_form)
