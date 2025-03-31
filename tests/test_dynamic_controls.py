import pytest
from playwright.sync_api import Page

from configs.settings import TEST_APP_URL


@pytest.mark.dynamic_controls
class TestDynamicControls:

    def test_dynamic_controls(self, page: Page):
        page.goto(TEST_APP_URL)

        page.locator('[href="/dynamic_controls"]').click()
        page.get_by_role("button", name="Enable").click()

        input_field = page.locator('#input-example input')

        # TODO:
        # 1. Verify that the input field is enabled.
        # 2. Generate a random string and type it into the input field.
        # 3. Verify that the random string is displayed.
