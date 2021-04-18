from flask_restful import Resource
from .. import db
from main.models import BolsonModel

BOLSONES = {
    1: {'name' : 'Bolson D'},
    2: {'name' : 'Bolson E'}
    }


class BolsonPrevio(Resource):

    def get(self, id):
        if int(id) in BOLSONES:
            return BOLSONES[int(id)]
        return '', 404


class BolsonesPrevios(Resource):

    def get(self):
        return BOLSONES