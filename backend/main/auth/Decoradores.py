from .. import jwt 
from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from functools import wraps

def administrador_requerido(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        if claims['role'] == "admin":
            return fn(*args, **kwargs)
        else:
            return 'Únicamente el administrador tiene acceso', 403
    return wrapper

@jwt.user_identity_loader

def busqueda_identidad_de_usuario():
    