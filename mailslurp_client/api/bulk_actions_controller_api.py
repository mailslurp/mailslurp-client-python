# coding: utf-8

"""
    MailSlurp API

    ## Introduction  [MailSlurp](https://www.mailslurp.com) is an Email API for developers and QA testers. It let's users: - create emails addresses on demand - receive emails and attachments in code - send templated HTML emails  ## About  This page contains the REST API documentation for MailSlurp. All requests require API Key authentication passed as an `x-api-key` header.  Create an account to [get your free API Key](https://app.mailslurp.com/sign-up/).  ## Resources - 🔑 [Get API Key](https://app.mailslurp.com/sign-up/)                    - 🎓 [Developer Portal](https://www.mailslurp.com/docs/)           - 📦 [Library SDKs](https://www.mailslurp.com/docs/) - ✍️ [Code Examples](https://www.mailslurp.com/examples) - ⚠️ [Report an issue](https://drift.me/mailslurp)  ## Explore    # noqa: E501

    The version of the OpenAPI document: 6.5.2
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from mailslurp_client.api_client import ApiClient
from mailslurp_client.exceptions import (
    ApiTypeError,
    ApiValueError
)


class BulkActionsControllerApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def bulk_create_inboxes(self, count, **kwargs):  # noqa: E501
        """Bulk create Inboxes (email addresses)  # noqa: E501

        Enterprise Plan Required  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bulk_create_inboxes(count, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int count: Number of inboxes to be created in bulk (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[Inbox]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.bulk_create_inboxes_with_http_info(count, **kwargs)  # noqa: E501

    def bulk_create_inboxes_with_http_info(self, count, **kwargs):  # noqa: E501
        """Bulk create Inboxes (email addresses)  # noqa: E501

        Enterprise Plan Required  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bulk_create_inboxes_with_http_info(count, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int count: Number of inboxes to be created in bulk (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[Inbox], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method bulk_create_inboxes" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'count' is set
        if self.api_client.client_side_validation and ('count' not in local_var_params or  # noqa: E501
                                                        local_var_params['count'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `count` when calling `bulk_create_inboxes`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'count' in local_var_params and local_var_params['count'] is not None:  # noqa: E501
            query_params.append(('count', local_var_params['count']))  # noqa: E501

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
            '/bulk/inboxes', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Inbox]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def bulk_delete_inboxes(self, ids, **kwargs):  # noqa: E501
        """Bulk Delete Inboxes  # noqa: E501

        Enterprise Plan Required  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bulk_delete_inboxes(ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param list[str] ids: ids (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.bulk_delete_inboxes_with_http_info(ids, **kwargs)  # noqa: E501

    def bulk_delete_inboxes_with_http_info(self, ids, **kwargs):  # noqa: E501
        """Bulk Delete Inboxes  # noqa: E501

        Enterprise Plan Required  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bulk_delete_inboxes_with_http_info(ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param list[str] ids: ids (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method bulk_delete_inboxes" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'ids' is set
        if self.api_client.client_side_validation and ('ids' not in local_var_params or  # noqa: E501
                                                        local_var_params['ids'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `ids` when calling `bulk_delete_inboxes`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'ids' in local_var_params:
            body_params = local_var_params['ids']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API_KEY']  # noqa: E501

        return self.api_client.call_api(
            '/bulk/inboxes', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def bulk_send_emails(self, bulk_send_email_options, **kwargs):  # noqa: E501
        """Bulk Send Emails  # noqa: E501

        Enterprise Plan Required  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bulk_send_emails(bulk_send_email_options, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param BulkSendEmailOptions bulk_send_email_options: bulkSendEmailOptions (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.bulk_send_emails_with_http_info(bulk_send_email_options, **kwargs)  # noqa: E501

    def bulk_send_emails_with_http_info(self, bulk_send_email_options, **kwargs):  # noqa: E501
        """Bulk Send Emails  # noqa: E501

        Enterprise Plan Required  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bulk_send_emails_with_http_info(bulk_send_email_options, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param BulkSendEmailOptions bulk_send_email_options: bulkSendEmailOptions (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['bulk_send_email_options']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method bulk_send_emails" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'bulk_send_email_options' is set
        if self.api_client.client_side_validation and ('bulk_send_email_options' not in local_var_params or  # noqa: E501
                                                        local_var_params['bulk_send_email_options'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `bulk_send_email_options` when calling `bulk_send_emails`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'bulk_send_email_options' in local_var_params:
            body_params = local_var_params['bulk_send_email_options']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API_KEY']  # noqa: E501

        return self.api_client.call_api(
            '/bulk/send', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
