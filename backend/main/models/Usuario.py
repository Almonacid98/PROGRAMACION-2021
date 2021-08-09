from enum import unique
from operator import index
from .. import db
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100), nullable = False)
    apellido = db.Column(db.String(100), nullable = False)
    telefono = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(64), unique = True, index = True, nullable = False)
    contraseña = db.Column(db.String(128), nullable = False)
    rol = db.Column(db.String(10), nullable = False, default = 'user')
    compras = db.relationship('Compra', back_populate = 'usuarios', cascade = 'all, delete-orphan')
    productos = db.relationship('Producto', back_populates = 'usuarios')

