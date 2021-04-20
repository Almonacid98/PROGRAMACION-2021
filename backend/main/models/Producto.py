from .. import db
from main.models import ProveedorModel
class Producto(db.Model):
    
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100), nullable = False)
    proveedorid = db.Column(db.Integer, db.ForeignKey('proveedor.id'), nullable = False)
    proveedor = db.relationship('Proveedor', back_populates = 'productos', uselist = False, single_parent = True)
    productos_bolsones = db.relationship('ProductoBolson', back_populates = 'producto')

    def __repr__(self):
        return '<Producto: %r >' % (self.nombre)

    def to_json(self):
        self.proveedor = db.session.query(ProveedorModel).get_or_404(self.proveedorid)
        producto_json = {
            'id' : self.id,
            'nombre' : str(self.nombre),
            'proveedor' : self.proveedor.to_json(),
        }
        return producto_json
    @staticmethod

    def from_json(producto_json):
        id = producto_json.get('id')
        nombre = producto_json.get('nombre')
        proveedorid = producto_json.get('proveedorid')
        return Producto(id = id,
                        nombre = nombre,
                        proveedorid = proveedorid, 
                        )