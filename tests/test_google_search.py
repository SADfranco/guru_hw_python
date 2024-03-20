from selene import browser, be, have
from conftest import current_time

def test_search_current_time_and_city(configuration):
    browser.open('')
    browser.element('[name="q"]').should(be.blank).type('Текущее время').press_enter()
    browser.element('[id="search"]').should(have.text(current_time()))
    browser.element('[id="search"]').should(have.text('Москва'))

def test_invalid_search_request(configuration):
    browser.open('')
    browser.element('[name="q"]').should(be.blank).type("kmklnsalkcmdsk;mv;dsl,v'dsl,vsd,v'ds,v;dsv';dsv;'dss,c;sd,cs,c").press_enter()
    browser.element('.card-section').should(have.text('ничего не найдено'))