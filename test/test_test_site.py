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
from covid_local.models.test_site import TestSite  # noqa: E501
from covid_local.rest import ApiException

class TestTestSite(unittest.TestCase):
    """TestSite unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TestSite
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = covid_local.models.test_site.TestSite()  # noqa: E501
        if include_optional :
            return TestSite(
                country_code = '0', 
                lat = 1.337, 
                lon = 1.337, 
                name = '0', 
                street = '0', 
                zip_code = 56, 
                city = '0', 
                address_supplement = '0', 
                phone = '0', 
                website = '0', 
                operating_hours = '0', 
                appointment_required = True, 
                description = '0', 
                sources = '0', 
                distance = 1.337
            )
        else :
            return TestSite(
        )

    def testTestSite(self):
        """Test TestSite"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
