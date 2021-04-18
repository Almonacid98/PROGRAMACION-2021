from .. import db

class Cliente(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100), nullable = False)
    apellido = db.Column(db.String(100), nullable = False)
    telefono = db.Column(db.String(100), nullable = False)
    mail = db.Column(db.String(100), nullable = False)

    def __repr__(self):
        return '<Cliente: %r %r %r %r >' % (self.nombre, self.apellido, self.telefono, self.mail)
    
    def to_json(self):
        cliente_json = {
            'id' : self.id,
            'nombre' : str(self.nombre),
            'apellido' : str(self.apellido),
            'telefono' : str(self.telefono),
            'mail' : str(self.mail),

        }
        return cliente_json
    @staticmethod

    def from_json(cliente_json):
        id = cliente_json.get('id')
        nombre = cliente_json.get('nombre')
        apellido = cliente_json.get('apellido')
        telefono = cliente_json.get('telefono')
        mail = cliente_json.get('mail')
        return Cliente(id = id,
                        nombre = nombre,
                        apellido = apellido,
                        telefono = telefono, 
                        mail = mail,
                        )