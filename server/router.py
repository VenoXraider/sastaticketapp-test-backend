from api import api_blueprint

def routes(app):
    app.register_blueprint(api_blueprint, url_prefix='/api')
    return app
