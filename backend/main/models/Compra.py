from .. import db
import datetime as dt
from .Bolson import Bolson as BolsonModel

class Compra(db.Model):
    
    id = db.Column(db.Integer, primary_key = True)
    fecha_hora_compra = db.Column(db.DateTime, nullable = False)
    retirado = db.Column(db.Boolean, nullable = False)
    bolsonid = db.Column(db.Integer, db.ForeignKey('bolson.id'), nullable = False)
    usuarioid = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable = False)
    bolson = db.relationship('Bolson', back_populates = 'compras', uselist = False, single_parent = True)
    usuarios = db.relationship('Usuario', back_populates = 'compras', uselist = False, single_parent = True)

    def __repr__(self):
        return '<Compra: %r %r %r %r >' % (self.fecha_hora_compra, self.retirado, self.cliente.to_json(), self.bolson.to_json())
    def to_json(self):
        self.bolson = db.session.query(BolsonModel).get_or_404(self.bolsonid)
        compra_json = {
            'id' : self.id,
            'fecha_hora_compra' : self.fecha_hora_compra.isoformat(),
            'retirado' : self.retirado,
            'bolson' : self.bolson.to_json(),
            'usuario' : self.usuarios.to_json(),

        }
        return compra_json
    @staticmethod

    def from_json(compra_json):
        id = compra_json.get('id')
        fecha_hora_compra = dt.datetime.strptime(compra_json.get('fecha_hora_compra'), '%Y/%m/%d %H:%M:%S')
        retirado = compra_json.get('retirado')
        bolsonid = compra_json.get('bolsonid')
        usuarioid = compra_json.get('usuarioid')
        return Compra(id = id,
                    fecha_hora_compra = fecha_hora_compra,
                    retirado = retirado,
                    bolsonid = bolsonid,
                    usuarioid = usuarioid,
                    )