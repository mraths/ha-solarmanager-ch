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
from pydantic import BaseModel, Field, StrictBool, StrictStr

class GatewayInfoSchema(BaseModel):
    """
    GatewayInfoSchema
    """
    id: Optional[StrictStr] = Field(default=None, alias="_id")
    signal: Optional[StrictStr] = Field(default=None, description="gateway signal")
    name: Optional[StrictStr] = Field(default=None, description="gateway name in system")
    sm_id: Optional[StrictStr] = Field(default=None, description="gateway unique id")
    owner: Optional[StrictStr] = None
    firmware: Optional[StrictStr] = Field(default=None, description="gateway firmware version")
    last_error_date: Optional[date] = Field(default=None, alias="lastErrorDate", description="date of last error")
    mac: Optional[StrictStr] = Field(default=None, description="gateway mac address")
    ip: Optional[StrictStr] = Field(default=None, description="gateway ip")
    is_installation_completed: Optional[StrictBool] = Field(default=None, alias="isInstallationCompleted")
    __properties = ["_id", "signal", "name", "sm_id", "owner", "firmware", "lastErrorDate", "mac", "ip", "isInstallationCompleted"]

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
    def from_json(cls, json_str: str) -> GatewayInfoSchema:
        """Create an instance of GatewayInfoSchema from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GatewayInfoSchema:
        """Create an instance of GatewayInfoSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GatewayInfoSchema.parse_obj(obj)

        _obj = GatewayInfoSchema.parse_obj({
            "id": obj.get("_id"),
            "signal": obj.get("signal"),
            "name": obj.get("name"),
            "sm_id": obj.get("sm_id"),
            "owner": obj.get("owner"),
            "firmware": obj.get("firmware"),
            "last_error_date": obj.get("lastErrorDate"),
            "mac": obj.get("mac"),
            "ip": obj.get("ip"),
            "is_installation_completed": obj.get("isInstallationCompleted")
        })
        return _obj


