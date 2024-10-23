#!/usr/bin/env python3
"""Defines the Order model
"""
from models.base import Base
from sqlalchemy import (
    Column, Integer, DateTime, Numeric,
    String, ForeignKey
)
from sqlalchemy.orm import relationship
from datetime import datetime


class Order(Base):
    """Represents an Order
    """
    __tablename__ = 'orders'

    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    order_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    total_amount = Column(Numeric(12, 2), nullable=False, default=0.00)
    shipping_address = Column(String(300), nullable=False)
    status = Column(String(30), default='pending')

    items = relationship("OrderItem", backref="order",
                         cascade="all, delete-orphan")
    shipment = relationship("Shipment", backref="order",
                            cascade="all, delete-orphan")

    def __init__(self, *args, **kwargs):
        """ Initializes the order instance """
        super().__init__(*args, **kwargs)
