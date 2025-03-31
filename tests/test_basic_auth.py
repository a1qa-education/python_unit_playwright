import pytest
from playwright.sync_api import Page

from configs.settings import TEST_APP_URL

SUCCESS_AUTH_MSG = "Congratulations! You must have the proper credentials"


@pytest.mark.basic_auth
class TestBasicAuth:

    def test_basic_auth(self, page: Page):
        # TODO
        # Before navigation set auth headers to context (user and pass: admin).
        # basic_auth_header = http_utils.generate_basic_auth_header(<user>, <password>)

        page.goto(TEST_APP_URL)
        page.locator('[href="/basic_auth"]').click()

        # TODO
        # Verify that SUCCESS_AUTH_MSG is displayed.
