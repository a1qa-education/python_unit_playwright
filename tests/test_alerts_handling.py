import pytest
from playwright.sync_api import Page

from configs.settings import TEST_APP_URL

SUCCESS_ALERT_MSG = "You successfully clicked an alert"


@pytest.mark.alerts
class TestAlertsHandling:

    def test_alerts_handling(self, page: Page):
        page.goto(TEST_APP_URL)

        page.locator('[href="/javascript_alerts"]').click()
        page.locator('[onclick="jsAlert()"]').click()

        # TODO:
        # 1. Accept the alert.
        # 2. Verify that the SUCCESS_ALERT_MSG is displayed.
