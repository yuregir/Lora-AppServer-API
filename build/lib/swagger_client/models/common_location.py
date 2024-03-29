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

from swagger_client.models.common_location_source import CommonLocationSource  # noqa: F401,E501


class CommonLocation(object):
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
        'accuracy': 'int',
        'altitude': 'float',
        'latitude': 'float',
        'longitude': 'float',
        'source': 'CommonLocationSource'
    }

    attribute_map = {
        'accuracy': 'accuracy',
        'altitude': 'altitude',
        'latitude': 'latitude',
        'longitude': 'longitude',
        'source': 'source'
    }

    def __init__(self, accuracy=None, altitude=None, latitude=None, longitude=None, source=None):  # noqa: E501
        """CommonLocation - a model defined in Swagger"""  # noqa: E501

        self._accuracy = None
        self._altitude = None
        self._latitude = None
        self._longitude = None
        self._source = None
        self.discriminator = None

        if accuracy is not None:
            self.accuracy = accuracy
        if altitude is not None:
            self.altitude = altitude
        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude
        if source is not None:
            self.source = source

    @property
    def accuracy(self):
        """Gets the accuracy of this CommonLocation.  # noqa: E501

        Accuracy (in meters).  # noqa: E501

        :return: The accuracy of this CommonLocation.  # noqa: E501
        :rtype: int
        """
        return self._accuracy

    @accuracy.setter
    def accuracy(self, accuracy):
        """Sets the accuracy of this CommonLocation.

        Accuracy (in meters).  # noqa: E501

        :param accuracy: The accuracy of this CommonLocation.  # noqa: E501
        :type: int
        """

        self._accuracy = accuracy

    @property
    def altitude(self):
        """Gets the altitude of this CommonLocation.  # noqa: E501

        Altitude.  # noqa: E501

        :return: The altitude of this CommonLocation.  # noqa: E501
        :rtype: float
        """
        return self._altitude

    @altitude.setter
    def altitude(self, altitude):
        """Sets the altitude of this CommonLocation.

        Altitude.  # noqa: E501

        :param altitude: The altitude of this CommonLocation.  # noqa: E501
        :type: float
        """

        self._altitude = altitude

    @property
    def latitude(self):
        """Gets the latitude of this CommonLocation.  # noqa: E501

        Latitude.  # noqa: E501

        :return: The latitude of this CommonLocation.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this CommonLocation.

        Latitude.  # noqa: E501

        :param latitude: The latitude of this CommonLocation.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this CommonLocation.  # noqa: E501

        Longitude.  # noqa: E501

        :return: The longitude of this CommonLocation.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this CommonLocation.

        Longitude.  # noqa: E501

        :param longitude: The longitude of this CommonLocation.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

    @property
    def source(self):
        """Gets the source of this CommonLocation.  # noqa: E501

        Location source.  # noqa: E501

        :return: The source of this CommonLocation.  # noqa: E501
        :rtype: CommonLocationSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this CommonLocation.

        Location source.  # noqa: E501

        :param source: The source of this CommonLocation.  # noqa: E501
        :type: CommonLocationSource
        """

        self._source = source

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
        if issubclass(CommonLocation, dict):
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
        if not isinstance(other, CommonLocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
