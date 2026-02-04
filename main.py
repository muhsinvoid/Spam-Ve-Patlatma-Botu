import pyautogui
import time
import sys

# --- HIZ VE GÜVENLİK AYARLARI ---
pyautogui.FAILSAFE = True 
# Tuşlara basma hızını maksimuma çekiyoruz
pyautogui.PAUSE = 0.01 

print("--- WHATSAPP OPTİMİZE EDİLMİŞ HIZLI MOD ---")
print("UYARI: Resim gönderecekseniz, resmi önceden 'Kopyala'mış olmalısınız!")

# 1. Başlangıç Sayacı
print("\nLütfen 5 saniye içinde WhatsApp Web sekmesine geçin...")
time.sleep(5)

# 2. Ayarlar
try:
    print("\nModlar: 1=Sadece Mesaj, 2=Sadece Resim, 3=Karışık (Yazı+Resim)")
    secim = input("Seçiminiz (1/2/3): ")
    grup = input("Grup/Kişi İsmi: ")
    gonderim_sayisi = int(input("Kaç kez gönderilsin: "))
    
    mesaj = ""
    if secim == "1" or secim == "3":
        mesaj = input("Gönderilecek Mesaj: ")

except ValueError:
    print("Hata: Sayı girmeniz gereken yere harf girdiniz.")
    sys.exit()

# 3. Grubu Bul
# Ekranın ortasına tıkla ve arama yap
pyautogui.click(960, 540) 
time.sleep(0.2)
pyautogui.hotkey('ctrl', 'alt', '/') 
time.sleep(0.5)
pyautogui.write(grup)
time.sleep(1.5) # Arama sonuçlarının oturması için bu süre şarttır (kısamazsınız)
pyautogui.press('enter')
time.sleep(1.5) # Sohbetin açılması için bu süre şarttır

# --- OPTİMİZE EDİLMİŞ GÖNDERİM DÖNGÜSÜ ---
print("Gönderim başlıyor...")

for i in range(gonderim_sayisi):
    
    # MOD 1: SADECE MESAJ (Maksimum Hız)
    if secim == "1":
        pyautogui.write(mesaj)
        pyautogui.press('enter')
        # Sadece mesajda bekleme süresine gerek yok, WhatsApp çok hızlı işler.
        
    # MOD 2: SADECE RESİM
    elif secim == "2":
        pyautogui.hotkey('ctrl', 'v') 
        # Resim önizleme penceresinin açılması için gereken minimum süre
        time.sleep(0.8) 
        pyautogui.press('enter')
        time.sleep(0.2) # Mesajın gitmesi için minik ara

    # MOD 3: KARIŞIK (Yazı + Resim) - KRİTİK AYAR BURADA
    elif secim == "3":
        # A) Önce Mesajı Yaz ve Gönder
        if mesaj:
            pyautogui.write(mesaj)
            pyautogui.press('enter')
            
            # Yazı gittikten sonra resim yapıştırma komutunun "yemesi" için
            # çok kısa bir nefes payı bırakıyoruz.
            time.sleep(0.3) 
        
        # B) Resmi Yapıştır
        pyautogui.hotkey('ctrl', 'v')
        
        # C) Resim Yüklenme Beklemesi (En önemli ayar)
        # Bu süre 0.1 olursa resim gitmez. 0.7 - 0.8 en ideal hızlı ayardır.
        # Bilgisayarınız çok hızlıysa 0.6 deneyebilirsiniz ama altı risklidir.
        time.sleep(0.7) 
        
        # D) Resmi Gönder
        pyautogui.press('enter')
        
        # E) Bir sonraki tura geçmeden önce temizlik süresi
        time.sleep(0.2)

print(f"\nİşlem bitti! {gonderim_sayisi} adet gönderim yapıldı.")