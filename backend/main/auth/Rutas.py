from backend.main.mail.Funciones import send_mail
from flask import request, jsonify, Blueprint
from .. import db
from main.models import UsuarioModel
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from main.mail.Funciones import send_mail

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/login', methods=['POST'])
def login():
    usuario= db.session.query(UsuarioModel).filter(UsuarioModel.email == request.get_json().get("email")).first_or_404()
    if usuario.validate_pass(request.get_json().get("password")):
        access_token = create_access_token(identity=usuario)
        data = {
            'id': str(usuario.id),
            'email': usuario.email,
            'access_token': access_token
        }

        return data, 200
    else:
        return 'Contraseña incorrecta', 401

"""""
@auth.route("/cambiarpassword", methods=['GET', 'POST'])
def changed_password():
        password = db.session.query(UsuarioModel)
    if request.methods == 'GET':
    

    if request.methods == 'POST':
        
        nuevo_password = request.form['newpassword']
        confirmacion_password = request.form['passwordconfirmed']
        if (nuevo_password == confirmacion_password):
            return redirect(url_for('index'))
        else:
            return 'La contraseña no son iguales', 401
   """""         
@auth.route('/register', methods=['POST'])

def register():
    usuario = UsuarioModel.from_json(request.get_json())
    exists = db.session.query(UsuarioModel).filter(UsuarioModel.email == usuario.email).scalar() is not None
    if exists:
        return 'Email duplicado', 409
    else:
        try:
            db.session.add(usuario)
            db.session.commit()
            sent = send_mail([usuario.email], "Bienvenido", "register", usuario = usuario)
        except Exception as error:
            db.session.rollback()
            return str(error), 409
        return usuario.to_json() , 201

