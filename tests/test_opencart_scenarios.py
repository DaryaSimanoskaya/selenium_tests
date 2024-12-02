from datetime import datetime

import allure
from selenium.webdriver.common.by import By

from pages.AdminLoginPage import AdminLoginPage, AdminLoginPageLocators
from pages.AdminPage import AdminPage, AdminPageLocators
from pages.CartPage import CartPageLocators, CartPage
from pages.HomePage import HomePage, HomePageLocators
from pages.RegistrationPage import RegistrationPage, RegistrationPageLocators


class TestOpencartScenarios:

    @allure.description("Test admin login and logout functionality")
    def test_admin_login_logout(self, browser, admin_url):
        browser.get(admin_url)
        page = AdminLoginPage(browser)

        with allure.step("Enter admin credentials"):
            page.set_login("user")
            page.set_password("bitnami")
            page.login()
        if not page.element_is_exists(AdminLoginPageLocators.EXTENSIONS):
            with allure.step("Enter admin credentials try number two"):
                page.set_login("user")
                page.set_password("bitnami")
                page.login()
        with allure.step("Verify admin panel elements are visible"):
            assert page.find_element(AdminLoginPageLocators.EXTENSIONS)
            assert page.find_element(AdminLoginPageLocators.CATALOG)
            assert page.find_element(AdminLoginPageLocators.CUSTOMERS)
            assert page.find_element(AdminLoginPageLocators.DESIGN)
            assert page.find_element(AdminLoginPageLocators.MARKETING)
            assert page.find_element(AdminLoginPageLocators.NAVIGATION)
            assert page.find_element(AdminLoginPageLocators.SYSTEM)
            assert page.find_element(AdminLoginPageLocators.REPORTS)
            assert page.find_element(AdminLoginPageLocators.SALES)
            assert page.find_element(AdminLoginPageLocators.SALES_ANALYTICS)

        with allure.step("Logout from admin panel"):
            page.logout()

        with allure.step("Verify login page is displayed"):
            assert page.find_element(AdminLoginPageLocators.USERNAME)
            assert page.find_element(AdminLoginPageLocators.PASSWORD)
            assert page.find_element(AdminLoginPageLocators.LOGIN)

    @allure.description("Test adding a random product to the cart")
    def test_add_random_product_to_cart(self, browser, url):
        with allure.step("Open homepage"):
            browser.get(url)

        home_page = HomePage(browser)
        home_page.driver.refresh()
        with allure.step("Add a random product to the cart"):
            home_page.add_random_product_to_cart()
            assert home_page.find_element(HomePageLocators.ALERT_YOU_ADDED_PRODUCT)
            product_url = home_page.find_elements(HomePageLocators.PRODUCT_URL)[0].get_attribute("href")

        with allure.step("Go to shopping cart"):
            home_page.go_to_shopping_cart()
            assert home_page.find_element(CartPageLocators.ADDED_PRODUCT_URL).get_attribute("href") == product_url
            assert home_page.find_element(CartPageLocators.QUANTITY).get_attribute("size") == "1"

        cart_page = CartPage(browser)

        with allure.step("Remove the first item from the cart"):
            cart_page.remove_first_item_from_cart()
            assert cart_page.find_element(CartPageLocators.EMPTY_CART)

    @allure.description("Test changing currency to EUR on the homepage")
    def test_change_currency_to_eur_on_homepage(self, browser, url):
        with allure.step("Open homepage"):
            browser.get(url)

        page = HomePage(browser)

        with allure.step("Capture current prices"):
            prev_price_new = page.find_element(HomePageLocators.PRICE_NEW).text
            prev_price_old = page.find_element(HomePageLocators.PRICE_OLD).text
            prev_price_tax = page.find_element(HomePageLocators.PRICE_TAX).text

        with allure.step("Switch currency to EUR"):
            page.switch_currency_to_euro()

        with allure.step("Verify prices have changed"):
            cur_price_new = page.find_element(HomePageLocators.PRICE_NEW).text
            cur_price_old = page.find_element(HomePageLocators.PRICE_OLD).text
            cur_price_tax = page.find_element(HomePageLocators.PRICE_TAX).text
            assert prev_price_new != cur_price_new
            assert prev_price_old != cur_price_old
            assert prev_price_tax != cur_price_tax

    @allure.description("Test changing currency to GBP on the catalog page")
    def test_change_currency_to_pound_sterling_on_catalog(self, browser, url):
        with allure.step("Open catalog page for desktops"):
            browser.get(f"{url}/en-gb/catalog/desktops")

        page = HomePage(browser)

        with allure.step("Capture current prices"):
            prev_price_new = page.find_element(HomePageLocators.PRICE_NEW).text
            prev_price_old = page.find_element(HomePageLocators.PRICE_OLD).text
            prev_price_tax = page.find_element(HomePageLocators.PRICE_TAX).text

        with allure.step("Switch currency to GBP"):
            page.switch_currency_to_pound_sterling()

        with allure.step("Verify prices have changed"):
            cur_price_new = page.find_element(HomePageLocators.PRICE_NEW).text
            cur_price_old = page.find_element(HomePageLocators.PRICE_OLD).text
            cur_price_tax = page.find_element(HomePageLocators.PRICE_TAX).text
            assert prev_price_new != cur_price_new
            assert prev_price_old != cur_price_old
            assert prev_price_tax != cur_price_tax

    @allure.description("Test adding a new product in the admin panel")
    def test_add_new_product(self, browser, admin_url, administrator_login_token, delete_product):
        rand = f'{datetime.now():%Y%m%d-%H%M%S%z}'
        product_name = f"Test product name {rand}"
        meta_tag = f"Test meta tag {rand}"
        model = f"Test model {rand}"
        keyword = f"test_keyword_{rand}"

        with allure.step("Open admin product page"):
            browser.get(f"{admin_url}/index.php?route=catalog/product&user_token={administrator_login_token}")

        admin_page = AdminPage(browser)

        with allure.step("Add a new product"):
            admin_page.add_new_product(name=product_name, meta_tag=meta_tag, model=model, keyword=keyword)
            browser.get(f"{admin_url}/index.php?route=catalog/product&user_token={administrator_login_token}")
            admin_page.go_to_last_product()

        with allure.step("Verify the product was added"):
            created_product_id = admin_page.wait_element_with_retry(AdminPageLocators.CHECKBOX).get_attribute('value')
            delete_product(created_product_id)
            assert (admin_page.wait_element_with_retry(locator=(By.XPATH,
                                                                f"//form[@id='form-product']//tbody//tr[last()]/td[3]"))
            .text.split("\n")[0]) == product_name
            assert (admin_page.wait_for_element(
                locator=(By.XPATH, f"//form[@id='form-product']//tbody//tr[last()]/td[4]"))
                    .text) == model

    @allure.description("Test deleting a product from the admin panel")
    def test_delete_product_from_admin(self, browser, admin_url, administrator_login_token):
        with allure.step("Open admin product page"):
            browser.get(f"{admin_url}/index.php?route=catalog/product&user_token={administrator_login_token}")

        admin_page = AdminPage(browser)

        with allure.step("Add a new product"):
            admin_page.add_new_product()

        with allure.step("Open admin product page again"):
            browser.get(f"{admin_url}/index.php?route=catalog/product&user_token={administrator_login_token}")

        with allure.step("Delete the last added product"):
            admin_page.go_to_last_product()
            created_product_id = admin_page.wait_element_with_retry(AdminPageLocators.CHECKBOX).get_attribute('value')
            admin_page.delete_product(value=created_product_id)
            assert admin_page.find_element(AdminPageLocators.ALERT_DELETE_PRODUCT_SUCCESS)

        with allure.step("Verify the product was deleted"):
            checkbox = (By.XPATH, f"//input[@value='{created_product_id}']")
            assert admin_page.wait_until_element_is_not_visible(checkbox)

    @allure.description("Test registering a new user account")
    def test_register_new_account(self, browser, url):
        with allure.step("Open homepage"):
            browser.get(url)

        registration_page = RegistrationPage(browser)

        with allure.step("Register a new user"):
            registration_page.register_new_user()

        with allure.step("Verify registration completion"):
            assert registration_page.find_element(RegistrationPageLocators.END_REGISTRATION)