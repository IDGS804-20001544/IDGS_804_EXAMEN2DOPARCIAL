from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask import Blueprint
from project.models import db, Maestros
import project.forms as forms
from ..db import get_connection



ma = Blueprint('ma', __name__, url_prefix='/ma')

@ma.route('/crear_maestros',methods = ['GET', 'POST'])
def insert_maestro():
    create_form = forms.MaestrosForm(request.form)
    if request.method == 'POST':
        nombre=create_form.nombre.data,
        apaterno=create_form.apaterno.data,
        amaterno=create_form.amaterno.data,
        email=create_form.email.data,
        telefono=create_form.telefono.data
        

        connection=get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL create_maestro(%s,%s,%s,%s,%s) ',(nombre,apaterno,amaterno,email,telefono))
        connection.commit()
        connection.close()
               
        
        return redirect(url_for('ma.leer'))
    return render_template('crear_maestros.html',form=create_form)



@ma.route('/leer_maestros',methods = ['GET', 'POST'])
def leer():
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute('CALL get_maestros()')
        maestros = cursor.fetchall()
    return render_template('leer_maestros.html',maestros=maestros)

@ma.route('/actualizar_maestros',methods = ['GET', 'POST'])
def actualizar():
    update_form = forms.MaestrosForm(request.form)
   
    
    if request.method == 'GET':
        id=request.args.get('id')
        ma = db.session.query(Maestros).filter(Maestros.id == id).first()
        update_form.id.data = request.args.get('id')
        update_form.nombre.data = ma.nombre
        update_form.apaterno.data = ma.apaterno
        update_form.amaterno.data = ma.amaterno
        update_form.email.data = ma.email
        update_form.telefono.data = ma.telefono
        
    if request.method == 'POST':
        id = update_form.id.data
        nombre=update_form.nombre.data
        apaterno=update_form.apaterno.data
        amaterno=update_form.amaterno.data
        email=update_form.email.data
        telefono=update_form.telefono.data
       
     
        connection=get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL update_maestro(%s,%s,%s,%s,%s,%s) ',(id,nombre,apaterno,amaterno,email,telefono))
        connection.commit()
        connection.close()
               
        
        return redirect(url_for('ma.leer'))
    return render_template('actualizar_maestros.html',form=update_form)

@ma.route('/eliminar_maestros',methods = ['GET', 'POST'])
def eliminar():
    delete_form = forms.MaestrosForm(request.form)
    if request.method == 'GET':
            id=request.args.get('id')
            ma = db.session.query(Maestros).filter(Maestros.id == id).first()
            delete_form.id.data = request.args.get('id')
            delete_form.nombre.data = ma.nombre
            delete_form.apaterno.data = ma.apaterno
            delete_form.amaterno.data = ma.amaterno
            delete_form.email.data = ma.email
            delete_form.telefono.data = ma.telefono
        
    if request.method == 'POST':
        id = delete_form.id.data
        
       
     
        connection=get_connection()
        with connection.cursor() as cursor:
            cursor.execute('CALL delete_maestro(%s) ',(id))
        connection.commit()
        connection.close()
               
        
        return redirect(url_for('ma.leer'))
    return render_template('eliminar_maestros.html',form=delete_form)