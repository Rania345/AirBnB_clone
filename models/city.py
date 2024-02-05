#!/usr/bin/python3
"""city class for project"""
from models.base_model import BaseModel


class City(BaseModel):
    """describes a city.
    Attributes:
        state_id,
        name.
    """

    state_id = ""
    name = ""
