# coding: utf-8

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails from dynamically allocated email addresses. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.   ## Resources - [Homepage](https://www.mailslurp.com) - Get an [API KEY](https://app.mailslurp.com/sign-up/) - Generated [SDK Clients](https://www.mailslurp.com/docs/) - [Examples](https://github.com/mailslurp/examples) repository   # noqa: E501

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


class CommonActionsControllerApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_new_email_address(self, use_domain_pool, **kwargs):  # noqa: E501
        """Create new random inbox  # noqa: E501

        Returns an Inbox with an `id` and an `emailAddress`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_new_email_address(use_domain_pool, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param bool use_domain_pool: useDomainPool (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Inbox
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_new_email_address_with_http_info(use_domain_pool, **kwargs)  # noqa: E501

    def create_new_email_address_with_http_info(self, use_domain_pool, **kwargs):  # noqa: E501
        """Create new random inbox  # noqa: E501

        Returns an Inbox with an `id` and an `emailAddress`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_new_email_address_with_http_info(use_domain_pool, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param bool use_domain_pool: useDomainPool (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Inbox, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'use_domain_pool'
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
                    " to method create_new_email_address" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'use_domain_pool' is set
        if self.api_client.client_side_validation and ('use_domain_pool' not in local_var_params or  # noqa: E501
                                                        local_var_params['use_domain_pool'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `use_domain_pool` when calling `create_new_email_address`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'use_domain_pool' in local_var_params and local_var_params['use_domain_pool'] is not None:  # noqa: E501
            query_params.append(('useDomainPool', local_var_params['use_domain_pool']))  # noqa: E501

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
            '/createInbox', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Inbox',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_new_email_address1(self, use_domain_pool, **kwargs):  # noqa: E501
        """Create new random inbox  # noqa: E501

        Returns an Inbox with an `id` and an `emailAddress`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_new_email_address1(use_domain_pool, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param bool use_domain_pool: useDomainPool (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Inbox
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_new_email_address1_with_http_info(use_domain_pool, **kwargs)  # noqa: E501

    def create_new_email_address1_with_http_info(self, use_domain_pool, **kwargs):  # noqa: E501
        """Create new random inbox  # noqa: E501

        Returns an Inbox with an `id` and an `emailAddress`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_new_email_address1_with_http_info(use_domain_pool, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param bool use_domain_pool: useDomainPool (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Inbox, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'use_domain_pool'
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
                    " to method create_new_email_address1" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'use_domain_pool' is set
        if self.api_client.client_side_validation and ('use_domain_pool' not in local_var_params or  # noqa: E501
                                                        local_var_params['use_domain_pool'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `use_domain_pool` when calling `create_new_email_address1`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'use_domain_pool' in local_var_params and local_var_params['use_domain_pool'] is not None:  # noqa: E501
            query_params.append(('useDomainPool', local_var_params['use_domain_pool']))  # noqa: E501

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
            '/newEmailAddress', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Inbox',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def empty_inbox(self, inbox_id, **kwargs):  # noqa: E501
        """Delete all emails in an inbox  # noqa: E501

        Deletes all emails  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.empty_inbox(inbox_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str inbox_id: inboxId (required)
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
        return self.empty_inbox_with_http_info(inbox_id, **kwargs)  # noqa: E501

    def empty_inbox_with_http_info(self, inbox_id, **kwargs):  # noqa: E501
        """Delete all emails in an inbox  # noqa: E501

        Deletes all emails  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.empty_inbox_with_http_info(inbox_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str inbox_id: inboxId (required)
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

        all_params = [
            'inbox_id'
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
                    " to method empty_inbox" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'inbox_id' is set
        if self.api_client.client_side_validation and ('inbox_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['inbox_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `inbox_id` when calling `empty_inbox`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'inbox_id' in local_var_params and local_var_params['inbox_id'] is not None:  # noqa: E501
            query_params.append(('inboxId', local_var_params['inbox_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['API_KEY']  # noqa: E501

        return self.api_client.call_api(
            '/emptyInbox', 'DELETE',
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

    def send_email_simple(self, email_options, **kwargs):  # noqa: E501
        """Send an email  # noqa: E501

        If no senderId or inboxId provided a random email address will be used to send from.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.send_email_simple(email_options, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param SimpleSendEmailOptions email_options: emailOptions (required)
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
        return self.send_email_simple_with_http_info(email_options, **kwargs)  # noqa: E501

    def send_email_simple_with_http_info(self, email_options, **kwargs):  # noqa: E501
        """Send an email  # noqa: E501

        If no senderId or inboxId provided a random email address will be used to send from.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.send_email_simple_with_http_info(email_options, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param SimpleSendEmailOptions email_options: emailOptions (required)
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

        all_params = [
            'email_options'
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
                    " to method send_email_simple" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'email_options' is set
        if self.api_client.client_side_validation and ('email_options' not in local_var_params or  # noqa: E501
                                                        local_var_params['email_options'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `email_options` when calling `send_email_simple`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'email_options' in local_var_params:
            body_params = local_var_params['email_options']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API_KEY']  # noqa: E501

        return self.api_client.call_api(
            '/sendEmail', 'POST',
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
