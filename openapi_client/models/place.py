# coding: utf-8

"""
    COVID-19 Local API

    API to get local help information about COVID-19 (hotlines, websites, test sites, health departments)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class Place(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'name': 'str',
        'geonames_id': 'int',
        'search_provider': 'str',
        'country': 'str',
        'country_code': 'str',
        'state': 'str',
        'description': 'str',
        'lat': 'float',
        'lon': 'float'
    }

    attribute_map = {
        'name': 'name',
        'geonames_id': 'geonames_id',
        'search_provider': 'search_provider',
        'country': 'country',
        'country_code': 'country_code',
        'state': 'state',
        'description': 'description',
        'lat': 'lat',
        'lon': 'lon'
    }

    def __init__(self, name=None, geonames_id=None, search_provider=None, country=None, country_code=None, state=None, description=None, lat=None, lon=None, local_vars_configuration=None):  # noqa: E501
        """Place - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._geonames_id = None
        self._search_provider = None
        self._country = None
        self._country_code = None
        self._state = None
        self._description = None
        self._lat = None
        self._lon = None
        self.discriminator = None

        self.name = name
        self.geonames_id = geonames_id
        self.search_provider = search_provider
        if country is not None:
            self.country = country
        if country_code is not None:
            self.country_code = country_code
        if state is not None:
            self.state = state
        if description is not None:
            self.description = description
        if lat is not None:
            self.lat = lat
        if lon is not None:
            self.lon = lon

    @property
    def name(self):
        """Gets the name of this Place.  # noqa: E501


        :return: The name of this Place.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Place.


        :param name: The name of this Place.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def geonames_id(self):
        """Gets the geonames_id of this Place.  # noqa: E501


        :return: The geonames_id of this Place.  # noqa: E501
        :rtype: int
        """
        return self._geonames_id

    @geonames_id.setter
    def geonames_id(self, geonames_id):
        """Sets the geonames_id of this Place.


        :param geonames_id: The geonames_id of this Place.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and geonames_id is None:  # noqa: E501
            raise ValueError("Invalid value for `geonames_id`, must not be `None`")  # noqa: E501

        self._geonames_id = geonames_id

    @property
    def search_provider(self):
        """Gets the search_provider of this Place.  # noqa: E501


        :return: The search_provider of this Place.  # noqa: E501
        :rtype: str
        """
        return self._search_provider

    @search_provider.setter
    def search_provider(self, search_provider):
        """Sets the search_provider of this Place.


        :param search_provider: The search_provider of this Place.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and search_provider is None:  # noqa: E501
            raise ValueError("Invalid value for `search_provider`, must not be `None`")  # noqa: E501

        self._search_provider = search_provider

    @property
    def country(self):
        """Gets the country of this Place.  # noqa: E501


        :return: The country of this Place.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Place.


        :param country: The country of this Place.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def country_code(self):
        """Gets the country_code of this Place.  # noqa: E501


        :return: The country_code of this Place.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this Place.


        :param country_code: The country_code of this Place.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def state(self):
        """Gets the state of this Place.  # noqa: E501


        :return: The state of this Place.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Place.


        :param state: The state of this Place.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def description(self):
        """Gets the description of this Place.  # noqa: E501


        :return: The description of this Place.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Place.


        :param description: The description of this Place.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def lat(self):
        """Gets the lat of this Place.  # noqa: E501


        :return: The lat of this Place.  # noqa: E501
        :rtype: float
        """
        return self._lat

    @lat.setter
    def lat(self, lat):
        """Sets the lat of this Place.


        :param lat: The lat of this Place.  # noqa: E501
        :type: float
        """

        self._lat = lat

    @property
    def lon(self):
        """Gets the lon of this Place.  # noqa: E501


        :return: The lon of this Place.  # noqa: E501
        :rtype: float
        """
        return self._lon

    @lon.setter
    def lon(self, lon):
        """Sets the lon of this Place.


        :param lon: The lon of this Place.  # noqa: E501
        :type: float
        """

        self._lon = lon

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, Place):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Place):
            return True

        return self.to_dict() != other.to_dict()