#!/usr/bin/env python3
"""Defines the User class"""
from models.base import Base, BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Represents a User
    """
    __tablename__ = 'users'

    firstname = Column(String(30), nullable=False)
    lastname = Column(String(30), nullable=False)
    email = Column(String(60), unique=True, nullable=False)
    phone_number = Column(String(14), unique=True, nullable=False)
    username = Column(String(30), unique=True, nullable=False)
    hashed_password = Column(String(120), nullable=False)

    orders = relationship("Order", backref="user")

    def __init__(self, *args, **kwargs):
        """ Initialize the User instance """
        super().__init__(*args, **kwargs)
