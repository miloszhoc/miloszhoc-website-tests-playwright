import pytest
from playwright.sync_api import Page

from config import BASE_URL


@pytest.fixture()
def open_base_page(page: Page):
    page.goto(BASE_URL)
    return page
