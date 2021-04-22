from flask import render_template, request, redirect, url_for, flash, session
from src import app
from flask_mail import Mail, Message
from src.models.users import UsersModel
from hashlib import md5
from src.config.send import mail
import datetime


@app.route('/user/checkIn', methods=['GET','POST'])
def checkIn():
    if request.method == 'GET':
        return render_template('user/check_in.html')

    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    #print(name, email, password)


    password=md5(password.encode("utf-8")).hexdigest()
    
    
    try:
        usersModel = UsersModel()
        usersModel.save(name, email, password)

        with app.app_context():

            msg = Message(subject="Por verificar para poder accerder",sender="barrcam37@gmail.com", recipients=[email], html='<button><a href="http://localhost:5000/user/check/{}">Verificar</a></button>'.format(email))
          
            #msg.html='<button><a href="http://localhost:5000/user/check/{}">Verificar</a></button>'.format(email)
            mail.send(msg)

        flash('Registrado correctamente... Verifique su correo electronico para poder acceder','success')

        return redirect(url_for('login'))
        
    except:
        flash('Error...', 'danger') 
        usersModel = UsersModel()
        user = usersModel.consultCheckIn(email)
        if user is not None:
            flash('Ya existe un usuario registrado con ese correo', 'danger') 
        return redirect(request.url)
        
@app.route('/user/check/<email>')
def check(email):
    date= datetime.datetime.now()
    usersModel = UsersModel()
    usersModel.check(date, email)
    print(date)
    return render_template('user/login.html')

@app.route('/user/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('user/login.html')

    email = request.form.get('email')
    password = request.form.get('password')
    password=md5(password.encode("utf-8")).hexdigest()
   # print(email, password)
    usersModel = UsersModel()
    user = usersModel.consultlogin(email, password)

    #print(user)
    if user == None:
        flash('Usuario o contraseña incorrecta...','danger')
        return redirect(request.url)
    
    date = usersModel.checkDate(email)
    #print(date[0])
    if date[0] is None :
        flash('No se ha verificado el correo...','danger')
        return redirect(request.url)
    
    session['user'] = {'id': user[0], 'name': user[1]}
    print(session['user']['name'])
    
    flash('Ingreso correcto','success')
    return redirect(url_for('index'))

@app.route('/user/logout', methods=['GET','POST'])
def logout():
    session.pop('user', None)
    #del session['user']
    return redirect(url_for('index'))

