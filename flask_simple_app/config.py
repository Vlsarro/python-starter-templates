import os
from pydantic import BaseSettings, Field


__all__ = ('app_settings',)


class Settings(BaseSettings):
    root_path: str = os.path.dirname(__file__)
    templates_path: str = os.path.join(root_path, 'templates')
    static_path: str = os.path.join(root_path, 'static')
    upload_path: str = os.path.join(root_path, 'uploads')

    site_host: str = Field(default='0.0.0.0', env='flask_site_host')
    port: int = Field(default=5000, env='flask_site_port')
    debug: bool = Field(default=False, env='flask_debug')
    encoding: str = Field(default='utf-8', env='flask_encoding')
    use_ssl: bool = Field(default=False, env='flask_use_ssl')

    # Local certificate generation
    # openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
    use_ssl_cert: bool = Field(default=False, env='flask_use_ssl_cert')

    # FIXME: https://pydantic-docs.helpmanual.io/usage/settings/#use-case-docker-secrets
    secret_key: bytes = Field(default=b'default_key', env='flask_secret_key')

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


app_settings = Settings()
