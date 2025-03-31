from pathlib import Path

import pytest
from playwright.sync_api import Page

from configs.settings import TEST_APP_URL

TEST_FILE = "test_file.txt"
TEST_FILE_PATH = Path(f"./resources/{TEST_FILE}").resolve()


@pytest.mark.file_upload
class TestFileUpload:

    def test_file_upload(self, page: Page):
        page.goto(TEST_APP_URL)

        page.locator('[href="/upload"]').click()

        file_input = page.locator("#file-upload")
        upload_btn = page.locator("#file-submit")

        # TODO
        # 1. Chose input file and submit.
        # 2. Verify that file name on Upload page is correct.
