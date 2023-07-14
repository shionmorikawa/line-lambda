# coding: utf-8

"""
    LINE Messaging API

    This document describes LINE Messaging API.  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr, constr

class CreateClickBasedAudienceGroupRequest(BaseModel):
    """
    Create audience for click-based retargeting
    https://developers.line.biz/en/reference/messaging-api/#create-click-audience-group
    """
    description: Optional[constr(strict=True, max_length=120)] = Field(None, description="The audience's name. This is case-insensitive, meaning AUDIENCE and audience are considered identical. Max character limit: 120 ")
    request_id: Optional[StrictStr] = Field(None, alias="requestId", description="The request ID of a broadcast or narrowcast message sent in the past 60 days. Each Messaging API request has a request ID. ")
    click_url: Optional[constr(strict=True, max_length=2000)] = Field(None, alias="clickUrl", description="The URL clicked by the user. If empty, users who clicked any URL in the message are added to the list of recipients. Max character limit: 2,000 ")

    __properties = ["description", "requestId", "clickUrl"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> CreateClickBasedAudienceGroupRequest:
        """Create an instance of CreateClickBasedAudienceGroupRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateClickBasedAudienceGroupRequest:
        """Create an instance of CreateClickBasedAudienceGroupRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateClickBasedAudienceGroupRequest.parse_obj(obj)

        _obj = CreateClickBasedAudienceGroupRequest.parse_obj({
            "description": obj.get("description"),
            "request_id": obj.get("requestId"),
            "click_url": obj.get("clickUrl")
        })
        return _obj

