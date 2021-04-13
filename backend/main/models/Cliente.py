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
            
        }