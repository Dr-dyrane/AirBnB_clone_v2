#!/usr/bin/python3
"""Module that holds the Review class"""

import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """Representation of a Review"""

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'reviews'

        text = Column(
            String(1024),
            nullable=False
        )

        place_id = Column(
            String(60),
            ForeignKey('places.id'),
            nullable=False
        )

        user_id = Column(
            String(60),
            ForeignKey('users.id'),
            nullable=False
        )
    else:
        text = ""
        place_id = ""
        user_id = ""

    def __init__(self, *args, **kwargs):
        """Initializes Review"""
        super().__init__(*args, **kwargs)
