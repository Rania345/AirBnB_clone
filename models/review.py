#!/usr/bin/python3
"""review class for project"""
from models.base_model import BaseModel

class review(BaseModel):
    """describes a review.
    Attributes:
    place_id,
    user_id,
    text.
    """

    place_id = ""
    user_id = ""
    text = ""
