# coding: utf-8

"""
    Solar Manager external API 

    This is a Solar Manager external communication service

    The version of the OpenAPI document: 1.19.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class SensorTagSchema(BaseModel):
    """
    the device tag  # noqa: E501
    """
    id: Optional[StrictStr] = Field(default=None, alias="_id")
    name: Optional[StrictStr] = None
    __properties = ["_id", "name"]

    class Config:
        """Pydantic configuration"""
        populate_by_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> SensorTagSchema:
        """Create an instance of SensorTagSchema from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SensorTagSchema:
        """Create an instance of SensorTagSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SensorTagSchema.parse_obj(obj)

        _obj = SensorTagSchema.parse_obj({
            "id": obj.get("_id"),
            "name": obj.get("name")
        })
        return _obj


