from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import BolsonModel
import datetime as dt
from flask_jwt_extended import jwt_required, get_jwt_identity
from main.auth.Decoradores import admin_required

class BolsonPrevio(Resource):

    @admin_required
    def get(self, id):

        bolsonprevio = db.session.query(BolsonModel).get_or_404(id)
        if bolsonprevio.fecha <= BolsonesPrevios.date:
            return jsonify(bolsonprevio.to_json())
        else:
            return '', 404

class BolsonesPrevios(Resource):

    date = dt.datetime.today() - dt.timedelta(days=7)
    @admin_required
    def get(self):

        page = 1
        per_page = 10
        bolsones = db.session.query(BolsonModel).filter(BolsonModel.fecha <= self.date)
        if request.get_json():
            filters = request.get_json().items()
            for key, value in filters:
                if key == 'page':
                    page = int(value)
                if key == 'per_page':
                    per_page = int(value)

        bolsones = bolsones.paginate(page, per_page, True, 30)
        return jsonify({'bolsones': [bolson.to_json() for bolson in bolsones.items],
            'total': bolsones.total,
            'pages': bolsones.pages,
            'page': page
        })
