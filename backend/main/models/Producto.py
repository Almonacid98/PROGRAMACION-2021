from .. import db


class Producto(db.Model):
    
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100), nullable = False)
    usuarioid = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable = False)
    usuario = db.relationship('Usuario', back_populates = 'productos', uselist = False, single_parent = True)
    productos_bolsones = db.relationship('ProductoBolson', back_populates = 'producto')

    def __repr__(self):
        return '<Producto: %r >' % (self.nombre)

    def to_json(self):
        self.proveedor = db.session.query(ProveedorModel).get_or_404(self.proveedorid)
        producto_json = {
            'id' : self.id,
            'nombre' : str(self.nombre),
            'usuario' : self.usuario.nombre
        }
        return producto_json
    @staticmethod

    def from_json(producto_json):
        id = producto_json.get('id')
        nombre = producto_json.get('nombre')
        usuarioid = producto_json.get('usuarioid')
        return Producto(id = id,
                        nombre = nombre,
                        usuarioid = usuarioid, 
                        )