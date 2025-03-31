import pytest
from playwright.sync_api import Page

from configs.settings import TEST_APP_URL

EXPECTED_DUE_VALUE = 251.00
CURRENCY_SYMBOL = "$"


@pytest.mark.data_tables
class TestDataTables:

    def test_data_table(self, page: Page):
        page.goto(TEST_APP_URL)

        page.locator('[href="/tables"]').click()
        page.locator("table#table1").wait_for(state="visible")

        total_sum = 0
        rows = 0

        # TODO:
        # 1. Get rows count in table.
        # 2. Loop through all rows:
        # - extract the numeric values from the "Due" column,
        # - remove the currency symbols,
        # - convert the value to a float and add the value to the total sum".

        assert total_sum == EXPECTED_DUE_VALUE, f"Expected Due amount: {EXPECTED_DUE_VALUE}, Actual: {total_sum}"
