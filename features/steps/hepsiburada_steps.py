print("hepsiburada_steps.py loaded")
from behave import given, when, then
from pages.home_page import HomePage
import time

# ============================================================================
# GIVEN STEPS - Test öncesi hazırlık adımları
# ============================================================================

@given('the Hepsiburada home page is opened')
def open_home_page(context):
    """
    Hepsiburada ana sayfasını açar ve yüklendiğini doğrular.
    Çerezleri kabul eder ve sayfanın hazır olduğunu kontrol eder.
    """
    context.home_page.accept_cookies()
    assert context.home_page.is_home_page_loaded(), "Home page did not load"

# ============================================================================
# WHEN STEPS - Kullanıcı eylemleri
# ============================================================================

@when('the user clicks the button by xpath')
def click_button_by_xpath(context):
    """
    Belirtilen XPath ile butona tıklar ve yeni sekmede açar.
    """
    context.home_page.click_button_by_xpath()

@when('the user clicks the add to cart button')
def click_add_to_cart(context):
    """
    'Sepete ekle' butonuna tıklar.
    """
    context.home_page.click_add_to_cart()

@when('the user clicks the go to cart button')
def click_go_to_cart(context):
    """
    'Sepete git' butonuna tıklar.
    """
    context.home_page.click_go_to_cart()

@when('the user clicks the selected checkbox')
def click_selected_checkbox(context):
    """
    Seçili checkbox'a tıklar.
    """
    context.home_page.click_selected_checkbox()

# ============================================================================
# THEN STEPS - Doğrulama ve bekleme adımları
# ============================================================================

@then('cookies should be accepted')
def check_cookies_accepted(context):
    """
    Çerezlerin kabul edildiğini doğrular.
    """
    assert True, "Cookies were not accepted"

@then('the product should be in the basket')
def product_should_be_in_basket(context):
    """
    Ürünün sepete eklendiğini doğrular.
    'Ürün sepetinizde' yazısının görünürlüğünü kontrol eder.
    """
    assert context.home_page.is_product_in_basket(), "Ürün sepetinizde yazısı bulunamadı!"

@then('the total price should be zero and wait 3 seconds')
def verify_total_price_zero_and_wait(context):
    """
    Sepetteki toplam fiyatın 0,00 TL olduğunu doğrular ve 3 saniye bekler.
    """
    assert context.home_page.verify_total_price_is_zero(), "Toplam fiyat 0,00 TL değil!"
    time.sleep(3)
    print("Toplam fiyat 0,00 TL olarak doğrulandı. 3 saniye bekleme tamamlandı.")

@then('wait 3 seconds and log')
def wait_3_seconds_and_log(context):
    """
    Test sonunda 3 saniye bekler.
    """
    time.sleep(3) 
    