# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 2.0.9
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from launchdarkly_api.models.custom_role_key_or_id import CustomRoleKeyOrId  # noqa: F401,E501
from launchdarkly_api.models.policy import Policy  # noqa: F401,E501


class CustomRoleBody(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'description': 'str',
        'key': 'CustomRoleKeyOrId',
        'policy': 'list[Policy]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'key': 'key',
        'policy': 'policy'
    }

    def __init__(self, name=None, description=None, key=None, policy=None):  # noqa: E501
        """CustomRoleBody - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._description = None
        self._key = None
        self._policy = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.key = key
        self.policy = policy

    @property
    def name(self):
        """Gets the name of this CustomRoleBody.  # noqa: E501

        Name of the custom role.  # noqa: E501

        :return: The name of this CustomRoleBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CustomRoleBody.

        Name of the custom role.  # noqa: E501

        :param name: The name of this CustomRoleBody.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this CustomRoleBody.  # noqa: E501

        Description of the custom role.  # noqa: E501

        :return: The description of this CustomRoleBody.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CustomRoleBody.

        Description of the custom role.  # noqa: E501

        :param description: The description of this CustomRoleBody.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def key(self):
        """Gets the key of this CustomRoleBody.  # noqa: E501


        :return: The key of this CustomRoleBody.  # noqa: E501
        :rtype: CustomRoleKeyOrId
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this CustomRoleBody.


        :param key: The key of this CustomRoleBody.  # noqa: E501
        :type: CustomRoleKeyOrId
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def policy(self):
        """Gets the policy of this CustomRoleBody.  # noqa: E501


        :return: The policy of this CustomRoleBody.  # noqa: E501
        :rtype: list[Policy]
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this CustomRoleBody.


        :param policy: The policy of this CustomRoleBody.  # noqa: E501
        :type: list[Policy]
        """
        if policy is None:
            raise ValueError("Invalid value for `policy`, must not be `None`")  # noqa: E501

        self._policy = policy

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CustomRoleBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
