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


class BolsonPendiente(Resource):

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


class BolsonesPendientes(Resource):
    
    def get(self):
        return BOLSONES
    
    def post(self):    
        bolson = request.get_json()
        id = int(max(BOLSONES.keys())) + 1
        BOLSONES[id] = bolson
        return BOLSONES[id], 201