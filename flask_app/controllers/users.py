from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.user import Usuario
from flask_app.models.auto import Auto
from flask_app.models.proceso import Proceso

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/indexadmin')
def indexadmin():
    return render_template('indexadmin.html')

@app.route('/register',methods=['POST'])
def register():
    if not Usuario.validate_register(request.form):
        return redirect('/')
    data ={ 
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "correo": request.form['correo'],
        "clave": bcrypt.generate_password_hash(request.form['clave'])
    }
    id = Usuario.save(data)
    session['users_id'] = id

    return redirect('/dashboard')

@app.route('/logina',methods=['POST'])
def logina():
    user = Usuario.get_by_email(request.form)

    if not user:
        flash("Invalid Email","login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.clave, request.form['clave']):
        flash("Invalid Password","login")
        return redirect('/')
    session['users_id'] = user.id_usuario
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'users_id' not in session:
        return redirect('/logout')
    data ={
        'id_usuario': session['users_id']
    }
    return render_template("dashboard.html",user=Usuario.get_by_id(data),clientes=Auto.get_all3())


@app.route('/login',methods=['POST'])
def login():
    user = Usuario.get_by_email2(request.form)

    if not user:
        flash("Invalid Email","login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.clave, request.form['clave']):
        flash("Clave o Correo Incorrect","login")
        return redirect('/')
    session['users_id'] = user.id_usuario
    return redirect('/dashboardcli')

@app.route('/dashboardcli')
def dashboardcli():
    if 'users_id' not in session:
        return redirect('/logout')
    data ={
        'id_usuario': session['users_id']
    }
    return render_template("dashboardcliente.html",user=Usuario.get_by_id(data),clientes=Auto.get_all4(data))


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/new/cliente')
def newcliente():
    return render_template('agregarcliente.html')

@app.route('/create/cliente',methods=['POST'])
def create_cliente():
    if 'users_id' not in session:
        return redirect('/logout')
    if not Usuario.validate_register(request.form):
        return redirect('/new/cliente')
    data = {
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "correo": request.form["correo"],
        "clave": bcrypt.generate_password_hash(request.form['clave'])
    }
    Usuario.save(data)
    return redirect('/dashboard')