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
@auth.route("/changepassword", methods=['PUT'])

def change_password(request):
    if request.method == 'PUT':
        form = Password(request.usuario, request.POST)
        if form.is_valid():
            usuario = form.save()
            update_session_auth_hash(request, usuario)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.usuario)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })
"""
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
            sent = send_mail([usuario.email], "Bienvenido", 'registrarse', usuario = usuario)
        except Exception as error:
            db.session.rollback()
            return str(error), 409
        return usuario.to_json() , 201

