from .._baseController import BaseController
from .service import AuthService

base_instance = BaseController()
service_instance = AuthService()

class AuthController():

    def getSheetsRouter(self, payload):
        try:
            response = service_instance.getSheetsRouter(payload)
            return base_instance.response(response, 'Get Sheets Successfully')
        except Exception as err:
            return err

    def sendEmail(self, payload):
        try:
            response = service_instance.sendEmail(payload)
            return base_instance.response(response, 'Email Send Successfully')
        except Exception as err:
            return err