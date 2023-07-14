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
from linebot.v3.messaging.models.imagemap_area import ImagemapArea
from linebot.v3.messaging.models.imagemap_external_link import ImagemapExternalLink

class ImagemapVideo(BaseModel):
    """
    ImagemapVideo
    """
    original_content_url: Optional[StrictStr] = Field(None, alias="originalContentUrl")
    preview_image_url: Optional[StrictStr] = Field(None, alias="previewImageUrl")
    area: Optional[ImagemapArea] = None
    external_link: Optional[ImagemapExternalLink] = Field(None, alias="externalLink")

    __properties = ["originalContentUrl", "previewImageUrl", "area", "externalLink"]

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
    def from_json(cls, json_str: str) -> ImagemapVideo:
        """Create an instance of ImagemapVideo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of area
        if self.area:
            _dict['area'] = self.area.to_dict()
        # override the default output from pydantic by calling `to_dict()` of external_link
        if self.external_link:
            _dict['externalLink'] = self.external_link.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ImagemapVideo:
        """Create an instance of ImagemapVideo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ImagemapVideo.parse_obj(obj)

        _obj = ImagemapVideo.parse_obj({
            "original_content_url": obj.get("originalContentUrl"),
            "preview_image_url": obj.get("previewImageUrl"),
            "area": ImagemapArea.from_dict(obj.get("area")) if obj.get("area") is not None else None,
            "external_link": ImagemapExternalLink.from_dict(obj.get("externalLink")) if obj.get("externalLink") is not None else None
        })
        return _obj

