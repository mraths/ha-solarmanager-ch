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



from pydantic import BaseModel, Field, conint

class Model40(BaseModel):
    """
    Model40
    """
    charging_mode: conint(strict=True, le=5, ge=1) = Field(default=..., alias="chargingMode")
    __properties = ["chargingMode"]

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
    def from_json(cls, json_str: str) -> Model40:
        """Create an instance of Model40 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Model40:
        """Create an instance of Model40 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Model40.parse_obj(obj)

        _obj = Model40.parse_obj({
            "charging_mode": obj.get("chargingMode")
        })
        return _obj


