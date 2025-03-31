import pytest
from playwright.sync_api import Page

from configs.settings import TEST_APP_URL


@pytest.mark.frames
class TestFramesHandling:

    def test_frames_handling(self, page: Page):
        page.goto(TEST_APP_URL)

        page.locator('[href="/frames"]').click()
        page.locator('[href="/iframe"]').click()

        iframe_locator = page.locator("iframe#mce_0_ifr")

        # TODO
        # 1. Type text to the input field.
        # 2. Undo changes.
        # 2. Verify that initial text is displayed in the editor.
