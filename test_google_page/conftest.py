import pytest
from datetime import datetime
from selene import browser

@pytest.fixture
def page_open():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = 'https://google.com'


def current_time():
    now = datetime.now().time()
    return (f'{now.hour}:{now.minute}')