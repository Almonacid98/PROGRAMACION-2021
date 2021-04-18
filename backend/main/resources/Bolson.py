from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import BolsonModel

#Pr�ximo diccionario
BOLSONES = {
    1: {'name' : 'Bolson A'},
    2: {'name' : 'Bolson B'},
    3: {'name' : 'Bolson C'},
    4: {'name' : 'Bolson D'},
    5: {'name' : 'Bolson E'},
    6: {'name' : 'Bolson F'}
    }



#Recursos de Bols�n"
class Bolson(Resource):

    def get(self, id):
        bolson = db.session.query(BolsonModel).get_or_404(id)
        return bolson.to_json()


class Bolsones(Resource):

    def get(self):
        bolsones = db.session.query(BolsonModel).all()
        return jsonify([bolson.to_json() for bolson in bolsones])