from flask_restful import Resource
from flask import request
from flask import request, jsonify
from .. import db
from main.models import CompraModel
from datetime import datetime
from flask_jwt_extended import jwt_required, get_jwt_identity

class Compra(Resource):

    @jwt_required(optional=True)
    def get(self, id):
        
        compra = db.session.query(CompraModel).get_or_404(id)
        return compra.to_json()
    
    @jwt_required()
    def delete(self, id):
        
        compra = db.session.query(CompraModel).get_or_404(id)
        db.session.delete(compra)
        db.session.commit()
        return '', 204
    
    @jwt_required()
    def put(self, id):

        compra = db.session.query(CompraModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            if key == 'fecha_hora_compra':
                setattr(compra, key, datetime.strptime(value, '%Y/%m/%d %H:%M:%S'))
            else:
                setattr(compra, key, value)
        db.session.add(compra)
        db.session.commit()
        return compra.to_json(), 201

class Compras(Resource):
    
    def get(self):
        
        page = 1
        per_page = 10
        compras = db.session.query(CompraModel)
        if request.get_json():
            filters = request.get_json().items()
            for key, value in filters:
                if key =="page":
                    page = int(value)
                if key == "per_page":
                    per_page = int(value)
        compras = compras.paginate(page, per_page, True, 30)
        return jsonify({ 'compras': [compra.to_json() for compra in compras.items],
                  'total': compras.total,
                  'pages': compras.pages,
                  'page': page
                  })
    
    @jwt_required()
    def post(self): 

        compra = CompraModel.from_json(request.get_json())
        current_user = get_jwt_identity()
        compra.usuarioid = current_user
        try:
            db.session.add(compra)
            db.session.commit()
        except Exception as error:
            return 'El formato utilizado no es correcto', 400
        return compra.to_json(), 201

