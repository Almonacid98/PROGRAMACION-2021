from .. import db
from .. import mailsender
from flask import current_app, render_template, Blueprint
from flask_mail import Message
from smtplib import SMTPException
from main.models import UsuarioModel, BolsonModel
from main.auth.Decoradores import admin_required

def send_mail(to, subject, template, **kwargs):

    msj = Message (subject, sender = current_app.config['FLASKY_MAIL_SENDER'], recipients = to)
    try:
        msj.body = render_template(template + '.txt', **kwargs)
        msj.html = render_template(template + '.html', **kwargs)
        result = mailsender.send(msj)
    except SMTPException as e:
        print(str(e))
        return "Entrega de correo/mail fallida"
    return True

email = Blueprint('email', __name__, url_prefix = '/email')

@email.route('/promocion', methods = ['POST'])

@admin_required
def promocion_semanal():
    user= db.session.query(UsuarioModel).filter(UsuarioModel.rol == 'cliente').all()
    bolsones = db.session.query(BolsonModel).filter(BolsonModel.aprobado == 1).all()
    try:
        for usuario in user:
            sent = send_mail([usuario.email], "Promocion semanal", 'Super ofertas', usuario = usuario, bolsones = [bolson.nombre for bolson in bolsones])
    except SMTPException as e:
        print(str(e))
        return "Entrega de correo/mail fallida"
    return 'Correo enviado a destino', 200   