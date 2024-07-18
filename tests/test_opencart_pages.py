from pages.AdminLoginPage import AdminLoginPage, AdminLoginPageLocators
from pages.BasePage import BasePageLocators
from pages.CatalogPage import CatalogPage, CatalogPageLocators
from pages.HomePage import HomePage, HomePageLocators
from pages.ProductPage import ProductPage, ProductPageLocators
from pages.RegistrationPage import RegistrationPage, RegistrationPageLocators


class TestOpenCartPages:
    def test_homepage_elements(self, browser, url):
        browser.get(url)
        page = HomePage(browser)
        assert page.find_element(BasePageLocators.SEARCH)
        assert page.find_element(BasePageLocators.MENU_NAVBAR)
        assert page.find_element(HomePageLocators.CAROUSEL_ITEM)
        assert page.find_element(HomePageLocators.CONTENT_COLUMN)

    def test_catalog_elements(self, browser, url):
        browser.get(f"{url}/en-gb/catalog/desktops")
        page = CatalogPage(browser)
        assert page.find_element(CatalogPageLocators.LEFT_SIDE_BAR_DESKTOPS)
        assert page.find_element(CatalogPageLocators.LEFT_SIDE_BAR_COMPONENTS)
        assert page.find_element(CatalogPageLocators.LEFT_SIDE_BAR_LAPTOPS_AND_NOTEBOOKS)
        assert page.find_element(CatalogPageLocators.LEFT_SIDE_BAR_CAMERAS)
        assert page.find_element(CatalogPageLocators.LEFT_SIDE_BAR_TABLETS)
        assert page.find_element(CatalogPageLocators.LEFT_SIDE_BAR_MP3_PLAYERS)
        assert page.find_element(CatalogPageLocators.LEFT_SIDE_BAR_PHONES_AND_PDAS)
        assert page.find_element(CatalogPageLocators.LEFT_SIDE_BAR_SOFTWARE)

    def test_product_elements(self, browser, url):
        browser.get(f"{url}/en-gb/product/macbook")
        page = ProductPage(browser)
        assert page.find_element(ProductPageLocators.PRODUCT_IMAGE)
        assert page.find_element(ProductPageLocators.BUTTON_ADD_TO_CART)
        assert page.find_element(ProductPageLocators.QUANTITY)
        assert page.find_element(ProductPageLocators.RATING)
        assert page.find_element(ProductPageLocators.BUTTON_GROUP_ADD_TO_WISH_LIST)

    def test_admin_login_page_elements(self, browser, url):
        browser.get(f'{url}/administration/')
        page = AdminLoginPage(browser)
        assert page.find_element(AdminLoginPageLocators.LOGIN)
        assert page.find_element(AdminLoginPageLocators.PASSWORD)
        assert page.find_element(AdminLoginPageLocators.USERNAME)
        assert page.find_element(AdminLoginPageLocators.INFO_PLEASE_ENTER_CREDENTIALS)

    def test_registration_page_element(self, browser, url):
        browser.get(f"{url}/en-gb?route=account/register")
        page = RegistrationPage(browser)
        assert page.find_element(RegistrationPageLocators.FIRSTNAME)
        assert page.find_element(RegistrationPageLocators.PASSWORD)
        assert page.find_element(RegistrationPageLocators.EMAIL)
        assert page.find_element(RegistrationPageLocators.LASTNAME)
        assert page.find_element(RegistrationPageLocators.SUBSCRIBE)
