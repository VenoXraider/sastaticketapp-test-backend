import common.env
from common.server import Server
from router import routes
import os

def startApp():
   Server().router(routes).listen(os.environ.get('PORT'))

if __name__ == '__main__':
   startApp()