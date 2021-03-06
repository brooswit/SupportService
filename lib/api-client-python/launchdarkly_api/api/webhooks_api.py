# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 2.0.9
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from launchdarkly_api.api_client import ApiClient


class WebhooksApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_webhook(self, resource_id, **kwargs):  # noqa: E501
        """Delete a webhook by ID.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_webhook(resource_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str resource_id: The resource ID. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_webhook_with_http_info(resource_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_webhook_with_http_info(resource_id, **kwargs)  # noqa: E501
            return data

    def delete_webhook_with_http_info(self, resource_id, **kwargs):  # noqa: E501
        """Delete a webhook by ID.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_webhook_with_http_info(resource_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str resource_id: The resource ID. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['resource_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_webhook" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'resource_id' is set
        if ('resource_id' not in params or
                params['resource_id'] is None):
            raise ValueError("Missing the required parameter `resource_id` when calling `delete_webhook`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'resource_id' in params:
            path_params['resourceId'] = params['resource_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/webhooks/{resourceId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_webhook(self, resource_id, **kwargs):  # noqa: E501
        """Get a webhook by ID.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_webhook(resource_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str resource_id: The resource ID. (required)
        :return: Webhook
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_webhook_with_http_info(resource_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_webhook_with_http_info(resource_id, **kwargs)  # noqa: E501
            return data

    def get_webhook_with_http_info(self, resource_id, **kwargs):  # noqa: E501
        """Get a webhook by ID.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_webhook_with_http_info(resource_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str resource_id: The resource ID. (required)
        :return: Webhook
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['resource_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_webhook" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'resource_id' is set
        if ('resource_id' not in params or
                params['resource_id'] is None):
            raise ValueError("Missing the required parameter `resource_id` when calling `get_webhook`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'resource_id' in params:
            path_params['resourceId'] = params['resource_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/webhooks/{resourceId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Webhook',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_webhooks(self, **kwargs):  # noqa: E501
        """Fetch a list of all webhooks.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_webhooks(async=True)
        >>> result = thread.get()

        :param async bool
        :return: Webhooks
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_webhooks_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_webhooks_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_webhooks_with_http_info(self, **kwargs):  # noqa: E501
        """Fetch a list of all webhooks.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_webhooks_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: Webhooks
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_webhooks" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/webhooks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Webhooks',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def patch_webhook(self, resource_id, patch_delta, **kwargs):  # noqa: E501
        """Modify a webhook by ID.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.patch_webhook(resource_id, patch_delta, async=True)
        >>> result = thread.get()

        :param async bool
        :param str resource_id: The resource ID. (required)
        :param list[PatchOperation] patch_delta: Requires a JSON Patch representation of the desired changes to the project. 'http://jsonpatch.com/' (required)
        :return: Webhook
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.patch_webhook_with_http_info(resource_id, patch_delta, **kwargs)  # noqa: E501
        else:
            (data) = self.patch_webhook_with_http_info(resource_id, patch_delta, **kwargs)  # noqa: E501
            return data

    def patch_webhook_with_http_info(self, resource_id, patch_delta, **kwargs):  # noqa: E501
        """Modify a webhook by ID.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.patch_webhook_with_http_info(resource_id, patch_delta, async=True)
        >>> result = thread.get()

        :param async bool
        :param str resource_id: The resource ID. (required)
        :param list[PatchOperation] patch_delta: Requires a JSON Patch representation of the desired changes to the project. 'http://jsonpatch.com/' (required)
        :return: Webhook
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['resource_id', 'patch_delta']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_webhook" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'resource_id' is set
        if ('resource_id' not in params or
                params['resource_id'] is None):
            raise ValueError("Missing the required parameter `resource_id` when calling `patch_webhook`")  # noqa: E501
        # verify the required parameter 'patch_delta' is set
        if ('patch_delta' not in params or
                params['patch_delta'] is None):
            raise ValueError("Missing the required parameter `patch_delta` when calling `patch_webhook`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'resource_id' in params:
            path_params['resourceId'] = params['resource_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'patch_delta' in params:
            body_params = params['patch_delta']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/webhooks/{resourceId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Webhook',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_webhook(self, webhook_body, **kwargs):  # noqa: E501
        """Create a webhook.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_webhook(webhook_body, async=True)
        >>> result = thread.get()

        :param async bool
        :param WebhookBody webhook_body: New webhook. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.post_webhook_with_http_info(webhook_body, **kwargs)  # noqa: E501
        else:
            (data) = self.post_webhook_with_http_info(webhook_body, **kwargs)  # noqa: E501
            return data

    def post_webhook_with_http_info(self, webhook_body, **kwargs):  # noqa: E501
        """Create a webhook.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_webhook_with_http_info(webhook_body, async=True)
        >>> result = thread.get()

        :param async bool
        :param WebhookBody webhook_body: New webhook. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['webhook_body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_webhook" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'webhook_body' is set
        if ('webhook_body' not in params or
                params['webhook_body'] is None):
            raise ValueError("Missing the required parameter `webhook_body` when calling `post_webhook`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'webhook_body' in params:
            body_params = params['webhook_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/webhooks', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
