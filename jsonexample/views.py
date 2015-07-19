from pyramid.view import view_config


@view_config(route_name='user_basic', renderer='json')
def get_user_basic(request):
    return {
        "id": 1,
        "name": "Bruce Wayne",
        "super_hero": True,
        "friend_ids": [2, 3, 5, 8]
    }
