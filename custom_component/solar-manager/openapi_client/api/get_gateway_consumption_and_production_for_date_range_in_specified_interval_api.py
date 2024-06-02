# coding: utf-8

"""
    Solar Manager external API 

    This is a Solar Manager external communication service

    The version of the OpenAPI document: 1.19.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from typing_extensions import Annotated
from datetime import datetime

from pydantic import Field, StrictFloat, StrictInt, constr

from typing import Union

from openapi_client.models.gateway_interval_consumption_schema import GatewayIntervalConsumptionSchema

from openapi_client.api_client import ApiClient
from openapi_client.api_response import ApiResponse
from openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class GetGatewayConsumptionAndProductionForDateRangeInSpecifiedIntervalApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_v1_consumption_gateway_smid_range(self, sm_id : Annotated[constr(strict=True, max_length=24, min_length=3), Field(..., description="smId of gateway")], var_from : Annotated[datetime, Field(..., description="date string in ISO format")], to : Annotated[datetime, Field(..., description="date string in ISO format")], interval : Annotated[Union[StrictFloat, StrictInt], Field(..., description="data point interval / for now possible to choose only 300 sec")], **kwargs) -> GatewayIntervalConsumptionSchema:  # noqa: E501
        """get_v1_consumption_gateway_smid_range  # noqa: E501

        API description  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_v1_consumption_gateway_smid_range(sm_id, var_from, to, interval, async_req=True)
        >>> result = thread.get()

        :param sm_id: smId of gateway (required)
        :type sm_id: str
        :param var_from: date string in ISO format (required)
        :type var_from: datetime
        :param to: date string in ISO format (required)
        :type to: datetime
        :param interval: data point interval / for now possible to choose only 300 sec (required)
        :type interval: float
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GatewayIntervalConsumptionSchema
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_v1_consumption_gateway_smid_range_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_v1_consumption_gateway_smid_range_with_http_info(sm_id, var_from, to, interval, **kwargs)  # noqa: E501

    @validate_arguments
    def get_v1_consumption_gateway_smid_range_with_http_info(self, sm_id : Annotated[constr(strict=True, max_length=24, min_length=3), Field(..., description="smId of gateway")], var_from : Annotated[datetime, Field(..., description="date string in ISO format")], to : Annotated[datetime, Field(..., description="date string in ISO format")], interval : Annotated[Union[StrictFloat, StrictInt], Field(..., description="data point interval / for now possible to choose only 300 sec")], **kwargs) -> ApiResponse:  # noqa: E501
        """get_v1_consumption_gateway_smid_range  # noqa: E501

        API description  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_v1_consumption_gateway_smid_range_with_http_info(sm_id, var_from, to, interval, async_req=True)
        >>> result = thread.get()

        :param sm_id: smId of gateway (required)
        :type sm_id: str
        :param var_from: date string in ISO format (required)
        :type var_from: datetime
        :param to: date string in ISO format (required)
        :type to: datetime
        :param interval: data point interval / for now possible to choose only 300 sec (required)
        :type interval: float
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GatewayIntervalConsumptionSchema, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'sm_id',
            'var_from',
            'to',
            'interval'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_v1_consumption_gateway_smid_range" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['sm_id'] is not None:
            _path_params['smId'] = _params['sm_id']


        # process the query parameters
        _query_params = []
        if _params.get('var_from') is not None:  # noqa: E501
            if isinstance(_params['var_from'], datetime):
                _query_params.append(('from', _params['var_from'].strftime(self.api_client.configuration.datetime_format)))
            else:
                _query_params.append(('from', _params['var_from']))

        if _params.get('to') is not None:  # noqa: E501
            if isinstance(_params['to'], datetime):
                _query_params.append(('to', _params['to'].strftime(self.api_client.configuration.datetime_format)))
            else:
                _query_params.append(('to', _params['to']))

        if _params.get('interval') is not None:  # noqa: E501
            _query_params.append(('interval', _params['interval']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basic', 'BearerAuth']  # noqa: E501

        _response_types_map = {
            '200': "GatewayIntervalConsumptionSchema",
        }

        return self.api_client.call_api(
            '/v1/consumption/gateway/{smId}/range', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
