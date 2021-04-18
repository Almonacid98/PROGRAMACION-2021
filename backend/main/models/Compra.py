from .. import db

class Compra(db.Model):
    
    id = db.Column(db.Integer, primary_key = True)
    fecha_hora_compra = db.Column(db.DateTime, nullable = False)
    retirado = db.Column(db.Boolean, nullable = False)

    def __repr__(self):
        return '<Compra: %r %r >' % (self.fecha_hora_compra, self.retirado)

    def to_json(self):
        compra_json = {
            'id' : self.id,
            'fecha_hora_compra' : self.fecha_hora_compra.isoformat(),
            'retirado' : self.retirado,

        }
        return compra_json
    @staticmethod

    def from_json(compra_json):
        id = compra_json.get('id')
        fecha_hora_compra = compra_json.get('fecha_hora_compra')
        retirado = compra_json.get('retirado')
        return Compra(id = id,
                    fecha_hora_compra = fecha_hora_compra,
                    retirado = retirado,
                    )