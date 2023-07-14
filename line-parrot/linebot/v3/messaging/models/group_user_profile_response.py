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
from pydantic import BaseModel, Field, StrictStr

class GroupUserProfileResponse(BaseModel):
    """
    GroupUserProfileResponse
    https://developers.line.biz/en/reference/messaging-api/#get-group-member-profile
    """
    display_name: StrictStr = Field(..., alias="displayName", description="User's display name")
    user_id: StrictStr = Field(..., alias="userId", description="User ID")
    picture_url: Optional[StrictStr] = Field(None, alias="pictureUrl", description="Profile image URL. `https` image URL. Not included in the response if the user doesn't have a profile image.")

    __properties = ["displayName", "userId", "pictureUrl"]

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
    def from_json(cls, json_str: str) -> GroupUserProfileResponse:
        """Create an instance of GroupUserProfileResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GroupUserProfileResponse:
        """Create an instance of GroupUserProfileResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GroupUserProfileResponse.parse_obj(obj)

        _obj = GroupUserProfileResponse.parse_obj({
            "display_name": obj.get("displayName"),
            "user_id": obj.get("userId"),
            "picture_url": obj.get("pictureUrl")
        })
        return _obj

