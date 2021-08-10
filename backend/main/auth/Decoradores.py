from .. import jwt 
from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from functools import wraps

def admin_required(fn): 
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        if claims['rol'] == "admin":
            return fn(*args, **kwargs)
        else:
            return 'Únicamente el administrador tiene acceso', 403
    return wrapper

def proveedor_or_admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        if claims['rol'] == 'proveedor' or claims['rol'] == 'admin':
            return fn(*args, **kwargs)
        else:
            return 'Pueden acceder libremente solo los administradores/proveedores', 403
    return wrapper

def proveedor_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        if claims['rol'] == 'proveedor':
            return fn(*args, **kwargs)
        else:
            return 'Pueden acceder libremente solo los proveedores', 403
    return wrapper

@jwt.user_identity_loader

def user_identity_lookup(usuario):
    return usuario.id

@jwt.additional_claims_loader
def add_claims_to_access_token(usuario):
    claims = {
        'rol' : usuario.rol,
        'id' : usuario.id,
        'email' : usuario.email
    }
    return claims
    
    