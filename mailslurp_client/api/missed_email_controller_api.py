# coding: utf-8

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails from dynamically allocated email addresses. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.  ## Resources  - [Homepage](https://www.mailslurp.com) - Get an [API KEY](https://app.mailslurp.com/sign-up/) - Generated [SDK Clients](https://www.mailslurp.com/docs/) - [Examples](https://github.com/mailslurp/examples) repository  # noqa: E501

    The version of the OpenAPI document: 6.5.2
    Contact: contact@mailslurp.dev
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


class MissedEmailControllerApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_all_missed_emails(self, **kwargs):  # noqa: E501
        """Get all MissedEmails in paginated format  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_missed_emails(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int page: Optional page index in list pagination
        :param int size: Optional page size in list pagination
        :param str sort: Optional createdAt sort direction ASC or DESC
        :param str search_filter: Optional search filter
        :param datetime since: Filter by created at after the given timestamp
        :param datetime before: Filter by created at before the given timestamp
        :param str inbox_id: Optional inbox ID filter
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PageMissedEmailProjection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_all_missed_emails_with_http_info(**kwargs)  # noqa: E501

    def get_all_missed_emails_with_http_info(self, **kwargs):  # noqa: E501
        """Get all MissedEmails in paginated format  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_missed_emails_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int page: Optional page index in list pagination
        :param int size: Optional page size in list pagination
        :param str sort: Optional createdAt sort direction ASC or DESC
        :param str search_filter: Optional search filter
        :param datetime since: Filter by created at after the given timestamp
        :param datetime before: Filter by created at before the given timestamp
        :param str inbox_id: Optional inbox ID filter
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PageMissedEmailProjection, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'page',
            'size',
            'sort',
            'search_filter',
            'since',
            'before',
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
                    " to method get_all_missed_emails" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'size' in local_var_params and local_var_params['size'] is not None:  # noqa: E501
            query_params.append(('size', local_var_params['size']))  # noqa: E501
        if 'sort' in local_var_params and local_var_params['sort'] is not None:  # noqa: E501
            query_params.append(('sort', local_var_params['sort']))  # noqa: E501
        if 'search_filter' in local_var_params and local_var_params['search_filter'] is not None:  # noqa: E501
            query_params.append(('searchFilter', local_var_params['search_filter']))  # noqa: E501
        if 'since' in local_var_params and local_var_params['since'] is not None:  # noqa: E501
            query_params.append(('since', local_var_params['since']))  # noqa: E501
        if 'before' in local_var_params and local_var_params['before'] is not None:  # noqa: E501
            query_params.append(('before', local_var_params['before']))  # noqa: E501
        if 'inbox_id' in local_var_params and local_var_params['inbox_id'] is not None:  # noqa: E501
            query_params.append(('inboxId', local_var_params['inbox_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API_KEY']  # noqa: E501

        return self.api_client.call_api(
            '/missed-emails', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PageMissedEmailProjection',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_unknown_missed_emails(self, **kwargs):  # noqa: E501
        """Get all unknown missed emails in paginated format  # noqa: E501

        Unknown missed emails are emails that were sent to MailSlurp but could not be assigned to an existing inbox.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_unknown_missed_emails(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int page: Optional page index in list pagination
        :param int size: Optional page size in list pagination
        :param str sort: Optional createdAt sort direction ASC or DESC
        :param str search_filter: Optional search filter
        :param datetime since: Filter by created at after the given timestamp
        :param datetime before: Filter by created at before the given timestamp
        :param str inbox_id: Optional inbox ID filter
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PageUnknownMissedEmailProjection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_all_unknown_missed_emails_with_http_info(**kwargs)  # noqa: E501

    def get_all_unknown_missed_emails_with_http_info(self, **kwargs):  # noqa: E501
        """Get all unknown missed emails in paginated format  # noqa: E501

        Unknown missed emails are emails that were sent to MailSlurp but could not be assigned to an existing inbox.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_unknown_missed_emails_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int page: Optional page index in list pagination
        :param int size: Optional page size in list pagination
        :param str sort: Optional createdAt sort direction ASC or DESC
        :param str search_filter: Optional search filter
        :param datetime since: Filter by created at after the given timestamp
        :param datetime before: Filter by created at before the given timestamp
        :param str inbox_id: Optional inbox ID filter
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PageUnknownMissedEmailProjection, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'page',
            'size',
            'sort',
            'search_filter',
            'since',
            'before',
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
                    " to method get_all_unknown_missed_emails" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'size' in local_var_params and local_var_params['size'] is not None:  # noqa: E501
            query_params.append(('size', local_var_params['size']))  # noqa: E501
        if 'sort' in local_var_params and local_var_params['sort'] is not None:  # noqa: E501
            query_params.append(('sort', local_var_params['sort']))  # noqa: E501
        if 'search_filter' in local_var_params and local_var_params['search_filter'] is not None:  # noqa: E501
            query_params.append(('searchFilter', local_var_params['search_filter']))  # noqa: E501
        if 'since' in local_var_params and local_var_params['since'] is not None:  # noqa: E501
            query_params.append(('since', local_var_params['since']))  # noqa: E501
        if 'before' in local_var_params and local_var_params['before'] is not None:  # noqa: E501
            query_params.append(('before', local_var_params['before']))  # noqa: E501
        if 'inbox_id' in local_var_params and local_var_params['inbox_id'] is not None:  # noqa: E501
            query_params.append(('inboxId', local_var_params['inbox_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API_KEY']  # noqa: E501

        return self.api_client.call_api(
            '/missed-emails/unknown', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PageUnknownMissedEmailProjection',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_missed_email(self, missed_email_id, **kwargs):  # noqa: E501
        """Get MissedEmail  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_missed_email(missed_email_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str missed_email_id: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: MissedEmail
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_missed_email_with_http_info(missed_email_id, **kwargs)  # noqa: E501

    def get_missed_email_with_http_info(self, missed_email_id, **kwargs):  # noqa: E501
        """Get MissedEmail  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_missed_email_with_http_info(missed_email_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str missed_email_id: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(MissedEmail, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'missed_email_id'
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
                    " to method get_missed_email" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'missed_email_id' is set
        if self.api_client.client_side_validation and ('missed_email_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['missed_email_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `missed_email_id` when calling `get_missed_email`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'missed_email_id' in local_var_params:
            path_params['missedEmailId'] = local_var_params['missed_email_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API_KEY']  # noqa: E501

        return self.api_client.call_api(
            '/missed-emails/{missedEmailId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MissedEmail',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def wait_for_nth_missed_email(self, index, **kwargs):  # noqa: E501
        """Wait for Nth missed email  # noqa: E501

        Wait for 0 based index missed email  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.wait_for_nth_missed_email(index, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int index: Zero based index of the email to wait for. If 1 missed email already and you want to wait for the 2nd email pass index=1 (required)
        :param str inbox_id: Optional inbox ID filter
        :param int timeout: Optional timeout milliseconds
        :param datetime since: Filter by created at after the given timestamp
        :param datetime before: Filter by created at before the given timestamp
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: MissedEmail
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.wait_for_nth_missed_email_with_http_info(index, **kwargs)  # noqa: E501

    def wait_for_nth_missed_email_with_http_info(self, index, **kwargs):  # noqa: E501
        """Wait for Nth missed email  # noqa: E501

        Wait for 0 based index missed email  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.wait_for_nth_missed_email_with_http_info(index, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int index: Zero based index of the email to wait for. If 1 missed email already and you want to wait for the 2nd email pass index=1 (required)
        :param str inbox_id: Optional inbox ID filter
        :param int timeout: Optional timeout milliseconds
        :param datetime since: Filter by created at after the given timestamp
        :param datetime before: Filter by created at before the given timestamp
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(MissedEmail, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'index',
            'inbox_id',
            'timeout',
            'since',
            'before'
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
                    " to method wait_for_nth_missed_email" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'index' is set
        if self.api_client.client_side_validation and ('index' not in local_var_params or  # noqa: E501
                                                        local_var_params['index'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `index` when calling `wait_for_nth_missed_email`")  # noqa: E501

        if self.api_client.client_side_validation and 'index' in local_var_params and local_var_params['index'] > 2147483647:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `index` when calling `wait_for_nth_missed_email`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if self.api_client.client_side_validation and 'index' in local_var_params and local_var_params['index'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `index` when calling `wait_for_nth_missed_email`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'inbox_id' in local_var_params and local_var_params['inbox_id'] is not None:  # noqa: E501
            query_params.append(('inboxId', local_var_params['inbox_id']))  # noqa: E501
        if 'timeout' in local_var_params and local_var_params['timeout'] is not None:  # noqa: E501
            query_params.append(('timeout', local_var_params['timeout']))  # noqa: E501
        if 'index' in local_var_params and local_var_params['index'] is not None:  # noqa: E501
            query_params.append(('index', local_var_params['index']))  # noqa: E501
        if 'since' in local_var_params and local_var_params['since'] is not None:  # noqa: E501
            query_params.append(('since', local_var_params['since']))  # noqa: E501
        if 'before' in local_var_params and local_var_params['before'] is not None:  # noqa: E501
            query_params.append(('before', local_var_params['before']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API_KEY']  # noqa: E501

        return self.api_client.call_api(
            '/missed-emails/waitForNthMissedEmail', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MissedEmail',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
