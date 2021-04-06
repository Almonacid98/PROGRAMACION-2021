from flask_restful import Resource
from flask import request

#Pr�ximo diccionario
BOLSONES = {
    1: {'name' : 'Juan', 'lastname' : 'Santiago'},
    2: {'name' : 'Alvaro', 'lastname' : 'Perez'}
    }



#Recursos de Bols�n"
class Bolson(Resource):

    def get(self, id):

        if int(id) in BOLSONES:
            return BOLSONES[int(id)]
        return '', 404


class Bolsones(Resource):

    def get(self):
        return BOLSONES