#!/usr/bin/env python3
"""Defines the Shipment model
"""
from models.base import Base, BaseModel
from sqlalchemy import (
    Column, Integer, DateTime, Numeric,
    String, ForeignKey
)
from sqlalchemy.orm import relationship
from datetime import datetime


class Shipment(BaseModel, Base):
    """Represents an Order
    """
    __tablename__ = 'shipments'

    order_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    shipped_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    shipping_cost = Column(Numeric(12, 2), nullable=False, default=0.00)
    shipping_address = Column(String(300), nullable=False)
    status = Column(String(30), default='pending')

    def __init__(self, *args, **kwargs):
        """ Initializes the shipment instance """
        super().__init__(*args, **kwargs)
