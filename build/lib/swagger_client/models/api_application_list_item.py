# coding: utf-8

"""
    LoRa App Server REST API

     For more information about the usage of the LoRa App Server (REST) API, see [https://docs.loraserver.io/lora-app-server/api/](https://docs.loraserver.io/lora-app-server/api/).   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ApiApplicationListItem(object):
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
        'description': 'str',
        'id': 'str',
        'name': 'str',
        'organization_id': 'str',
        'service_profile_id': 'str',
        'service_profile_name': 'str'
    }

    attribute_map = {
        'description': 'description',
        'id': 'id',
        'name': 'name',
        'organization_id': 'organizationID',
        'service_profile_id': 'serviceProfileID',
        'service_profile_name': 'serviceProfileName'
    }

    def __init__(self, description=None, id=None, name=None, organization_id=None, service_profile_id=None, service_profile_name=None):  # noqa: E501
        """ApiApplicationListItem - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._id = None
        self._name = None
        self._organization_id = None
        self._service_profile_id = None
        self._service_profile_name = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if organization_id is not None:
            self.organization_id = organization_id
        if service_profile_id is not None:
            self.service_profile_id = service_profile_id
        if service_profile_name is not None:
            self.service_profile_name = service_profile_name

    @property
    def description(self):
        """Gets the description of this ApiApplicationListItem.  # noqa: E501

        Description of the application.  # noqa: E501

        :return: The description of this ApiApplicationListItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ApiApplicationListItem.

        Description of the application.  # noqa: E501

        :param description: The description of this ApiApplicationListItem.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this ApiApplicationListItem.  # noqa: E501

        Application ID.  # noqa: E501

        :return: The id of this ApiApplicationListItem.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiApplicationListItem.

        Application ID.  # noqa: E501

        :param id: The id of this ApiApplicationListItem.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ApiApplicationListItem.  # noqa: E501

        Name of the application.  # noqa: E501

        :return: The name of this ApiApplicationListItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiApplicationListItem.

        Name of the application.  # noqa: E501

        :param name: The name of this ApiApplicationListItem.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def organization_id(self):
        """Gets the organization_id of this ApiApplicationListItem.  # noqa: E501

        ID of the organization to which the application belongs.  # noqa: E501

        :return: The organization_id of this ApiApplicationListItem.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this ApiApplicationListItem.

        ID of the organization to which the application belongs.  # noqa: E501

        :param organization_id: The organization_id of this ApiApplicationListItem.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

    @property
    def service_profile_id(self):
        """Gets the service_profile_id of this ApiApplicationListItem.  # noqa: E501

        ID of the service profile.  # noqa: E501

        :return: The service_profile_id of this ApiApplicationListItem.  # noqa: E501
        :rtype: str
        """
        return self._service_profile_id

    @service_profile_id.setter
    def service_profile_id(self, service_profile_id):
        """Sets the service_profile_id of this ApiApplicationListItem.

        ID of the service profile.  # noqa: E501

        :param service_profile_id: The service_profile_id of this ApiApplicationListItem.  # noqa: E501
        :type: str
        """

        self._service_profile_id = service_profile_id

    @property
    def service_profile_name(self):
        """Gets the service_profile_name of this ApiApplicationListItem.  # noqa: E501

        Service-profile name.  # noqa: E501

        :return: The service_profile_name of this ApiApplicationListItem.  # noqa: E501
        :rtype: str
        """
        return self._service_profile_name

    @service_profile_name.setter
    def service_profile_name(self, service_profile_name):
        """Sets the service_profile_name of this ApiApplicationListItem.

        Service-profile name.  # noqa: E501

        :param service_profile_name: The service_profile_name of this ApiApplicationListItem.  # noqa: E501
        :type: str
        """

        self._service_profile_name = service_profile_name

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
        if issubclass(ApiApplicationListItem, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ApiApplicationListItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other