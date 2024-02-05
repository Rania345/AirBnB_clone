#!/usr/bin/python3
""" the city class """
from models.base_model import BaseModel

class city(BaseModel):
    """ describes a city, contains: state_id and name """

    state_id = ""
    name = ""
