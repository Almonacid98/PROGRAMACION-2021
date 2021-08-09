from collections import UserList
from .. import db
import datetime as dt
from .Cliente import Cliente as ClienteModel
from .Bolson import Bolson as BolsonModel

class Compra(db.Model):
    
    id = db.Column(db.Integer, primary_key = True)
    fecha_hora_compra = db.Column(db.DateTime, nullable = False)
    retirado = db.Column(db.Boolean, nullable = False)
    bolsonid = db.Column(db.Integer, db.ForeignKey('bolson.id'), nullable = False)
    bolson = db.relationship('Bolson', back_populates = 'compras', uselist = False, single_parent = True)
    usuarioid = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable = False)
    usuario = db.relationship('Usuario', back_populates = 'compras', Uselist = False, single_parent = True)

    def __repr__(self):
        return '<Compra: %r %r >' % (self.fecha_hora_compra, self.retirado)

    def to_json(self):
        self.cliente = db.session.query(ClienteModel).get_or_404(self.clienteid)
        self.bolson = db.session.query(BolsonModel).get_or_404(self.bolsonid)
        compra_json = {
            'id' : self.id,
            'fecha_hora_compra' : self.fecha_hora_compra.isoformat(),
            'retirado' : self.retirado,
            'cliente' : self.cliente.to_json(),
            'bolson' : self.bolson.to_json(),
            'usuario' : self.usuario.to_json(),

        }
        return compra_json
    @staticmethod

    def from_json(compra_json):
        id = compra_json.get('id')
        fecha_hora_compra = dt.datetime.strptime(compra_json.get('fecha_hora_compra'), '%Y/%m/%d %H:%M:%S')
        retirado = compra_json.get('retirado')
        clienteid = compra_json.get('clienteid')
        bolsonid = compra_json.get('bolsonid')
        usuarioid = compra_json.get('usuarioid')
        return Compra(id = id,
                    fecha_hora_compra = fecha_hora_compra,
                    retirado = retirado,
                    clienteid = clienteid,
                    bolsonid = bolsonid,
                    usuarioid = usuarioid,
                    )