from flask_restful import Resource
from flask import request 






class BolsonPendiente():

    def get(self, id):
        if int(id) in BOLSONES:
            return BOLSONES[int(id)]
        return '', 404


    def delete(self, id):
        if int(id) in BOLSONES:
            del BOLSONES[int(id)]
            return '', 204
        return '', 404

    def put(self, id):
        if int(id) in BOLSONES:
            bolson = BOLSONES[int(id)]
            data = request.get_json()
            bolson.update(data)
            return bolson, 201
        return '', 404

class BolsonesPendientes():

    def get(self):
        return BOLSONES

    def post(self):
        bolson = request.get_json()
        id = int(max(BOLSONES.keys())) + 1
        BOLSONES[id] = bolson
        return BOLSONES[id], 201