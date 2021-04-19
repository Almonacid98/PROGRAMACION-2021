from flask_restful import Resource
from .. import db
from main.models import BolsonModel

#Pr�ximo diccionario
BOLSONES = {
    1: {'name' : 'Bolson A'},
    2: {'name' : 'Bolson B'},
    3: {'name' : 'Bolson C'}
    }



#Recursos de Bols�n"
class BolsonVenta(Resource):

    def get(self, id):
        bolsonventa = db.session.query(BolsonModel).get_or_404(id)
        return bolsonventa.to_json()

class BolsonesVenta(Resource):

    def get(self):
        bolsonesventa = db.session.query(BolsonModel).all()
        return jsonify([bolsonventa.to_json() for bolsonventa in bolsonesventa])