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





class AudienceGroupCreateRoute(str, Enum):
    """
    How the audience was created. One of:  - `OA_MANAGER`: Audience created with [LINE Official Account Manager](https://manager.line.biz/). - `MESSAGING_API`: Audience created with Messaging API. - `POINT_AD`: Audience created with [LINE Points Ads](https://www.linebiz.com/jp/service/line-point-ad/) (Japanese only). - `AD_MANAGER`: Audience created with [LINE Ads](https://admanager.line.biz/). 
    """

    """
    allowed enum values
    """
    OA_MANAGER = 'OA_MANAGER'
    MESSAGING_API = 'MESSAGING_API'
    POINT_AD = 'POINT_AD'
    AD_MANAGER = 'AD_MANAGER'

    @classmethod
    def from_json(cls, json_str: str) -> AudienceGroupCreateRoute:
        """Create an instance of AudienceGroupCreateRoute from a JSON string"""
        return AudienceGroupCreateRoute(json.loads(json_str))


