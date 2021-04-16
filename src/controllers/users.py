from flask import render_template, request, redirect, url_for, flash
from src import app
from flask_mail import Mail, Message
from src.models.users import UsersModel
from hashlib import md5
from src.config.send import mail
app.secret_key ='CBZEkZPmgsPdrA3sVEb2PLu1p'

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

            msg = Message(subject="HOLA",sender="barrcam37@gmail.com", recipients=[email], body="Ya estas registrado")
            mail.send(msg)
        
        flash('Registrado correctamente...','success')

        return redirect(url_for('login'))
        
    except:
        flash('Error...', 'danger') 
        usersModel = UsersModel()
        user = usersModel.consultCheckIn(email)
        if user is not None:
            flash('Ya existe un usuario registrado con ese correo', 'danger') 
        return redirect(request.url)
        


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

    print(user)
    if user == None:
        flash('Usuario o contraseña incorrecta...','danger')
        return redirect(request.url)
    flash('Ingreso correcto','success')
    return redirect(url_for('index'))



