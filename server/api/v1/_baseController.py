from flask import jsonify

class BaseController():

    def response(self, data, message):
        d = {'data': data if data else '', 'message': message if message else ''}
        return jsonify(d)