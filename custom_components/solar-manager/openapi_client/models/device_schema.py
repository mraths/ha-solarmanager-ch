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


from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist

class DeviceSchema(BaseModel):
    """
    DeviceSchema
    """
    id: Optional[StrictStr] = Field(default=None, alias="_id")
    soc: Optional[StrictInt] = Field(default=None, alias="SOC")
    accumulated_error_count: Optional[StrictInt] = Field(default=None, alias="accumulatedErrorCount")
    current_power_inv_sm: Optional[StrictInt] = Field(default=None, alias="currentPowerInvSm")
    current_energy: Optional[StrictInt] = Field(default=None, alias="currentEnergy")
    signal: Optional[StrictStr] = None
    current_percent_on: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="currentPercentOn")
    consumed_for_last24h: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="consumedForLast24h")
    active_device: Optional[StrictInt] = Field(default=None, alias="activeDevice")
    current_power: Optional[StrictInt] = Field(default=None, alias="currentPower")
    errors: Optional[conlist(StrictStr)] = None
    energy_today: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="energyToday")
    switch_state: Optional[StrictInt] = Field(default=None, alias="switchState")
    current_water_temp: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="currentWaterTemp")
    status: Optional[StrictInt] = None
    __properties = ["_id", "SOC", "accumulatedErrorCount", "currentPowerInvSm", "currentEnergy", "signal", "currentPercentOn", "consumedForLast24h", "activeDevice", "currentPower", "errors", "energyToday", "switchState", "currentWaterTemp", "status"]

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
    def from_json(cls, json_str: str) -> DeviceSchema:
        """Create an instance of DeviceSchema from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DeviceSchema:
        """Create an instance of DeviceSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DeviceSchema.parse_obj(obj)

        _obj = DeviceSchema.parse_obj({
            "id": obj.get("_id"),
            "soc": obj.get("SOC"),
            "accumulated_error_count": obj.get("accumulatedErrorCount"),
            "current_power_inv_sm": obj.get("currentPowerInvSm"),
            "current_energy": obj.get("currentEnergy"),
            "signal": obj.get("signal"),
            "current_percent_on": obj.get("currentPercentOn"),
            "consumed_for_last24h": obj.get("consumedForLast24h"),
            "active_device": obj.get("activeDevice"),
            "current_power": obj.get("currentPower"),
            "errors": obj.get("errors"),
            "energy_today": obj.get("energyToday"),
            "switch_state": obj.get("switchState"),
            "current_water_temp": obj.get("currentWaterTemp"),
            "status": obj.get("status")
        })
        return _obj

