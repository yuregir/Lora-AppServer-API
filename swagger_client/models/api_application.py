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


class ApiApplication(object):
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
        'payload_codec': 'str',
        'payload_decoder_script': 'str',
        'payload_encoder_script': 'str',
        'service_profile_id': 'str'
    }

    attribute_map = {
        'description': 'description',
        'id': 'id',
        'name': 'name',
        'organization_id': 'organizationID',
        'payload_codec': 'payloadCodec',
        'payload_decoder_script': 'payloadDecoderScript',
        'payload_encoder_script': 'payloadEncoderScript',
        'service_profile_id': 'serviceProfileID'
    }

    def __init__(self, description=None, id=None, name=None, organization_id=None, payload_codec=None, payload_decoder_script=None, payload_encoder_script=None, service_profile_id=None):  # noqa: E501
        """ApiApplication - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._id = None
        self._name = None
        self._organization_id = None
        self._payload_codec = None
        self._payload_decoder_script = None
        self._payload_encoder_script = None
        self._service_profile_id = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if organization_id is not None:
            self.organization_id = organization_id
        if payload_codec is not None:
            self.payload_codec = payload_codec
        if payload_decoder_script is not None:
            self.payload_decoder_script = payload_decoder_script
        if payload_encoder_script is not None:
            self.payload_encoder_script = payload_encoder_script
        if service_profile_id is not None:
            self.service_profile_id = service_profile_id

    @property
    def description(self):
        """Gets the description of this ApiApplication.  # noqa: E501

        Description of the application.  # noqa: E501

        :return: The description of this ApiApplication.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ApiApplication.

        Description of the application.  # noqa: E501

        :param description: The description of this ApiApplication.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this ApiApplication.  # noqa: E501

        Application ID. This will be automatically assigned on create.  # noqa: E501

        :return: The id of this ApiApplication.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiApplication.

        Application ID. This will be automatically assigned on create.  # noqa: E501

        :param id: The id of this ApiApplication.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ApiApplication.  # noqa: E501

        Name of the application (must be unique).  # noqa: E501

        :return: The name of this ApiApplication.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiApplication.

        Name of the application (must be unique).  # noqa: E501

        :param name: The name of this ApiApplication.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def organization_id(self):
        """Gets the organization_id of this ApiApplication.  # noqa: E501

        ID of the organization to which the application belongs. After create, this can not be modified.  # noqa: E501

        :return: The organization_id of this ApiApplication.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this ApiApplication.

        ID of the organization to which the application belongs. After create, this can not be modified.  # noqa: E501

        :param organization_id: The organization_id of this ApiApplication.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

    @property
    def payload_codec(self):
        """Gets the payload_codec of this ApiApplication.  # noqa: E501

        Payload codec. NOTE: These field have moved to the device-profile and will be removed in the next major release. When set, the device-profile payload_ fields have priority over the application payload_ fields.  # noqa: E501

        :return: The payload_codec of this ApiApplication.  # noqa: E501
        :rtype: str
        """
        return self._payload_codec

    @payload_codec.setter
    def payload_codec(self, payload_codec):
        """Sets the payload_codec of this ApiApplication.

        Payload codec. NOTE: These field have moved to the device-profile and will be removed in the next major release. When set, the device-profile payload_ fields have priority over the application payload_ fields.  # noqa: E501

        :param payload_codec: The payload_codec of this ApiApplication.  # noqa: E501
        :type: str
        """

        self._payload_codec = payload_codec

    @property
    def payload_decoder_script(self):
        """Gets the payload_decoder_script of this ApiApplication.  # noqa: E501

        Payload decoder script. NOTE: These field have moved to the device-profile and will be removed in the next major release. When set, the device-profile payload_ fields have priority over the application payload_ fields.  # noqa: E501

        :return: The payload_decoder_script of this ApiApplication.  # noqa: E501
        :rtype: str
        """
        return self._payload_decoder_script

    @payload_decoder_script.setter
    def payload_decoder_script(self, payload_decoder_script):
        """Sets the payload_decoder_script of this ApiApplication.

        Payload decoder script. NOTE: These field have moved to the device-profile and will be removed in the next major release. When set, the device-profile payload_ fields have priority over the application payload_ fields.  # noqa: E501

        :param payload_decoder_script: The payload_decoder_script of this ApiApplication.  # noqa: E501
        :type: str
        """

        self._payload_decoder_script = payload_decoder_script

    @property
    def payload_encoder_script(self):
        """Gets the payload_encoder_script of this ApiApplication.  # noqa: E501

        Payload encoder script. NOTE: These field have moved to the device-profile and will be removed in the next major release. When set, the device-profile payload_ fields have priority over the application payload_ fields.  # noqa: E501

        :return: The payload_encoder_script of this ApiApplication.  # noqa: E501
        :rtype: str
        """
        return self._payload_encoder_script

    @payload_encoder_script.setter
    def payload_encoder_script(self, payload_encoder_script):
        """Sets the payload_encoder_script of this ApiApplication.

        Payload encoder script. NOTE: These field have moved to the device-profile and will be removed in the next major release. When set, the device-profile payload_ fields have priority over the application payload_ fields.  # noqa: E501

        :param payload_encoder_script: The payload_encoder_script of this ApiApplication.  # noqa: E501
        :type: str
        """

        self._payload_encoder_script = payload_encoder_script

    @property
    def service_profile_id(self):
        """Gets the service_profile_id of this ApiApplication.  # noqa: E501

        ID of the service profile.  # noqa: E501

        :return: The service_profile_id of this ApiApplication.  # noqa: E501
        :rtype: str
        """
        return self._service_profile_id

    @service_profile_id.setter
    def service_profile_id(self, service_profile_id):
        """Sets the service_profile_id of this ApiApplication.

        ID of the service profile.  # noqa: E501

        :param service_profile_id: The service_profile_id of this ApiApplication.  # noqa: E501
        :type: str
        """

        self._service_profile_id = service_profile_id

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
        if issubclass(ApiApplication, dict):
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
        if not isinstance(other, ApiApplication):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other