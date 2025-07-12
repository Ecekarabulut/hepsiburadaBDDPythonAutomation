from selenium.webdriver.common.by import By
from .base_page import BasePage

class SearchResultsPage(BasePage):
    # Locators
    SEARCH_RESULTS = (By.CSS_SELECTOR, "div[data-test-id='product-card']")
    PRODUCT_TITLES = (By.CSS_SELECTOR, "h3[data-test-id='product-card-name']")
    PRODUCT_PRICES = (By.CSS_SELECTOR, "span[data-test-id='price-current-price']")
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, "button[data-test-id='add-to-cart-button']")
    FILTER_SIDEBAR = (By.CSS_SELECTOR, "div[data-test-id='filter-sidebar']")
    SORT_DROPDOWN = (By.CSS_SELECTOR, "select[data-test-id='sort-dropdown']")
    NO_RESULTS_MESSAGE = (By.CSS_SELECTOR, "div[data-test-id='no-results-message']")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def get_search_results_count(self):
        """Arama sonuçlarının sayısını al"""
        results = self.find_elements(self.SEARCH_RESULTS)
        return len(results)
    
    def get_product_titles(self):
        """Ürün başlıklarını al"""
        titles = self.find_elements(self.PRODUCT_TITLES)
        return [title.text for title in titles]
    
    def get_product_prices(self):
        """Ürün fiyatlarını al"""
        prices = self.find_elements(self.PRODUCT_PRICES)
        return [price.text for price in prices]
    
    def click_first_product(self):
        """İlk ürüne tıkla"""
        first_product = self.find_elements(self.SEARCH_RESULTS)[0]
        first_product.click()
    
    def add_first_product_to_cart(self):
        """İlk ürünü sepete ekle"""
        add_buttons = self.find_elements(self.ADD_TO_CART_BUTTONS)
        if add_buttons:
            add_buttons[0].click()
    
    def is_filter_sidebar_visible(self):
        """Filtre kenar çubuğu görünür mü"""
        return self.is_element_visible(self.FILTER_SIDEBAR)
    
    def sort_by_price_low_to_high(self):
        """Fiyata göre düşükten yükseğe sırala"""
        if self.is_element_visible(self.SORT_DROPDOWN):
            self.click_element(self.SORT_DROPDOWN)
            # Fiyat düşükten yükseğe seçeneğini seç
            low_to_high_option = (By.CSS_SELECTOR, "option[value='price-asc']")
            self.click_element(low_to_high_option)
    
    def is_no_results_found(self):
        """Sonuç bulunamadı mesajı var mı"""
        return self.is_element_visible(self.NO_RESULTS_MESSAGE)
    
    def get_search_results_info(self):
        """Arama sonuçları bilgisini al"""
        info = {
            'count': self.get_search_results_count(),
            'titles': self.get_product_titles()[:5],  # İlk 5 ürün
            'prices': self.get_product_prices()[:5]   # İlk 5 fiyat
        }
        return info 