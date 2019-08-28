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

from swagger_client.models.api_http_integration_header import ApiHTTPIntegrationHeader  # noqa: F401,E501


class ApiHTTPIntegration(object):
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
        'ack_notification_url': 'str',
        'application_id': 'str',
        'error_notification_url': 'str',
        'headers': 'list[ApiHTTPIntegrationHeader]',
        'join_notification_url': 'str',
        'location_notification_url': 'str',
        'status_notification_url': 'str',
        'uplink_data_url': 'str'
    }

    attribute_map = {
        'ack_notification_url': 'ackNotificationURL',
        'application_id': 'applicationID',
        'error_notification_url': 'errorNotificationURL',
        'headers': 'headers',
        'join_notification_url': 'joinNotificationURL',
        'location_notification_url': 'locationNotificationURL',
        'status_notification_url': 'statusNotificationURL',
        'uplink_data_url': 'uplinkDataURL'
    }

    def __init__(self, ack_notification_url=None, application_id=None, error_notification_url=None, headers=None, join_notification_url=None, location_notification_url=None, status_notification_url=None, uplink_data_url=None):  # noqa: E501
        """ApiHTTPIntegration - a model defined in Swagger"""  # noqa: E501

        self._ack_notification_url = None
        self._application_id = None
        self._error_notification_url = None
        self._headers = None
        self._join_notification_url = None
        self._location_notification_url = None
        self._status_notification_url = None
        self._uplink_data_url = None
        self.discriminator = None

        if ack_notification_url is not None:
            self.ack_notification_url = ack_notification_url
        if application_id is not None:
            self.application_id = application_id
        if error_notification_url is not None:
            self.error_notification_url = error_notification_url
        if headers is not None:
            self.headers = headers
        if join_notification_url is not None:
            self.join_notification_url = join_notification_url
        if location_notification_url is not None:
            self.location_notification_url = location_notification_url
        if status_notification_url is not None:
            self.status_notification_url = status_notification_url
        if uplink_data_url is not None:
            self.uplink_data_url = uplink_data_url

    @property
    def ack_notification_url(self):
        """Gets the ack_notification_url of this ApiHTTPIntegration.  # noqa: E501

        The URL to call for ACK notifications (for confirmed downlink data).  # noqa: E501

        :return: The ack_notification_url of this ApiHTTPIntegration.  # noqa: E501
        :rtype: str
        """
        return self._ack_notification_url

    @ack_notification_url.setter
    def ack_notification_url(self, ack_notification_url):
        """Sets the ack_notification_url of this ApiHTTPIntegration.

        The URL to call for ACK notifications (for confirmed downlink data).  # noqa: E501

        :param ack_notification_url: The ack_notification_url of this ApiHTTPIntegration.  # noqa: E501
        :type: str
        """

        self._ack_notification_url = ack_notification_url

    @property
    def application_id(self):
        """Gets the application_id of this ApiHTTPIntegration.  # noqa: E501

        The id of the application.  # noqa: E501

        :return: The application_id of this ApiHTTPIntegration.  # noqa: E501
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this ApiHTTPIntegration.

        The id of the application.  # noqa: E501

        :param application_id: The application_id of this ApiHTTPIntegration.  # noqa: E501
        :type: str
        """

        self._application_id = application_id

    @property
    def error_notification_url(self):
        """Gets the error_notification_url of this ApiHTTPIntegration.  # noqa: E501

        The URL to call for error notifications.  # noqa: E501

        :return: The error_notification_url of this ApiHTTPIntegration.  # noqa: E501
        :rtype: str
        """
        return self._error_notification_url

    @error_notification_url.setter
    def error_notification_url(self, error_notification_url):
        """Sets the error_notification_url of this ApiHTTPIntegration.

        The URL to call for error notifications.  # noqa: E501

        :param error_notification_url: The error_notification_url of this ApiHTTPIntegration.  # noqa: E501
        :type: str
        """

        self._error_notification_url = error_notification_url

    @property
    def headers(self):
        """Gets the headers of this ApiHTTPIntegration.  # noqa: E501

        The headers to use when making HTTP callbacks.  # noqa: E501

        :return: The headers of this ApiHTTPIntegration.  # noqa: E501
        :rtype: list[ApiHTTPIntegrationHeader]
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this ApiHTTPIntegration.

        The headers to use when making HTTP callbacks.  # noqa: E501

        :param headers: The headers of this ApiHTTPIntegration.  # noqa: E501
        :type: list[ApiHTTPIntegrationHeader]
        """

        self._headers = headers

    @property
    def join_notification_url(self):
        """Gets the join_notification_url of this ApiHTTPIntegration.  # noqa: E501

        The URL to call for join notifications.  # noqa: E501

        :return: The join_notification_url of this ApiHTTPIntegration.  # noqa: E501
        :rtype: str
        """
        return self._join_notification_url

    @join_notification_url.setter
    def join_notification_url(self, join_notification_url):
        """Sets the join_notification_url of this ApiHTTPIntegration.

        The URL to call for join notifications.  # noqa: E501

        :param join_notification_url: The join_notification_url of this ApiHTTPIntegration.  # noqa: E501
        :type: str
        """

        self._join_notification_url = join_notification_url

    @property
    def location_notification_url(self):
        """Gets the location_notification_url of this ApiHTTPIntegration.  # noqa: E501

        The URL to call for location notifications.  # noqa: E501

        :return: The location_notification_url of this ApiHTTPIntegration.  # noqa: E501
        :rtype: str
        """
        return self._location_notification_url

    @location_notification_url.setter
    def location_notification_url(self, location_notification_url):
        """Sets the location_notification_url of this ApiHTTPIntegration.

        The URL to call for location notifications.  # noqa: E501

        :param location_notification_url: The location_notification_url of this ApiHTTPIntegration.  # noqa: E501
        :type: str
        """

        self._location_notification_url = location_notification_url

    @property
    def status_notification_url(self):
        """Gets the status_notification_url of this ApiHTTPIntegration.  # noqa: E501

        The URL to call for device-status notifications.  # noqa: E501

        :return: The status_notification_url of this ApiHTTPIntegration.  # noqa: E501
        :rtype: str
        """
        return self._status_notification_url

    @status_notification_url.setter
    def status_notification_url(self, status_notification_url):
        """Sets the status_notification_url of this ApiHTTPIntegration.

        The URL to call for device-status notifications.  # noqa: E501

        :param status_notification_url: The status_notification_url of this ApiHTTPIntegration.  # noqa: E501
        :type: str
        """

        self._status_notification_url = status_notification_url

    @property
    def uplink_data_url(self):
        """Gets the uplink_data_url of this ApiHTTPIntegration.  # noqa: E501

        The URL to call for uplink data.  # noqa: E501

        :return: The uplink_data_url of this ApiHTTPIntegration.  # noqa: E501
        :rtype: str
        """
        return self._uplink_data_url

    @uplink_data_url.setter
    def uplink_data_url(self, uplink_data_url):
        """Sets the uplink_data_url of this ApiHTTPIntegration.

        The URL to call for uplink data.  # noqa: E501

        :param uplink_data_url: The uplink_data_url of this ApiHTTPIntegration.  # noqa: E501
        :type: str
        """

        self._uplink_data_url = uplink_data_url

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
        if issubclass(ApiHTTPIntegration, dict):
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
        if not isinstance(other, ApiHTTPIntegration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other