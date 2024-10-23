#!/usr/bin/env python3
"""Defines Order item model
"""
from models.base import Base
from sqlalchemy import Column, Integer, Numeric, ForeignKey, DateTime
from datetime import datetime


class OrderItem(Base):
    """Represents an Order item
    """
    __tablename__ = 'order_items'

    order_id = Column(String(60), ForeignKey('orders.id'), nullable=False)
    product_id = Column(String(60), ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    price_per_item = Column(Numeric(precision=10, scale=2), nullable=False)


    def __init(self, *args, **kwargs):
        """ Initializes the instance """
        super().__init__(*args, **kwargs)
