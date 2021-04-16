from flask_mail import Mail, Message
from src import app
from src.config.password import email, password

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": email,
    "MAIL_PASSWORD": password
}

app.config.update(mail_settings)
mail = Mail(app)
