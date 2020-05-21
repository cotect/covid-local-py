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
from covid_local.models.health_department import HealthDepartment  # noqa: E501
from covid_local.rest import ApiException

class TestHealthDepartment(unittest.TestCase):
    """HealthDepartment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test HealthDepartment
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = covid_local.models.health_department.HealthDepartment()  # noqa: E501
        if include_optional :
            return HealthDepartment(
                country_code = '0', 
                place = '0', 
                geonames_id = 56, 
                name = '0', 
                department = '0', 
                street = '0', 
                zip_code = 56, 
                city = '0', 
                address_supplement = '0', 
                phone = '0', 
                fax = '0', 
                email = '0', 
                website = '0', 
                sources = '0'
            )
        else :
            return HealthDepartment(
        )

    def testHealthDepartment(self):
        """Test HealthDepartment"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
