from flask_restful import Resource
from flask import request





class BolsonVenta():

    def get(self, id):
        if int(id) in BOLSONES:
            return BOLSONES[int(id)]
        return '', 404


class BolsonesVenta():

    def get(self):
        return BOLSONES