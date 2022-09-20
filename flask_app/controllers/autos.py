from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.auto import Auto
from flask_app.models.user import Usuario
from flask_app.models.proceso import Proceso

@app.route('/new/auto')
def newauto():
    todos_clientes=Usuario.get_all()
    return render_template('agregarauto.html',clientes=todos_clientes)


@app.route('/create/auto',methods=['POST'])
def create_auto():
    if 'users_id' not in session:
        return redirect('/logout')
#    if not Auto.validate_register(request.form):
#        return redirect('/new/auto')
    data = {
        "usuarios_id_usuario": request.form["usuarios_id_usuario"],
        "placa": request.form["placa"],
        "marca": request.form["marca"],
        "modelo": request.form["modelo"],
    }
    Auto.save(data)    
    return redirect('/dashboard')


@app.route('/start/estado/<int:autos_id_auto>')
def create_estado(autos_id_auto):
    if 'users_id' not in session:
        return redirect('/logout')
#    if not Auto.validate_register(request.form):
#        return redirect('/new/auto')
    data = {
        "autos_id_auto":  autos_id_auto,
    }
    Auto.save_prcesos(data)    
    return redirect('/dashboard')    


# @app.route('/edit/estado/<int:id_proceso>')
# def edit_estado(id_proceso):
#    print("el id es:", id_proceso)
#    if 'users_id' not in session:
#        return redirect('/logout')
#    data = {
#        "id_proceso":id_proceso
#    }
#    return render_template("editestado.html",edit=Proceso.get_one(data))


# @app.route('/update/proceso',methods=['POST'])
# def update_proceso():
#    if 'users_id' not in session:
#        return redirect('/logout')
#    if not Recipe.validate_recipe(request.form):
#        return redirect('/new/recipe')
#    data = {
#        "abcmotor": request.form["abcmotor"],
#        "abcfrenos": request.form["abcfrenos"],
#        "suspension": request.form["suspension"],
#        "liquidos": request.form["liquidos"],
#        "luces": request.form["luces"],
#        "id_proceso": request.form['id_proceso']
#    }
#    print(data)
#    Auto.update(data)
#    return redirect('/dashboard')