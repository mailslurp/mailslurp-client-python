# coding: utf-8

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails from dynamically allocated email addresses. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.  ## Resources  - [Homepage](https://www.mailslurp.com) - Get an [API KEY](https://app.mailslurp.com/sign-up/) - Generated [SDK Clients](https://www.mailslurp.com/docs/) - [Examples](https://github.com/mailslurp/examples) repository   # noqa: E501

    The version of the OpenAPI document: 6.5.2
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from mailslurp_client.api_client import ApiClient
from mailslurp_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ExportControllerApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def export_entities(self, api_key, export_type, output_format, **kwargs):  # noqa: E501
        """Export inboxes link callable via browser  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.export_entities(api_key, export_type, output_format, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str api_key: apiKey (required)
        :param str export_type: exportType (required)
        :param str output_format: outputFormat (required)
        :param datetime created_earliest_time: createdEarliestTime
        :param datetime created_oldest_time: createdOldestTime
        :param bool exclude_previously_exported: excludePreviouslyExported
        :param str filter: filter
        :param str list_separator_token: listSeparatorToken
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.export_entities_with_http_info(api_key, export_type, output_format, **kwargs)  # noqa: E501

    def export_entities_with_http_info(self, api_key, export_type, output_format, **kwargs):  # noqa: E501
        """Export inboxes link callable via browser  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.export_entities_with_http_info(api_key, export_type, output_format, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str api_key: apiKey (required)
        :param str export_type: exportType (required)
        :param str output_format: outputFormat (required)
        :param datetime created_earliest_time: createdEarliestTime
        :param datetime created_oldest_time: createdOldestTime
        :param bool exclude_previously_exported: excludePreviouslyExported
        :param str filter: filter
        :param str list_separator_token: listSeparatorToken
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(str, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'api_key',
            'export_type',
            'output_format',
            'created_earliest_time',
            'created_oldest_time',
            'exclude_previously_exported',
            'filter',
            'list_separator_token'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method export_entities" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'api_key' is set
        if self.api_client.client_side_validation and ('api_key' not in local_var_params or  # noqa: E501
                                                        local_var_params['api_key'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `api_key` when calling `export_entities`")  # noqa: E501
        # verify the required parameter 'export_type' is set
        if self.api_client.client_side_validation and ('export_type' not in local_var_params or  # noqa: E501
                                                        local_var_params['export_type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `export_type` when calling `export_entities`")  # noqa: E501
        # verify the required parameter 'output_format' is set
        if self.api_client.client_side_validation and ('output_format' not in local_var_params or  # noqa: E501
                                                        local_var_params['output_format'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `output_format` when calling `export_entities`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'api_key' in local_var_params and local_var_params['api_key'] is not None:  # noqa: E501
            query_params.append(('apiKey', local_var_params['api_key']))  # noqa: E501
        if 'created_earliest_time' in local_var_params and local_var_params['created_earliest_time'] is not None:  # noqa: E501
            query_params.append(('createdEarliestTime', local_var_params['created_earliest_time']))  # noqa: E501
        if 'created_oldest_time' in local_var_params and local_var_params['created_oldest_time'] is not None:  # noqa: E501
            query_params.append(('createdOldestTime', local_var_params['created_oldest_time']))  # noqa: E501
        if 'exclude_previously_exported' in local_var_params and local_var_params['exclude_previously_exported'] is not None:  # noqa: E501
            query_params.append(('excludePreviouslyExported', local_var_params['exclude_previously_exported']))  # noqa: E501
        if 'export_type' in local_var_params and local_var_params['export_type'] is not None:  # noqa: E501
            query_params.append(('exportType', local_var_params['export_type']))  # noqa: E501
        if 'filter' in local_var_params and local_var_params['filter'] is not None:  # noqa: E501
            query_params.append(('filter', local_var_params['filter']))  # noqa: E501
        if 'list_separator_token' in local_var_params and local_var_params['list_separator_token'] is not None:  # noqa: E501
            query_params.append(('listSeparatorToken', local_var_params['list_separator_token']))  # noqa: E501
        if 'output_format' in local_var_params and local_var_params['output_format'] is not None:  # noqa: E501
            query_params.append(('outputFormat', local_var_params['output_format']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API_KEY']  # noqa: E501

        return self.api_client.call_api(
            '/export', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_export_link(self, export_type, export_options, **kwargs):  # noqa: E501
        """Get export link  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_export_link(export_type, export_options, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str export_type: exportType (required)
        :param ExportOptions export_options: exportOptions (required)
        :param str api_key: apiKey
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ExportLink
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_export_link_with_http_info(export_type, export_options, **kwargs)  # noqa: E501

    def get_export_link_with_http_info(self, export_type, export_options, **kwargs):  # noqa: E501
        """Get export link  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_export_link_with_http_info(export_type, export_options, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str export_type: exportType (required)
        :param ExportOptions export_options: exportOptions (required)
        :param str api_key: apiKey
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ExportLink, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'export_type',
            'export_options',
            'api_key'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_export_link" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'export_type' is set
        if self.api_client.client_side_validation and ('export_type' not in local_var_params or  # noqa: E501
                                                        local_var_params['export_type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `export_type` when calling `get_export_link`")  # noqa: E501
        # verify the required parameter 'export_options' is set
        if self.api_client.client_side_validation and ('export_options' not in local_var_params or  # noqa: E501
                                                        local_var_params['export_options'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `export_options` when calling `get_export_link`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'api_key' in local_var_params and local_var_params['api_key'] is not None:  # noqa: E501
            query_params.append(('apiKey', local_var_params['api_key']))  # noqa: E501
        if 'export_type' in local_var_params and local_var_params['export_type'] is not None:  # noqa: E501
            query_params.append(('exportType', local_var_params['export_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'export_options' in local_var_params:
            body_params = local_var_params['export_options']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API_KEY']  # noqa: E501

        return self.api_client.call_api(
            '/export', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ExportLink',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)