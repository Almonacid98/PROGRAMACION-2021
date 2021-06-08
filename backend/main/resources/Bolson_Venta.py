from flask_restful import Resource
from flask import request, jsonify
from .. import db
from .Bolson import Bolson as BolsonModel


class BolsonVenta(Resource):

    def get(self, id):

        bolsonventa = db.session.query(BolsonModel).get_or_404(id)
        return bolsonventa.to_json()

class BolsonesVenta(Resource):

    def get(self):
        
        bolsonesventa = db.session.query(BolsonModel).all()
        return jsonify([bolsonventa.to_json() for bolsonventa in bolsonesventa])