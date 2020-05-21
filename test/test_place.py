# coding: utf-8

"""
    COVID-19 Local API

    API to get local help information about COVID-19 (hotlines, websites, test sites, health departments)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import covid_local
from covid_local.models.place import Place  # noqa: E501
from covid_local.rest import ApiException

class TestPlace(unittest.TestCase):
    """Place unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Place
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = covid_local.models.place.Place()  # noqa: E501
        if include_optional :
            return Place(
                name = '0', 
                geonames_id = 56, 
                search_provider = '0', 
                country = '0', 
                country_code = '0', 
                state = '0', 
                description = '0', 
                lat = 1.337, 
                lon = 1.337
            )
        else :
            return Place(
                name = '0',
                geonames_id = 56,
                search_provider = '0',
        )

    def testPlace(self):
        """Test Place"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
