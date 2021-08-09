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
    compras = db.relationship('Compra', back_populates = 'usuarios', cascade = 'all, delete-orphan')
    productos = db.relationship('Producto', back_populates = 'usuarios')

    @property
    def plain_password(self):
        raise AttributeError('La contraseña no se puede leer')
    
    @plain_password.setter
    
    def plain_password(self, password):
        self.password = generate_password_hash(password)
    
    def validate_pass(self, password):
        return check_password_hash(self.password, password)
    
    def __repr__(self):
        return '<Usuario: %r %r %r %r >' % (self.nombre, self.apellido, self.telefono, self.email)
    
    def to_json(self):
        usuario_json = {
            'id' : self.id,
            'nombre' : str(self.nombre),
            'apellido' : str(self.apellido),
            'telefono' : str(self.telefono),
            'email' : str(self.email)

        }
        return usuario_json
    
    @staticmethod

    def from_json(usuario_json):
        id = usuario_json.get('id')
        nombre = usuario_json.get('nombre')
        apellido = usuario_json.get('apellido')
        telefono = usuario_json.get('telefono')
        email = usuario_json.get('email')
        contraseña = usuario_json.get('contraseña')
        rol = usuario_json.get('rol')
        return Usuario(id = id,
                    nombre = nombre,
                    apellido = apellido,
                    telefono = telefono,
                    email = email,
                    plain_password = contraseña,
                    rol = rol,
                    )
