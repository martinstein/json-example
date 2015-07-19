from sqlalchemy import (
    Column,
    Boolean,
    DateTime,
    Integer,
    Text,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension
from jsonexample.util.jsonhelpers import RenderSchema

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))


class Base(object):
    def __json__(self, request):
        json_exclude = getattr(self, '__json_exclude__', set())
        return {key: value for key, value in self.__dict__.items()
                # Do not serialize 'private' attributes
                # (SQLAlchemy-internal attributes are among those, too)
                if not key.startswith('_')
                and key not in json_exclude}

Base = declarative_base(cls=Base)


class User(Base):
    __tablename__ = 'users'
    __json_exclude__ = set(["created_at"])

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    super_hero = Column(Boolean)
    created_at = Column(DateTime)


class UserSchema(RenderSchema):

    class Meta:
        fields = ("id", "name", "super_hero", "created_at")
