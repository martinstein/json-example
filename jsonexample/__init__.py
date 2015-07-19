from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import (
    DBSession,
    Base,
    )
from .util.jsonhelpers import custom_json_renderer
from .util.jsonhelpers2 import custom_json_renderer2


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.add_renderer('json', custom_json_renderer())
    config.add_renderer('json2', custom_json_renderer2())

    # standard static route (not really needed for this example)
    config.add_static_view('static', 'static', cache_max_age=3600)

    # relevant routes for the blog post
    config.add_route('basic', '/basic')
    config.add_route('custom', '/custom')
    config.add_route('sqlalchemy_simple', '/sqlalchemy_simple')
    config.add_route('sqlalchemy_marshmallow', '/sqlalchemy_marshmallow')
    config.add_route('marshmallow_integrated', '/marshmallow_integrated')

    config.scan()
    return config.make_wsgi_app()
