from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from pages.home_page import HomePage

def before_all(context):
    print("Test başlıyor...")
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service, options=chrome_options)
    context.driver.implicitly_wait(10)
    context.base_url = "https://www.hepsiburada.com/"
    context.driver.get(context.base_url)
    context.home_page = HomePage(context.driver)

def before_scenario(context, scenario):
    print(f"Senaryo başlıyor: {scenario.name}")
    # context.driver.get(context.base_url) ve context.home_page atamasını kaldırdık
    pass

def after_scenario(context, scenario):
    print(f"Senaryo tamamlandı: {scenario.name}")
    if scenario.status == "failed":
        screenshot_name = f"error_{scenario.name.replace(' ', '_')}_{int(time.time())}.png"
        context.driver.save_screenshot(screenshot_name)
        print(f"Hata ekran görüntüsü kaydedildi: {screenshot_name}")

def after_all(context):
    print("Test tamamlandı.")
    if hasattr(context, 'driver'):
        context.driver.quit() 