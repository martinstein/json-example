from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import (
    DBSession,
    Base,
    )


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)

    # standard static route (not really needed for this example)
    config.add_static_view('static', 'static', cache_max_age=3600)

    # relevant routes for the blog post
    config.add_route('user_basic', '/user_basic')
    config.add_route('user_custom', '/user_custom')

    config.scan()
    return config.make_wsgi_app()
