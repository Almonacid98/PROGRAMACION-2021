from .. import db
from . import ProductoModel
from . import BolsonModel

class ProductoBolson(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    productoid = db.Column(db.Integer, db.ForeignKey('producto.id'), nullable = False)
    bolsonid = db.Column(db.Integer, db.ForeignKey('bolson.id'), nullable = False)
    producto = db.relationship('Producto', back_populates = 'productos_bolsones', uselist = False, single_parent = True)
    bolson = db.relationship('Bolson', back_populates = 'productos_bolsones', uselist = False, single_parent = True)
    cantidad = db.Column(db.Float, nullable = False)
    def to_json(self):
        self.producto = db.session.query(ProductoModel).get_or_404(self.productoid)
        self.bolson = db.session.query(BolsonModel).get_or_404(self.bolsonid)
        productobolson_json = {
            'id' : self.id,
            'producto' : self.producto.to_json(),
            'bolson' : self.bolson.to_json()
        }
        return productobolson_json
    @staticmethod

    def from_json(productobolson_json):
        id = productobolson_json.get('id')
        productoid = productobolson_json.get('productoid')
        bolsonid = productobolson_json.get('bolsonid')
        return ProductoBolson(id = id,
                            productoid = productoid,
                            bolsonid = bolsonid,
                            )
