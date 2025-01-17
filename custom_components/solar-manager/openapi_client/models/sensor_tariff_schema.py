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
from pydantic import BaseModel, Field, StrictInt, StrictStr

class SensorTariffSchema(BaseModel):
    """
    SensorTariffSchema
    """
    id: Optional[StrictStr] = Field(default=None, alias="_id")
    current_energy_purchase_tariff1: Optional[StrictInt] = Field(default=None, alias="CurrentEnergyPurchaseTariff1")
    current_energy_delivery_tariff1: Optional[StrictInt] = Field(default=None, alias="CurrentEnergyDeliveryTariff1")
    current_energy_purchase_tariff2: Optional[StrictInt] = Field(default=None, alias="CurrentEnergyPurchaseTariff2")
    current_energy_delivery_tariff2: Optional[StrictInt] = Field(default=None, alias="CurrentEnergyDeliveryTariff2")
    created_at: Optional[date] = Field(default=None, alias="createdAt")
    updated_at: Optional[date] = Field(default=None, alias="updatedAt")
    v: Optional[StrictInt] = Field(default=None, alias="__v")
    __properties = ["_id", "CurrentEnergyPurchaseTariff1", "CurrentEnergyDeliveryTariff1", "CurrentEnergyPurchaseTariff2", "CurrentEnergyDeliveryTariff2", "createdAt", "updatedAt", "__v"]

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
    def from_json(cls, json_str: str) -> SensorTariffSchema:
        """Create an instance of SensorTariffSchema from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SensorTariffSchema:
        """Create an instance of SensorTariffSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SensorTariffSchema.parse_obj(obj)

        _obj = SensorTariffSchema.parse_obj({
            "id": obj.get("_id"),
            "current_energy_purchase_tariff1": obj.get("CurrentEnergyPurchaseTariff1"),
            "current_energy_delivery_tariff1": obj.get("CurrentEnergyDeliveryTariff1"),
            "current_energy_purchase_tariff2": obj.get("CurrentEnergyPurchaseTariff2"),
            "current_energy_delivery_tariff2": obj.get("CurrentEnergyDeliveryTariff2"),
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt"),
            "v": obj.get("__v")
        })
        return _obj


