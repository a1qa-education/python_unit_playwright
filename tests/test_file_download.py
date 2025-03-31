import os

import pytest
from playwright.sync_api import Page

from configs.settings import TEST_APP_URL

DOWNLOAD_DIR = "./downloads"
TEST_FILE = "test-file.txt"


@pytest.mark.file_download
class TestFileDownload:

    def test_file_download(self, page: Page):
        page.goto(TEST_APP_URL)

        page.locator('[href="/download"]').click()
        file_link = page.locator(f'[href="download/{TEST_FILE}"]')

        downloaded_file_path = os.path.join(DOWNLOAD_DIR, TEST_FILE)

        # TODO
        # 1. Before downloading, ensure the file is available for download.
        # 2. Download the file and verify that the file exists after download.
        # 3. After execution, delete the DOWNLOAD_DIR folder along with all its contents.
