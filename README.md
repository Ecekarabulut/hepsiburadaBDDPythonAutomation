# 🛒 Hepsiburada Web Otomasyon Projesi

Bu proje, modern web otomasyon teknolojileri kullanarak Hepsiburada e-ticaret sitesi için kapsamlı test otomasyonu sağlar. BDD (Behavior Driven Development) yaklaşımı ile geliştirilmiş, sürdürülebilir ve ölçeklenebilir bir test framework'ü sunar.

## 🚀 Teknoloji Stack'i

### 🐍 **Core Technologies**
- **Python 3.7+** - Ana programlama dili
- **Behave 1.2.6+** - BDD framework (Cucumber benzeri)
- **Selenium 4.15.0+** - Web otomasyon kütüphanesi

### 🧪 **Testing & Automation**
- **WebDriver Manager 4.0.0+** - Otomatik driver yönetimi
- **Pytest 7.4.0+** - Test framework
- **Pytest-HTML 4.1.0+** - HTML raporlama
- **Allure-Behave 2.13.0+** - Gelişmiş test raporlama

### 🏗️ **Design Patterns & Architecture**
- **Page Object Model (POM)** - Sürdürülebilir kod yapısı
- **BDD (Behavior Driven Development)** - İş odaklı test yaklaşımı
- **Gherkin Syntax** - Okunabilir test senaryoları

### 🌐 **Browser & Driver Management**
- **Chrome WebDriver** - Tarayıcı otomasyonu
- **Headless Mode Support** - CI/CD uyumluluğu
- **Cross-platform Compatibility** - Windows, macOS, Linux

### 📊 **Reporting & Monitoring**
- **HTML Reports** - Detaylı test raporları
- **JSON Reports** - API entegrasyonu için
- **Allure Reports** - Görsel test analizi
- **Screenshot Capture** - Hata durumunda görsel kanıt

## 🎯 Proje Özellikleri

- ✅ **Selenium WebDriver** ile Chrome tarayıcı otomasyonu
- ✅ **Behave (Cucumber)** ile BDD yaklaşımı
- ✅ **Page Object Model** tasarım deseni
- ✅ **Türkçe** test senaryoları
- ✅ Otomatik ChromeDriver yönetimi
- ✅ Hata durumunda ekran görüntüsü alma
- ✅ Çerez kabul etme otomasyonu
- ✅ Cross-platform uyumluluk
- ✅ CI/CD pipeline entegrasyonu hazır
- ✅ Detaylı raporlama sistemi

## 📋 Gereksinimler

- Python 3.7+
- Chrome tarayıcı
- pip (Python paket yöneticisi)

## 🛠️ Kurulum

1. **Projeyi klonlayın:**
```bash
git clone <repository-url>
cd Example2
```

2. **Gerekli paketleri yükleyin:**
```bash
pip install -r requirements.txt
```

3. **Chrome tarayıcısının yüklü olduğundan emin olun**

## 🏃‍♂️ Testleri Çalıştırma

### Tüm testleri çalıştırma:
```bash
behave
```

### Belirli bir senaryo çalıştırma:
```bash
behave --name="Ana sayfa yükleme kontrolü"
```

### HTML raporu ile çalıştırma:
```bash
behave --format=html --outfile=test_report.html
```

### Verbose mod ile çalıştırma:
```bash
behave -v
```

### Belirli tag'leri çalıştırma:
```bash
behave --tags=@smoke
```

## 📁 Proje Yapısı

```
Example2/
├── features/
│   ├── hepsiburada.feature    # Test senaryoları (Gherkin)
│   └── steps/
│       └── hepsiburada_steps.py  # Step definitions
├── pages/
│   ├── base_page.py           # Temel sayfa sınıfı
│   ├── home_page.py           # Ana sayfa
│   └── search_results_page.py # Arama sonuçları sayfası
├── environment.py             # Behave hooks
├── behave.ini                 # Behave konfigürasyonu
├── requirements.txt           # Python bağımlılıkları
└── README.md                  # Bu dosya
```

## 🧪 Test Senaryoları

### Mevcut Test Senaryoları:

1. **Ana sayfa yükleme kontrolü** - Sayfanın doğru yüklendiğini kontrol eder
2. **Ürün arama işlemi** - Ürün arama fonksiyonunu test eder
3. **Ürün arama - sonuç bulunamadı** - Geçersiz arama sonuçlarını test eder
4. **Ürün detay sayfasına gitme** - Ürün detay sayfasına erişimi test eder
5. **Sepete ürün ekleme** - Sepete ürün ekleme işlemini test eder
6. **Fiyat sıralama** - Fiyat sıralama fonksiyonunu test eder
7. **Kategori menüsü kontrolü** - Kategori menüsünün görünürlüğünü test eder
8. **Giriş yap butonu kontrolü** - Giriş butonunun görünürlüğünü test eder
9. **Sepet butonu kontrolü** - Sepet butonunun görünürlüğünü test eder
10. **Çerez kabul etme** - Çerez kabul etme işlemini test eder

## 🔧 Konfigürasyon

### behave.ini
```ini
[behave]
default_tags = ~@skip
```

### environment.py
- Chrome tarayıcı ayarları
- WebDriver başlatma
- Hata durumunda ekran görüntüsü alma
- Her senaryo öncesi ana sayfaya gitme

## 📊 Raporlama

Test sonuçları aşağıdaki formatlarda alınabilir:

- **Konsol çıktısı** (varsayılan)
- **HTML raporu** (`--format=html`)
- **JSON raporu** (`--format=json`)
- **Allure raporu** (Allure kurulu ise)

## 🐛 Sorun Giderme

### Yaygın Sorunlar:

1. **ChromeDriver hatası:**
   - Chrome tarayıcısının güncel olduğundan emin olun
   - `webdriver-manager` otomatik olarak uygun driver'ı indirecektir

2. **Element bulunamadı hatası:**
   - Sayfa yüklenme sürelerini kontrol edin
   - Locator'ları güncelleyin (site değişiklikleri olabilir)

3. **Timeout hatası:**
   - İnternet bağlantınızı kontrol edin
   - `environment.py` dosyasındaki timeout değerlerini artırın

## 🤝 Katkıda Bulunma

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/AmazingFeature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some AmazingFeature'`)
4. Branch'inizi push edin (`git push origin feature/AmazingFeature`)
5. Pull Request oluşturun

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

## 📞 İletişim

Sorularınız için issue açabilir veya iletişime geçebilirsiniz. 