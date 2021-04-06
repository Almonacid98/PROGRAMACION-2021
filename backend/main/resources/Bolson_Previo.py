from flask_restful import Resource
from flask import request




class BolsonPrevio():

    def get(self, id):
        if int(id) in BOLSONES:
            return BOLSONES[int(id)]
        return '', 404


class BolsonesPrevios():

    def get(self):
        return BOLSONES