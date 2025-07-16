from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

class HomePage(BasePage):
    """
    Hepsiburada ana sayfa işlemleri için Page Object Model sınıfı.
    Ana sayfa elementleri ve işlevleri burada tanımlanır.
    """
    
    # Element locators - Sayfa elementlerinin konumları
    PRODUCT_CARDS = (By.CSS_SELECTOR, "div[data-test-id='product-card']")
    COOKIE_ACCEPT = (By.ID, "onetrust-accept-btn-handler")
    BUTTON_BY_XPATH = (By.XPATH, "//*[@id='container']/main/div/div/section[1]/div/div[2]/div/div[2]")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button[data-test-id='addToCart']")
    BASKET_HEADER_TEXT = (By.CSS_SELECTOR, "span.checkoutui-ProductOnBasketHeader-nOvp_U8bHbLzgKbSUFaz")
    GO_TO_CART_BUTTON = (By.XPATH, "//button[text()='Sepete git']")
    SELECTED_CHECKBOX = (By.ID, "selectedCheckBox")
    BASKET_TOTAL_PRICE = (By.ID, "basket_payedPrice")

    def __init__(self, driver):
        """HomePage sınıfını başlatır ve driver'ı ayarlar."""
        super().__init__(driver)
        self.driver = driver

    def get_page_title(self):
        """Sayfanın başlığını döndürür."""
        return self.driver.title 

    def accept_cookies(self, timeout=10):
        """
        Çerez kabul butonunu bulur ve tıklar.
        Eğer buton yoksa veya zaten kabul edilmişse hata vermez.
        
        Args:
            timeout (int): Butonun görünmesini bekleyecek süre (saniye)
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(self.COOKIE_ACCEPT)
            ).click()
        except Exception:
            pass  # Zaten kapalıysa hata verme 

    def is_home_page_loaded(self, timeout=10):
        """
        Ana sayfanın yüklenip yüklenmediğini kontrol eder.
        Çerez butonunun görünürlüğünü kontrol ederek sayfanın hazır olduğunu doğrular.
        
        Args:
            timeout (int): Elementin görünmesini bekleyecek süre (saniye)
            
        Returns:
            bool: Sayfa yüklendiyse True, aksi halde False
        """
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.COOKIE_ACCEPT)
            )
        except Exception:
            return False 

    def click_button_by_xpath(self, timeout=10):
        """
        Belirtilen XPath ile butona tıklar ve yeni sekmede açar.
        Eğer element bir link ise JavaScript ile yeni sekmede açar,
        değilse Ctrl+Click ile yeni sekmede açmayı simüle eder.
        
        Args:
            timeout (int): Butonun tıklanabilir olmasını bekleyecek süre (saniye)
        """
        button = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self.BUTTON_BY_XPATH)
        )
        driver = self.driver
        original_tabs = driver.window_handles.copy()
        
        # Eğer bir <a> etiketi ise yeni sekmede açmak için
        if button.tag_name == 'a':
            href = button.get_attribute('href')
            driver.execute_script("window.open(arguments[0], '_blank');", href)
        else:
            # Anchor değilse Ctrl+Click ile yeni sekmede açmayı simüle et
            from selenium.webdriver.common.action_chains import ActionChains
            ActionChains(driver).key_down(Keys.CONTROL).click(button).key_up(Keys.CONTROL).perform()
        
        # Yeni sekmeye geçiş
        WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > len(original_tabs))
        driver.switch_to.window(driver.window_handles[-1]) 

    def click_add_to_cart(self, timeout=10):
        """
        'Sepete ekle' butonuna tıklar.
        
        Args:
            timeout (int): Butonun tıklanabilir olmasını bekleyecek süre (saniye)
        """
        button = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON)
        )
        button.click() 

    def is_product_in_basket(self, timeout=10):
        """
        Ürünün sepete eklenip eklenmediğini kontrol eder.
        'Ürün sepetinizde' yazısının görünürlüğünü kontrol eder.
        
        Args:
            timeout (int): Elementin görünmesini bekleyecek süre (saniye)
            
        Returns:
            bool: Ürün sepetteyse True, aksi halde False
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.BASKET_HEADER_TEXT)
            )
            return "Ürün sepetinizde" in element.text
        except Exception:
            return False 

    def click_go_to_cart(self, timeout=10):
        """
        'Sepete git' butonuna tıklar.
        
        Args:
            timeout (int): Butonun tıklanabilir olmasını bekleyecek süre (saniye)
        """
        button = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self.GO_TO_CART_BUTTON)
        )
        button.click() 

    def click_selected_checkbox(self, timeout=10):
        """
        Seçili checkbox'a tıklar.
        
        Args:
            timeout (int): Checkbox'ın tıklanabilir olmasını bekleyecek süre (saniye)
        """
        checkbox = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self.SELECTED_CHECKBOX)
        )
        checkbox.click() 

    def verify_total_price_is_zero(self, timeout=10):
        """
        Sepetteki toplam fiyatın 0,00 TL olup olmadığını kontrol eder.
        
        Args:
            timeout (int): Fiyat elementinin görünmesini bekleyecek süre (saniye)
            
        Returns:
            bool: Fiyat 0,00 ise True, aksi halde False
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.BASKET_TOTAL_PRICE)
            )
            price_text = element.text.strip()
            return "0,00" in price_text
        except Exception:
            return False 