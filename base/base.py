import pytest
from _pytest.fixtures import FixtureRequest

from pages.start_page import StartPage
from pages.failed_autorization_page import FailAutorizationPage
from pages.campaign_page import CampaignPage
from pages.campaign_menu_page import CampaignMenuPage
from pages.segment_config_page import SegmentConfigPage


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.start_page: StartPage = request.getfixturevalue('start_page')
        self.failed_autorization_page: FailAutorizationPage = request.getfixturevalue('failed_autorization_page')
        self.campaign_page: CampaignPage = request.getfixturevalue('campaign_page')
        self.campaign_menu_page: CampaignMenuPage = request.getfixturevalue('campaign_menu_page')
        self.segment_config_page: SegmentConfigPage = request.getfixturevalue('segment_config_page')