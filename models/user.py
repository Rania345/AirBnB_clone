#!/usr/bin/python3
"""user class for project"""
from models.base_model import BaseModel

class user(BaseModel):
    """describes a user.
    Attributes:
    email,
    password,
    first_name,
    last_name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
