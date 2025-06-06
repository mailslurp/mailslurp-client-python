# coding: utf-8

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails and SMS from dynamically allocated email addresses and phone numbers. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.  ## Resources  - [Homepage](https://www.mailslurp.com) - Get an [API KEY](https://app.mailslurp.com/sign-up/) - Generated [SDK Clients](https://docs.mailslurp.com/) - [Examples](https://github.com/mailslurp/examples) repository  # noqa: E501

    The version of the OpenAPI document: 6.5.2
    Contact: contact@mailslurp.dev
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mailslurp_client
from mailslurp_client.models.email_feature_support_result import EmailFeatureSupportResult  # noqa: E501
from mailslurp_client.rest import ApiException

class TestEmailFeatureSupportResult(unittest.TestCase):
    """EmailFeatureSupportResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EmailFeatureSupportResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mailslurp_client.models.email_feature_support_result.EmailFeatureSupportResult()  # noqa: E501
        if include_optional :
            return EmailFeatureSupportResult(
                names = mailslurp_client.models.email_feature_names.EmailFeatureNames(
                    family = [
                        mailslurp_client.models.email_feature_family_name.EmailFeatureFamilyName(
                            slug = 'aol', 
                            name = '0', )
                        ], 
                    platform = [
                        mailslurp_client.models.email_feature_platform_name.EmailFeaturePlatformName(
                            slug = 'android', 
                            name = '0', )
                        ], 
                    category = [
                        mailslurp_client.models.email_feature_category_name.EmailFeatureCategoryName(
                            slug = 'css', 
                            name = '0', )
                        ], ), 
                detected_features = [
                    'amp'
                    ], 
                feature_overviews = [
                    mailslurp_client.models.email_feature_overview.EmailFeatureOverview(
                        feature = 'amp', 
                        title = '0', 
                        description = '0', 
                        category = 'css', 
                        notes = '0', 
                        notes_numbers = {
                            'key' : '0'
                            }, 
                        feature_statistics = [
                            mailslurp_client.models.email_feature_family_statistics.EmailFeatureFamilyStatistics(
                                feature = 'amp', 
                                family = 'aol', 
                                platforms = [
                                    mailslurp_client.models.email_feature_platform_statistics.EmailFeaturePlatformStatistics(
                                        platform = 'android', 
                                        versions = [
                                            mailslurp_client.models.email_feature_version_statistics.EmailFeatureVersionStatistics(
                                                version = '0', 
                                                support_flags = mailslurp_client.models.email_feature_support_flags.EmailFeatureSupportFlags(
                                                    status = 'SUPPORTED', 
                                                    notes = [
                                                        '0'
                                                        ], ), )
                                            ], )
                                    ], )
                            ], 
                        statuses = [
                            'SUPPORTED'
                            ], )
                    ], 
                feature_percentages = [
                    mailslurp_client.models.email_feature_support_status_percentage.EmailFeatureSupportStatusPercentage(
                        status = 'SUPPORTED', 
                        percentage = 1.337, )
                    ]
            )
        else :
            return EmailFeatureSupportResult(
                names = mailslurp_client.models.email_feature_names.EmailFeatureNames(
                    family = [
                        mailslurp_client.models.email_feature_family_name.EmailFeatureFamilyName(
                            slug = 'aol', 
                            name = '0', )
                        ], 
                    platform = [
                        mailslurp_client.models.email_feature_platform_name.EmailFeaturePlatformName(
                            slug = 'android', 
                            name = '0', )
                        ], 
                    category = [
                        mailslurp_client.models.email_feature_category_name.EmailFeatureCategoryName(
                            slug = 'css', 
                            name = '0', )
                        ], ),
                detected_features = [
                    'amp'
                    ],
                feature_overviews = [
                    mailslurp_client.models.email_feature_overview.EmailFeatureOverview(
                        feature = 'amp', 
                        title = '0', 
                        description = '0', 
                        category = 'css', 
                        notes = '0', 
                        notes_numbers = {
                            'key' : '0'
                            }, 
                        feature_statistics = [
                            mailslurp_client.models.email_feature_family_statistics.EmailFeatureFamilyStatistics(
                                feature = 'amp', 
                                family = 'aol', 
                                platforms = [
                                    mailslurp_client.models.email_feature_platform_statistics.EmailFeaturePlatformStatistics(
                                        platform = 'android', 
                                        versions = [
                                            mailslurp_client.models.email_feature_version_statistics.EmailFeatureVersionStatistics(
                                                version = '0', 
                                                support_flags = mailslurp_client.models.email_feature_support_flags.EmailFeatureSupportFlags(
                                                    status = 'SUPPORTED', 
                                                    notes = [
                                                        '0'
                                                        ], ), )
                                            ], )
                                    ], )
                            ], 
                        statuses = [
                            'SUPPORTED'
                            ], )
                    ],
                feature_percentages = [
                    mailslurp_client.models.email_feature_support_status_percentage.EmailFeatureSupportStatusPercentage(
                        status = 'SUPPORTED', 
                        percentage = 1.337, )
                    ],
        )

    def testEmailFeatureSupportResult(self):
        """Test EmailFeatureSupportResult"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
