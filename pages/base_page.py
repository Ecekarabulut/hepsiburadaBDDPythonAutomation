from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)
    
    def find_element(self, locator, timeout=10):
        """Element bulma metodu"""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
    
    def find_elements(self, locator, timeout=10):
        """Elementleri bulma metodu"""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )
    
    def click_element(self, locator):
        """Elemente tıklama metodu"""
        element = self.find_element(locator)
        self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def send_keys(self, locator, text):
        """Elemente metin gönderme metodu"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        """Element metnini alma metodu"""
        element = self.find_element(locator)
        return element.text
    
    def is_element_visible(self, locator, timeout=5):
        """Element görünürlüğünü kontrol etme"""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False
    
    def wait_for_page_load(self):
        """Sayfa yüklenmesini bekleme"""
        self.wait.until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )
    
    def scroll_to_element(self, locator):
        """Elemente scroll yapma"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
    
    def hover_element(self, locator):
        """Element üzerine hover yapma"""
        element = self.find_element(locator)
        self.actions.move_to_element(element).perform()
    
    def take_screenshot(self, filename):
        """Ekran görüntüsü alma"""
        self.driver.save_screenshot(filename) 