from flask import Flask
from app.utils import *


# Active endpoints noted as following:
# (url_prefix, blueprint_object)
#ACTIVE_ENDPOINTS = (("/", ping), ("/dummy", dummy))


def create_app():
    app = Flask(__name__)

    # accepts both /endpoint and /endpoint/ as valid URLs
    app.url_map.strict_slashes = False

    # register each active blueprint
    #for url, blueprint in ACTIVE_ENDPOINTS:
    #    app.register_blueprint(blueprint, url_prefix=url)

    return app
