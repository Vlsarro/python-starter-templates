from config import app_settings
from flask import Flask, render_template, request, flash, Blueprint
from flask_log import Logging
from flask_uploads import configure_uploads, UploadSet, IMAGES
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired


photos = UploadSet('photos', IMAGES)


class UploadForm(FlaskForm):
    photo = FileField('photo', validators=[
        FileRequired(),
        FileAllowed(photos, 'Images only!')
    ])


bp = Blueprint('bp', __name__, template_folder=app_settings.templates_path, static_folder=app_settings.static_path)


@bp.route('/', methods=['GET', 'POST'])
def index():
    form = UploadForm()

    if form.validate_on_submit():
        photos.save(request.files['photo'])
        flash("Photo saved successfully.")

    return render_template('index.html', form=form)


def create_app() -> Flask:
    app = Flask(
        __name__,
        static_url_path='',
        static_folder=app_settings.static_path,
        template_folder=app_settings.templates_path
    )
    Logging(app)

    app.config['UPLOADED_PHOTOS_DEST'] = app_settings.upload_path
    app.config['DEBUG'] = app_settings.debug
    app.config['SERVER_NAME'] = f'{app_settings.site_host}:{app_settings.port}'
    app.secret_key = app_settings.secret_key

    configure_uploads(app, photos)

    app.register_blueprint(bp)

    return app


if __name__ == '__main__':
    fapp = create_app()
    if app_settings.use_ssl:
        fapp.run(ssl_context=(f'{app_settings.root_path}/localhost.crt', f'{app_settings.root_path}/localhost.key'))
    else:
        fapp.run()
