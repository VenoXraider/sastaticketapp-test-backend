from flask import Flask, request, render_template
from flask_cors import CORS
from .logging import file_handler
import socket

class Server:

    def __init__(self):
        self.app = Flask(__name__)
        self.app.logger.addHandler(file_handler)
        CORS(self.app, origins="*")
        self.app.config['REQUEST_LIMIT'] = '100kb'
        self.app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 60 * 60 * 24 * 14
        self.app.config['SESSION_COOKIE_SECURE'] = True
        self.app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

    def router(self, routesFunc):
        self.routes = routesFunc
        return self        

    def listen(self, port):
        self.app = self.routes(self.app)
        self.app.logger.info(f"up and running in production @: {socket.gethostname()} on port: {port}")
        self.app.run(host='0.0.0.0', port=port)
        return self.app