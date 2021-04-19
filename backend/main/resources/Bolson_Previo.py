from flask_restful import Resource
from .. import db
from main.models import BolsonModel

BOLSONES = {
    1: {'name' : 'Bolson D'},
    2: {'name' : 'Bolson E'}
    }


class BolsonPrevio(Resource):

    def get(self, id):
        bolsonprevio = db.session.query(BolsonModel).get_or_404(id)
        return bolsonprevio.to_json()

class BolsonesPrevios(Resource):

    def get(self):
        bolsonesprevios = db.session.query(BolsonModel).all()
        return jsonify([bolsonprevio.to_json() for bolsonprevio in bolsonesprevios])