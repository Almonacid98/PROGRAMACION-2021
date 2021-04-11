from flask_restful import Resource


#Pr�ximo diccionario
BOLSONES = {
    1: {'name' : 'Bolson A'},
    2: {'name' : 'Bolson B'},
    3: {'name' : 'Bolson C'}
    }



#Recursos de Bols�n"
class BolsonVenta(Resource):

    def get(self, id):
        if int(id) in BOLSONES:
            return BOLSONES[int(id)]
        return '', 404


class BolsonesVenta(Resource):

    def get(self):
        return BOLSONES