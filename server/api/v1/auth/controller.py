from .._baseController import BaseController
from .service import AuthService

base_instance = BaseController()
service_instance = AuthService()

class AuthController():

    def login(self, payload):
        try:
            response = service_instance.login(payload)
            return base_instance.response(response, 'Logged in Successfully')
        except Exception as err:
            return err