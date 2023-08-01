from selene.support.shared import browser
from selene import be, have


def test_1(browser_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests'))


def test_2():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('!#$kahksdhk;aa;a').press_enter()
    browser.element("[id='result-stats']").should(have.text('Результатов: примерно 0'))
