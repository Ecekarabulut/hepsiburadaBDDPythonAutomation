from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import WebDriverWait

class HomePage(BasePage):
    # Locators
    SEARCH_BOX = (By.CSS_SELECTOR, "input[data-test-id='search-bar-input']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[data-test-id='search-button']")
    LOGIN_BUTTON = (By.ID, "myAccount")
    LOGIN_LINK = (By.ID, "login")
    CART_BUTTON = (By.ID, "shoppingCart")
    CATEGORY_MENU = (By.CSS_SELECTOR, "ul[data-test-id='category-menu']")
    PRODUCT_CARDS = (By.CSS_SELECTOR, "div[data-test-id='product-card']")
    COOKIE_ACCEPT = (By.ID, "onetrust-accept-btn-handler")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def accept_cookies(self, max_retries=3):
        for attempt in range(max_retries):
            try:
                if self.is_element_visible(self.COOKIE_ACCEPT, timeout=5):
                    self.click_element(self.COOKIE_ACCEPT)
                    time.sleep(1)
                    return True
            except (TimeoutException, ElementClickInterceptedException):
                time.sleep(1)
            except Exception:
                time.sleep(1)
        return False
    
    def search_product(self, product_name):
        self.send_keys(self.SEARCH_BOX, product_name)
        self.click_element(self.SEARCH_BUTTON)
    
    def click_login(self):
        self.click_element(self.LOGIN_BUTTON)
    
    def click_login_link(self):
        # Giriş menüsünü aç ve login linkine tıkla
        self.click_element(self.LOGIN_BUTTON)
        time.sleep(1)
        self.click_element(self.LOGIN_LINK)
    
    def click_cart(self):
        self.click_element(self.CART_BUTTON)
    
    def get_category_menu(self):
        return self.find_element(self.CATEGORY_MENU)
    
    def get_product_cards(self):
        return self.find_elements(self.PRODUCT_CARDS)
    
    def is_home_page_loaded(self, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.SEARCH_BOX)
            )
        except Exception:
            return False
    
    def get_page_title(self):
        return self.driver.title 