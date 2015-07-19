import datetime

from pyramid.view import view_config

from jsonexample.models import (
    DBSession,
    User,
    )


@view_config(route_name='basic', renderer='json')
def get_user_basic(request):
    return {
        "id": 1,
        "name": "Bruce Wayne",
        "super_hero": True,
        "friend_ids": [2, 3, 5, 8]
    }


@view_config(route_name='custom', renderer='json')
def get_user_custom(request):
    return {
        "id": 1,
        "name": "Bruce Wayne",
        "super_hero": True,
        "friend_ids": [2, 3, 5, 8],
        "created_at": datetime.datetime(2015, 1, 23, 16, 2, 15)
    }


@view_config(route_name='sqlalchemy_simple', renderer='json')
def get_user_sqlalchemy_simple(request):
    user = DBSession.query(User).filter_by(name="Bruce Wayne").one()
    return user
