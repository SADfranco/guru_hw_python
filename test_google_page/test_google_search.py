from selene import browser, be, have
import pytest
from datetime import datetime

def current_time():
    now = datetime.now().time()
    return (f'{now.hour}:{now.minute}')


@pytest.fixture(scope="function",autouse="True")
def page_open():
    # options = webdriver.ChromeOptions()
    # options.add_argument('--enable-automation')
    # options.add_argument('window-size=1920,1080')
    # browser.config.driver_options = options
    browser.config.driver.maximize_window()
    browser.open('https://google.com')


def test_search_current_time_and_city(page_open):
    browser.element('[name="q"]').should(be.blank).type('Текущее время').press_enter()
    browser.element('[id="search"]').should(have.text(current_time()))
    browser.element('[id="search"]').should(have.text('Москва'))

def test_invalid_seach_request(page_open):
    browser.element('[name="q"]').should(be.blank).type("kmklnsalkcmdsk;mv;dsl,v'dsl,vsd,v'ds,v;dsv';dsv;'dss,c;sd,cs,c").press_enter()
    browser.driver.refresh()
    browser.element('.card-section').should(have.text('ничего не найдено'))
