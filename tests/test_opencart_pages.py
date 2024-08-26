import allure

from pages.AdminLoginPage import AdminLoginPage, AdminLoginPageLocators
from pages.BasePage import BasePageLocators
from pages.CatalogPage import CatalogPage, CatalogPageLocators
from pages.HomePage import HomePage, HomePageLocators
from pages.ProductPage import ProductPage, ProductPageLocators
from pages.RegistrationPage import RegistrationPage, RegistrationPageLocators


class TestOpenCartPages:

    @allure.description("Verify homepage elements are present")
    @allure.title("Test Homepage Elements")
    def test_homepage_elements(self, browser, url):
        with allure.step("Open homepage"):
            browser.get(url)

        page = HomePage(browser)

        with allure.step("Check for search element"):
            assert page.find_element(BasePageLocators.SEARCH)

        with allure.step("Check for menu navbar element"):
            assert page.find_element(BasePageLocators.MENU_NAVBAR)

        with allure.step("Check for carousel item element"):
            assert page.find_element(HomePageLocators.CAROUSEL_ITEM)

        with allure.step("Check for content column element"):
            assert page.find_element(HomePageLocators.CONTENT_COLUMN)

    @allure.description("Verify catalog elements are present")
    @allure.title("Test Catalog Elements")
    def test_catalog_elements(self, browser, url):
        with allure.step("Open catalog page for desktops"):
            browser.get(f"{url}/en-gb/catalog/desktops")

        page = CatalogPage(browser)

        with allure.step("Check for left sidebar desktops element"):
            assert page.find_element(CatalogPageLocators.LEFT_SIDE_BAR_DESKTOPS)

        with allure.step("Check for left sidebar components element"):
            assert page.find_element(CatalogPageLocators.LEFT_SIDE_BAR_COMPONENTS)

        with allure.step("Check for left sidebar laptops and notebooks element"):
            assert page.find_element(CatalogPageLocators.LEFT_SIDE_BAR_LAPTOPS_AND_NOTEBOOKS)

        with allure.step("Check for left sidebar cameras element"):
            assert page.find_element(CatalogPageLocators.LEFT_SIDE_BAR_CAMERAS)

        with allure.step("Check for left sidebar tablets element"):
            assert page.find_element(CatalogPageLocators.LEFT_SIDE_BAR_TABLETS)

        with allure.step("Check for left sidebar MP3 players element"):
            assert page.find_element(CatalogPageLocators.LEFT_SIDE_BAR_MP3_PLAYERS)

        with allure.step("Check for left sidebar phones and PDAs element"):
            assert page.find_element(CatalogPageLocators.LEFT_SIDE_BAR_PHONES_AND_PDAS)

        with allure.step("Check for left sidebar software element"):
            assert page.find_element(CatalogPageLocators.LEFT_SIDE_BAR_SOFTWARE)

    @allure.description("Verify product page elements are present")
    @allure.title("Test Product Page Elements")
    def test_product_elements(self, browser, url):
        with allure.step("Open product page for MacBook"):
            browser.get(f"{url}/en-gb/product/macbook")

        page = ProductPage(browser)

        with allure.step("Check for product image element"):
            assert page.find_element(ProductPageLocators.PRODUCT_IMAGE)

        with allure.step("Check for add to cart button"):
            assert page.find_element(ProductPageLocators.BUTTON_ADD_TO_CART)

        with allure.step("Check for quantity input field"):
            assert page.find_element(ProductPageLocators.QUANTITY)

        with allure.step("Check for rating element"):
            assert page.find_element(ProductPageLocators.RATING)

        with allure.step("Check for add to wish list button"):
            assert page.find_element(ProductPageLocators.BUTTON_GROUP_ADD_TO_WISH_LIST)

    @allure.description("Verify admin login page elements are present")
    @allure.title("Test Admin Login Page Elements")
    def test_admin_login_page_elements(self, browser, url):
        with allure.step("Open admin login page"):
            browser.get(f'{url}/administration/')

        page = AdminLoginPage(browser)

        with allure.step("Check for login button"):
            assert page.find_element(AdminLoginPageLocators.LOGIN)

        with allure.step("Check for password field"):
            assert page.find_element(AdminLoginPageLocators.PASSWORD)

        with allure.step("Check for username field"):
            assert page.find_element(AdminLoginPageLocators.USERNAME)

        with allure.step("Check for 'Please enter credentials' info message"):
            assert page.find_element(AdminLoginPageLocators.INFO_PLEASE_ENTER_CREDENTIALS)

    @allure.description("Verify registration page elements are present")
    @allure.title("Test Registration Page Elements")
    def test_registration_page_element(self, browser, url):
        with allure.step("Open registration page"):
            browser.get(f"{url}/en-gb?route=account/register")

        page = RegistrationPage(browser)

        with allure.step("Check for firstname input field"):
            assert page.find_element(RegistrationPageLocators.FIRSTNAME)

        with allure.step("Check for password input field"):
            assert page.find_element(RegistrationPageLocators.PASSWORD)

        with allure.step("Check for email input field"):
            assert page.find_element(RegistrationPageLocators.EMAIL)

        with allure.step("Check for lastname input field"):
            assert page.find_element(RegistrationPageLocators.LASTNAME)

        with allure.step("Check for subscribe checkbox"):
            assert page.find_element(RegistrationPageLocators.SUBSCRIBE)
