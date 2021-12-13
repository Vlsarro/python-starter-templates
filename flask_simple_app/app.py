import config
from flask import Flask, render_template, request, flash
from flask_log import Logging
from flask_uploads import configure_uploads, UploadSet, IMAGES
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired


photos = UploadSet('photos', IMAGES)

app = Flask(
    __name__,
    static_url_path='',
    static_folder=config.STATIC_PATH,
    template_folder=config.TEMPLATES_PATH
)
flask_log = Logging(app)

app.config['UPLOADED_PHOTOS_DEST'] = config.UPLOAD_PATH
app.secret_key = config.SECRET_KEY

configure_uploads(app, photos)


class UploadForm(FlaskForm):
    photo = FileField('photo', validators=[
        FileRequired(),
        FileAllowed(photos, 'Images only!')
    ])


@app.route('/', methods=['GET', 'POST'])
def index():
    form = UploadForm()

    if form.validate_on_submit():
        photos.save(request.files['photo'])
        flash("Photo saved successfully.")

    return render_template('index.html', form=form)


if __name__ == '__main__':
    app_params = {
        'debug': config.DEBUG,
        'threaded': True,
        'host': config.SITE_HOST,
        'port': config.PORT
    }
    if config.USE_SSL:
        if config.USE_SSL_CERT:
            app_params['ssl_context'] = (f'{config.ROOT_PATH}/cert.pem', f'{config.ROOT_PATH}/key.pem')
        else:
            app_params['ssl_context'] = 'adhoc'
    app.run(**app_params)
