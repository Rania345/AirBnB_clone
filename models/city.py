#!/usr/bin/python3
"""city class for project"""
from models.base_model import BaseModel

class city(BaseModel):
    """describes a city.
    Attributes:
        state_id,
        name.
    """

    state_id = ""
    name = ""
