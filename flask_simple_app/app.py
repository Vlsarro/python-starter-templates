from config import app_settings
from flask import Flask, render_template, request, flash
from flask_log import Logging
from flask_uploads import configure_uploads, UploadSet, IMAGES
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired


photos = UploadSet('photos', IMAGES)

app = Flask(
    __name__,
    static_url_path='',
    static_folder=app_settings.static_path,
    template_folder=app_settings.templates_path
)
flask_log = Logging(app)

app.config['UPLOADED_PHOTOS_DEST'] = app_settings.upload_path
app.secret_key = app_settings.secret_key

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
        'debug': app_settings.debug,
        'threaded': True,
        'host': app_settings.site_host,
        'port': app_settings.port
    }
    if app_settings.use_ssl:
        if app_settings.use_ssl_cert:
            app_params['ssl_context'] = (f'{app_settings.root_path}/cert.pem', f'{app_settings.root_path}/key.pem')
        else:
            app_params['ssl_context'] = 'adhoc'
    app.run(**app_params)
