from flask_restful import Resource
from flask import request

BOLSONES = {
    1: {'name' : 'Bolson A'},
    2: {'name' : 'Bolson B'},
    3: {'name' : 'Bolson C'},
    4: {'name' : 'Bolson D'},
    5: {'name' : 'Bolson E'},
    6: {'name' : 'Bolson F'}
    }


class BolsonVenta():

    def get(self, id):
        if int(id) in BOLSONES:
            return BOLSONES[int(id)]
        return '', 404


class BolsonesVenta():

    def get(self):
        return BOLSONES