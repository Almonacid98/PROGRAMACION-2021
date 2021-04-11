from flask_restful import Resource


BOLSONES = {
    1: {'name' : 'Bolson A'},
    2: {'name' : 'Bolson B'},
    3: {'name' : 'Bolson C'},
    4: {'name' : 'Bolson D'},
    5: {'name' : 'Bolson E'},
    6: {'name' : 'Bolson F'}
    }


class BolsonPrevio(Resource):

    def get(self, id):
        if int(id) in BOLSONES:
            return BOLSONES[int(id)]
        return '', 404


class BolsonesPrevios(Resource):

    def get(self):
        return BOLSONES