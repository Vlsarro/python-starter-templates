import config
from flask import Flask, render_template
from flask_log import Logging


app = Flask(
    __name__,
    static_url_path='',
    static_folder=config.STATIC_PATH,
    template_folder=config.TEMPLATES_PATH
)
flask_log = Logging(app)

app.secret_key = config.SECRET_KEY


@app.route('/', methods=['GET'])
def index():
    app.logger.debug('Testing a debug message')
    return render_template('index.html')


if __name__ == '__main__':
    app_params = {
        'debug': config.DEBUG,
        'threaded': True,
        'host': config.SITE_HOST,
        'port': config.PORT
    }
    if config.USE_SSL_CERT:
        app_params['ssl_context'] = (f'{config.ROOT_PATH}/cert.pem', f'{config.ROOT_PATH}/key.pem')
    else:
        app_params['ssl_context'] = 'adhoc'
    app.run(**app_params)
