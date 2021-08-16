from .. import sendemails
from flask import current_app, render_template
from flask_mail import Message
from smtplib import SMTPException

def send_mail(to, subject, template, **kwargs):

    msj = Message (subject, sender = current_app.config['FLASKY_MAIL_SENDER'], recipients = to)
    try:
        msj.body = render_template(template + '.txt', **kwargs)
        msj.html = render_template(template + '.html', **kwargs)
        result = sendemails.send(msj)
    except SMTPException as e:
        print(str(e))
        return "Entrega de correo/mail fallida"
    return True