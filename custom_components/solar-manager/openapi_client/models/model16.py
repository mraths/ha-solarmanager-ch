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

from datetime import date
from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, constr

class Model16(BaseModel):
    """
    Model16
    """
    id: Optional[StrictStr] = Field(default=None, alias="_id")
    gateway: Optional[StrictStr] = None
    sm_id: constr(strict=True, max_length=16, min_length=3) = Field(default=..., alias="smId", description="smId of gateway")
    inverter: Optional[StrictStr] = None
    capacity: Optional[StrictInt] = Field(default=None, description="string capacity")
    tilt: Optional[StrictInt] = Field(default=None, description="string tilt")
    orientation: Optional[StrictInt] = Field(default=None, description="string orientation")
    created_at: Optional[date] = Field(default=None, alias="createdAt")
    updated_at: Optional[date] = Field(default=None, alias="updatedAt")
    __properties = ["_id", "gateway", "smId", "inverter", "capacity", "tilt", "orientation", "createdAt", "updatedAt"]

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
    def from_json(cls, json_str: str) -> Model16:
        """Create an instance of Model16 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Model16:
        """Create an instance of Model16 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Model16.parse_obj(obj)

        _obj = Model16.parse_obj({
            "id": obj.get("_id"),
            "gateway": obj.get("gateway"),
            "sm_id": obj.get("smId"),
            "inverter": obj.get("inverter"),
            "capacity": obj.get("capacity"),
            "tilt": obj.get("tilt"),
            "orientation": obj.get("orientation"),
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt")
        })
        return _obj


