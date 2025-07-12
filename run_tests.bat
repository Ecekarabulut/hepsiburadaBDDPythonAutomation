@echo off
chcp 65001 >nul
echo 🚀 Hepsiburada Test Runner - Windows
echo ======================================

:menu
echo.
echo 📋 Test Seçenekleri:
echo 1. Tüm testleri çalıştır
echo 2. Verbose mod ile çalıştır
echo 3. HTML raporu ile çalıştır
echo 4. Belirli senaryo çalıştır
echo 5. Python script ile çalıştır
echo 6. Çıkış
echo.

set /p choice="Seçiminizi yapın (1-6): "

if "%choice%"=="1" goto run_all
if "%choice%"=="2" goto run_verbose
if "%choice%"=="3" goto run_html
if "%choice%"=="4" goto run_specific
if "%choice%"=="5" goto run_python
if "%choice%"=="6" goto exit
echo ❌ Geçersiz seçim!
goto menu

:run_all
echo 🔄 Tüm testler çalıştırılıyor...
behave
goto end

:run_verbose
echo 🔄 Verbose mod ile testler çalıştırılıyor...
behave -v
goto end

:run_html
echo 🔄 HTML raporu ile testler çalıştırılıyor...
behave --format=html --outfile=test_report.html
echo ✅ HTML raporu oluşturuldu: test_report.html
goto end

:run_specific
set /p scenario="Senaryo adını girin: "
echo 🔄 Belirli senaryo çalıştırılıyor: %scenario%
behave --name="%scenario%"
goto end

:run_python
echo 🔄 Python script ile çalıştırılıyor...
python run_tests.py
goto end

:end
echo.
echo ⏱️  Test tamamlandı!
pause
goto menu

:exit
echo 👋 Test runner kapatılıyor...
exit 