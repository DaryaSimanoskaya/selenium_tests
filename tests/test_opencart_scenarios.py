from pages.AdminLoginPage import AdminLoginPage, AdminLoginPageLocators
from pages.CartPage import CartPageLocators, CartPage
from pages.HomePage import HomePage, HomePageLocators


class TestOpencartScenarios:

    def test_admin_login_logout(self, browser, url):
        browser.get(f"{url}/administration/")
        page = AdminLoginPage(browser)
        page.set_login("user")
        page.set_password("bitnami")
        page.login()
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
        page.logout()
        assert page.find_element(AdminLoginPageLocators.USERNAME)
        assert page.find_element(AdminLoginPageLocators.PASSWORD)
        assert page.find_element(AdminLoginPageLocators.LOGIN)

    def test_add_random_product_to_cart(self, browser, url):
        browser.get(url)
        home_page = HomePage(browser)
        home_page.add_random_product_to_cart()
        assert home_page.find_element(HomePageLocators.ALERT_YOU_ADDED_PRODUCT)
        product_url = home_page.find_elements(HomePageLocators.PRODUCT_URL)[0].get_attribute("href")
        home_page.go_to_shopping_cart()
        assert home_page.find_element(CartPageLocators.ADDED_PRODUCT_URL).get_attribute("href") == product_url
        assert home_page.find_element(CartPageLocators.QUANTITY).get_attribute("size") == "1"
        cart_page = CartPage(browser)
        cart_page.remove_first_item_from_cart()
        assert cart_page.find_element(CartPageLocators.EMPTY_CART)

    def test_change_currency_to_eur_on_homepage(self, browser, url):
        browser.get(url)
        page = HomePage(browser)
        prev_price_new = page.find_element(HomePageLocators.PRICE_NEW).text
        prev_price_old = page.find_element(HomePageLocators.PRICE_OLD).text
        prev_price_tax = page.find_element(HomePageLocators.PRICE_TAX).text
        page.switch_currency_to_euro()
        cur_price_new = page.find_element(HomePageLocators.PRICE_NEW).text
        cur_price_old = page.find_element(HomePageLocators.PRICE_OLD).text
        cur_price_tax = page.find_element(HomePageLocators.PRICE_TAX).text
        assert prev_price_new != cur_price_new
        assert prev_price_old != cur_price_old
        assert prev_price_tax != cur_price_tax

    def test_change_currency_to_pound_sterling_on_catalog(self, browser, url):
        browser.get(f"{url}/en-gb/catalog/desktops")
        page = HomePage(browser)
        prev_price_new = page.find_element(HomePageLocators.PRICE_NEW).text
        prev_price_old = page.find_element(HomePageLocators.PRICE_OLD).text
        prev_price_tax = page.find_element(HomePageLocators.PRICE_TAX).text
        page.switch_currency_to_pound_sterling()
        cur_price_new = page.find_element(HomePageLocators.PRICE_NEW).text
        cur_price_old = page.find_element(HomePageLocators.PRICE_OLD).text
        cur_price_tax = page.find_element(HomePageLocators.PRICE_TAX).text
        assert prev_price_new != cur_price_new
        assert prev_price_old != cur_price_old
        assert prev_price_tax != cur_price_tax
