from sqlalchemy.orm import relationship, backref
from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy import Column, Integer, String,  ForeignKey
from .membership_tables import channel_membership

class Channel(db.Model):
    __tablename__ = 'channels'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False)
    serverId = Column(Integer, ForeignKey(add_prefix_for_prod('servers.id')), nullable=False)
    creatorId = Column(Integer, ForeignKey(add_prefix_for_prod('users.id')), nullable=False)

    users = db.relationship(
        "User",
        secondary = channel_membership,
        back_populates = "channels"
    )


    server = relationship('Server', backref=backref('channels', lazy=True))
    creator = relationship('User', backref=backref('created_channels', lazy=True))