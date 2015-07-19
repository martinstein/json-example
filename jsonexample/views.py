import datetime
import random

from pyramid.view import view_config

from jsonexample.models import (
    DBSession,
    User,
    UserSchema,
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


@view_config(route_name='sqlalchemy_marshmallow', renderer='json')
def get_user_sqlalchemy_marshmallow(request):
    user = DBSession.query(User).filter_by(name="Bruce Wayne").one()

    # Now we select the schema and which fields to be included/excluded
    # based on some runtime condition. Imagine a test if the currently
    # logged in user is admin or not.
    if random.randint(0, 1):
        user_schema = UserSchema()
    else:
        user_schema = UserSchema(exclude=("id", "created_at"))

    data, erros = user_schema.dump(user)
    return data
