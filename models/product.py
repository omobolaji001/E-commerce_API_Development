#!/usr/bin/env python3
"""Defines the Product model
"""
from models.base import Base, BaseModel
from sqlalchemy import Column, String, Numeric


class Product(BaseModel, Base):
    """Represents a Product
    """
    __tablename__ = 'products'

    name = Column(String(60), nullable=False)
    description = Column(String(60))
    price = Column(Numeric(precision=10, scale=2), nullable=False,
                   default=0.00)

    def __init__(self):
        """ Initializes the product instance """
        super().__init__(*args, **kwargs)
