from flask_restful import Resource
from flask import request
from flask import request, jsonify
from .. import db
from main.models import ProductoModel
from flask_jwt_extended import jwt_required, get_jwt_identity

class Producto(Resource):

    @jwt_required(optional=True)
    def get(self, id):
        
        producto = db.session.query(ProductoModel).get_or_404(id)
        current_identity = get_jwt_identity()
        if current_identity:
            return producto.to_json()
        else:
            return producto.to_json_public()
    
    @jwt_required()
    def delete(self, id):
        
        producto = db.session.query(ProductoModel).get_or_404(id)
        db.session.delete(producto)
        db.session.commit()
        return '', 204
    
    @jwt_required()
    def put(self, id):

        producto = db.session.query(ProductoModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(producto, key, value)
        db.session.add(producto)
        db.session.commit()
        return producto.to_json(), 201


class Productos(Resource):
    
    def get(self):

        filters = request.data     
        productos = db.session.query(ProductoModel)
        if filters:
            for key, value in request.get_json().items():
                if key == "proveedorid":
                    productos = productos.filter(ProductoModel.proveedorid == value)
        productos = productos.all()
        return jsonify({'productos' : [producto.to_json() for producto in productos]})
    
    @jwt_required()
    def post(self):
        
        producto = ProductoModel.from_json(request.get_json())
        current_user = get_jwt_identity()
        producto.usuarioid = current_user
        try:
            db.session.add(producto)
            db.session.commit()
        except Exception as error:
            return 'El formato utilizado no es correcto', 400
        return producto.to_json(), 201
