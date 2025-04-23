from playwright.sync_api import Page
from pages.login_page import LoginPage

def test_valid_login(page: Page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    assert page.url == "https://www.saucedemo.com/inventory.html"
