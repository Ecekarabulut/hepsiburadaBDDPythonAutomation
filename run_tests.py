#!/usr/bin/env python3
"""
Hepsiburada Test Runner Script
Bu script, Behave testlerini çeşitli seçeneklerle çalıştırmak için kullanılır.
"""

import subprocess
import sys
import os
from datetime import datetime

def run_command(command):
    """Komutu çalıştır ve sonucu döndür"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)

def main():
    print("🚀 Hepsiburada Test Runner")
    print("=" * 50)
    
    # Test seçenekleri
    options = {
        "1": ("Tüm testleri çalıştır", "behave"),
        "2": ("Verbose mod ile çalıştır", "behave -v"),
        "3": ("HTML raporu ile çalıştır", "behave --format=html --outfile=test_report.html"),
        "4": ("JSON raporu ile çalıştır", "behave --format=json --outfile=test_report.json"),
        "5": ("Belirli senaryo çalıştır", "behave --name=\"Ana sayfa yükleme kontrolü\""),
        "6": ("Sadece başarısız testleri çalıştır", "behave --tags=@failed"),
        "7": ("Smoke testleri çalıştır", "behave --tags=@smoke"),
        "8": ("Testleri paralel çalıştır", "behave --processes=4"),
        "9": ("Çıkış", "exit")
    }
    
    while True:
        print("\n📋 Test Seçenekleri:")
        for key, (description, _) in options.items():
            print(f"  {key}. {description}")
        
        choice = input("\nSeçiminizi yapın (1-9): ").strip()
        
        if choice == "9":
            print("👋 Test runner kapatılıyor...")
            break
        
        if choice not in options:
            print("❌ Geçersiz seçim! Lütfen 1-9 arasında bir sayı girin.")
            continue
        
        description, command = options[choice]
        
        if choice == "5":
            scenario_name = input("Senaryo adını girin: ").strip()
            command = f'behave --name="{scenario_name}"'
        
        print(f"\n🔄 {description}...")
        print(f"Komut: {command}")
        print("-" * 50)
        
        start_time = datetime.now()
        success, stdout, stderr = run_command(command)
        end_time = datetime.now()
        
        duration = end_time - start_time
        
        if success:
            print("✅ Testler başarıyla tamamlandı!")
        else:
            print("❌ Testlerde hata oluştu!")
        
        print(f"⏱️  Süre: {duration}")
        
        if stdout:
            print("\n📤 Çıktı:")
            print(stdout)
        
        if stderr:
            print("\n⚠️  Hata:")
            print(stderr)
        
        print("-" * 50)

if __name__ == "__main__":
    # Gerekli paketlerin yüklü olup olmadığını kontrol et
    try:
        import behave
        import selenium
        print("✅ Gerekli paketler yüklü")
    except ImportError as e:
        print(f"❌ Eksik paket: {e}")
        print("Lütfen 'pip install -r requirements.txt' komutunu çalıştırın.")
        sys.exit(1)
    
    main() 