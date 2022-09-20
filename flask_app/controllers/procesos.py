from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.auto import Auto
from flask_app.models.user import Usuario
from flask_app.models.proceso import Proceso

@app.route('/edit/estado/<int:id_proceso>')
def edit_estado(id_proceso):
    print("el id es:", id_proceso)
    if 'users_id' not in session:
        return redirect('/logout')
    data = {
        "id_proceso":id_proceso
    }
    return render_template("editestado.html",edit=Proceso.get_one(data))


@app.route('/update/proceso',methods=['POST'])
def update_proceso():
    if 'users_id' not in session:
        return redirect('/logout')
#    if not Recipe.validate_recipe(request.form):
#        return redirect('/new/recipe')
    data = {
        "abcmotor": request.form["abcmotor"],
        "abcfrenos": request.form["abcfrenos"],
        "suspension": request.form["suspension"],
        "liquidos": request.form["liquidos"],
        "luces": request.form["luces"],
        "id_proceso": request.form['id_proceso']
    }
    Auto.update(data)
    return redirect('/dashboard')

@app.route('/ver/proceso/<int:id_proceso>')
def show_proceso(id_proceso):
    if 'users_id' not in session:
        return redirect('/logout')
    data = {
        "id_proceso":id_proceso
    }
    return render_template("verestado.html",estado=Proceso.get_one(data))

@app.route('/ver/procesocli/<int:id_proceso>')
def show_procesocli(id_proceso):
    if 'users_id' not in session:
        return redirect('/logout')
    data = {
        "id_proceso":id_proceso
    }
    return render_template("verestadocli.html",estado=Proceso.get_one(data))