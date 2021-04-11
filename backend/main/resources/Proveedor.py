from flask_restful import Resource
from flask import request

PROVEEDORES = {
    1: {'name' : 'Proveedor A'},
    2: {'name' : 'Proveedor B'},
    3: {'name' : 'Proveedor C'},
    4: {'name' : 'Proveedor D'},
    5: {'name' : 'Proveedor E'},
    6: {'name' : 'Proveedor F'}
}


class Proveedor(Resource):

    def get(self, id):
        
        if int(id) in PROVEEDORES:  
            return PROVEEDORES[int(id)]
        return '', 404
    
    def delete(self, id):
        
        if int(id) in PROVEEDORES:
            del PROVEEDORES[int(id)]
            return '', 204
        return '', 404
    
    def put(self, id):
        if int(id) in PROVEEDORES:
            proveedor = PROVEEDORES[int(id)]
            data = request.get_json()
            proveedor.update(data)
            return proveedor, 201
        return '', 404


class Proveedores(Resource):
    
    def get(self):
        return PROVEEDORES
    
    def post(self):    
        proveedor = request.get_json()
        id = int(max(PROVEEDORES.keys())) + 1
        PROVEEDORES[id] = proveedor
        return PROVEEDORES[id], 201

