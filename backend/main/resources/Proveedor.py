from flask_restful import Resource
from flask import request
from flask import request, jsonify
from .. import db
from main.models import UsuarioModel
from flask_jwt_extended import jwt_required, get_jwt_identity
from main.auth.Decoradores import admin_required
from main.auth.Decoradores import proveedor_or_admin_required

class Proveedor(Resource):
    
    @proveedor_or_admin_required
    def get(self, id):
        
        proveedor = db.session.query(UsuarioModel).get_or_404(id)
        return proveedor.to_json()
    
    @admin_required
    def delete(self, id):
        
        proveedor = db.session.query(UsuarioModel).get_or_404(id)
        db.session.delete(proveedor)
        db.session.commit()
        return '', 204
    
    @admin_required
    def put(self, id):

        proveedor = db.session.query(UsuarioModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(proveedor, key, value)
        db.session.add(proveedor)
        db.session.commit()
        return proveedor.to_json(), 201


class Proveedores(Resource):
    
    @jwt_required()
    def get(self):

        proveedores = db.session.query(UsuarioModel).filter(UsuarioModel.rol == 'proveedor')
        return jsonify([proveedor.to_json() for proveedor in proveedores])
    
    @admin_required
    def post(self): 

        proveedor = UsuarioModel.from_json(request.get_json())
        db.session.add(proveedor)
        db.session.commit()
        return proveedor.to_json(), 201

