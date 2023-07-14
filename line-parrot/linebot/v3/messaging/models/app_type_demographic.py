# coding: utf-8

"""
    LINE Messaging API

    This document describes LINE Messaging API.  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class AppTypeDemographic(str, Enum):
    """
    AppTypeDemographic
    """

    """
    allowed enum values
    """
    IOS = 'ios'
    ANDROID = 'android'

    @classmethod
    def from_json(cls, json_str: str) -> AppTypeDemographic:
        """Create an instance of AppTypeDemographic from a JSON string"""
        return AppTypeDemographic(json.loads(json_str))


