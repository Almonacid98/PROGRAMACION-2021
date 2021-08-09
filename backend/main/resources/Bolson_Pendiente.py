from flask_restful import Resource
from flask import request
from flask import request, jsonify
from .. import db
from main.models import BolsonModel
from datetime import datetime
from flask_jwt_extended import jwt_required, get_jwt_identity
from main.auth.Decoradores import admin_required

class BolsonPendiente(Resource):
    
    @jwt_required()
    def get(self, id):
        
        bolsonpendiente = db.session.query(BolsonModel).get_or_404(id)
        return bolsonpendiente.to_json()
    
    @admin_required()
    def delete(self, id):
        
        bolsonpendiente = db.session.query(BolsonModel).get_or_404(id)
        db.session.delete(bolsonpendiente)
        db.session.commit()
        return '', 204
    
    jwt_required()
    def put(self, id):
        
        bolsonpendiente = db.session.query(BolsonModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            if key == 'fecha':
                setattr(bolsonpendiente, key, datetime.strptime(value, '%Y/%m/%d %H:%M:%S'))
            else:
                setattr(bolsonpendiente, key, value)
        db.session.add(bolsonpendiente)
        db.session.commit()
        return bolsonpendiente.to_json(), 201


class BolsonesPendientes(Resource):
    
    @jwt_required()
    def get(self):

        page = 1
        per_page = 10
        bolsonespendientes = db.session.query(BolsonModel)
        if request.get_json():
            filters = request.get_json().items()
            for key, value in filters:
                if key == 'page':
                    page = int(value)
                if key == 'per_page':
                    per_page = int(value)
        bolsonespendientes = bolsonespendientes.paginate(page, per_page, True, 30) 

        return jsonify({'bolsonespendientes': [bolsonpendiente.to_json() for bolsonpendiente in bolsonespendientes.items],
        'total': bolsonespendientes.total,
        'pages': bolsonespendientes.pages,
        'page': page
        })
    
    def post(self):
            
        bolsonpendiente = BolsonModel.from_json(request.get_json())
        db.session.add(bolsonpendiente)
        db.session.commit()
        return bolsonpendiente.to_json(), 201