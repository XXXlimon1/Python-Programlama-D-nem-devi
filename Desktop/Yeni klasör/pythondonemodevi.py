# --- 1.1 Değişkenler ve Tipler ---

ad_soyad = "Ahmet Yılmaz"          # string  — müşterinin adı soyadı
aylik_ucret = 650.0                 # float   — aylık fatura tutarı (TL)
sadakat_ayi = 30                    # int     — firmada kaldığı ay sayısı
aktif_mi = True                     # boolean — abonelik hâlâ aktif mi?

# Tipleri ekrana yazdıralım
print("===== Müşteri Değişkenleri ve Tipleri =====")
print(f"ad_soyad   : {ad_soyad}   -> Tip: {type(ad_soyad).__name__}")
print(f"aylik_ucret: {aylik_ucret} -> Tip: {type(aylik_ucret).__name__}")
print(f"sadakat_ayi: {sadakat_ayi}    -> Tip: {type(sadakat_ayi).__name__}")
print(f"aktif_mi   : {aktif_mi}  -> Tip: {type(aktif_mi).__name__}")

ad_soyad = "Ahmet Yılmaz"          # string  — müşterinin adı soyadı
aylik_ucret = 650.0                 # float   — aylık fatura tutarı (TL)
sadakat_ayi = 30                    # int     — firmada kaldığı ay sayısı
aktif_mi = True                     # boolean — abonelik hâlâ aktif mi?

# --- 1.2 Liste ve Sözlük Kullanımı ---

# Şirketin sunduğu 5 farklı hizmet (Liste)                        #Liste Kullanımı
hizmetler = [
    "Fiber İnternet",
    "Mobil Hat",
    "Dijital TV",
    "Bulut Depolama",
    "Siber Güvenlik Paketi"
]

# Müşterinin tüm bilgilerini bir Sözlükte saklıyoruz              #Sözlük Kullanımı
musteri = {
    "ad_soyad": ad_soyad,
    "aylik_ucret": aylik_ucret,
    "sadakat_ayi": sadakat_ayi,
    "aktif_mi": aktif_mi,
    "alinan_hizmetler": ["Fiber İnternet", "Mobil Hat", "Dijital TV"]
}

print("===== Şirket Hizmetleri (Liste) ====")
for i, hizmet in enumerate(hizmetler, 1):                          #Döngü Kullanımı
    print(f"  {i}. {hizmet}")

print("\n===== Müşteri Bilgileri (Sözlük) ====")
for anahtar, deger in musteri.items():                              #Döngü Kullanımı
    print(f"  {anahtar:20s} : {deger}")

# --- 1.3 Koşullu İfadeler (If-Else) ---

print("===== VIP Kontrolü =====")

if musteri["aylik_ucret"] > 500 or musteri["sadakat_ayi"] > 24:    #Koşullu İfade
    print("✅ VIP Müşteri: İndirim Tanımla")
else:                                                               #Koşullu İfade
    print("ℹ️ Standart Müşteri")

# --- 1.4 String Operasyonları ---

import random                                                       #Kütüphane İçe Aktarma

# Adı büyük harfe çevirme                                          #String Metodu
ad_buyuk = musteri["ad_soyad"].upper()
print(f"Büyük harfli ad: {ad_buyuk}")

# Rastgele müşteri ID oluşturma                                    #String Formatlama
rastgele_sayi = random.randint(1000, 9999)                          #Random Kullanımı
customer_id = f"IST-2026-{rastgele_sayi}"
print(f"Müşteri ID: {customer_id}")

# --- 2.1 Döngüler ve Listeler ---

# 5 farklı müşterinin sözlük verilerini içeren ana liste             #Liste Kullanımı
musteriler_listesi = [
    {
        "ad_soyad": "Ahmet Yılmaz",                                  #Sözlük Kullanımı
        "aylik_ucret": 650.0,
        "sadakat_ayi": 30,
        "aktif_mi": True,
        "alinan_hizmetler": ["Fiber İnternet", "Mobil Hat", "Dijital TV"]
    },
    {
        "ad_soyad": "Elif Demir",
        "aylik_ucret": 120.0,
        "sadakat_ayi": 3,
        "aktif_mi": False,
        "alinan_hizmetler": ["Mobil Hat"]
    },
    {
        "ad_soyad": "Mehmet Kaya",
        "aylik_ucret": 980.0,
        "sadakat_ayi": 48,
        "aktif_mi": True,
        "alinan_hizmetler": ["Fiber İnternet", "Dijital TV", "Bulut Depolama", "Siber Güvenlik Paketi"]
    },
    {
        "ad_soyad": "Zeynep Arslan",
        "aylik_ucret": 250.0,
        "sadakat_ayi": 6,
        "aktif_mi": True,
        "alinan_hizmetler": ["Mobil Hat", "Fiber İnternet"]
    },
    {
        "ad_soyad": "Can Öztürk",
        "aylik_ucret": 450.0,
        "sadakat_ayi": 12,
        "aktif_mi": False,
        "alinan_hizmetler": ["Fiber İnternet", "Mobil Hat", "Dijital TV"]
    }
]

print(f"Toplam müşteri sayısı: {len(musteriler_listesi)}\n")         #Len Fonksiyonu

# Tüm müşterileri döngüyle listeleme                                 #Döngü Kullanımı
for sira, m in enumerate(musteriler_listesi, 1):                      #Enumerate Kullanımı
    durum = "Aktif" if m["aktif_mi"] else "Pasif"                     #Ternary İfade
    print(f"{sira}. {m['ad_soyad']:20s} | Ücret: {m['aylik_ucret']:>8.2f} TL | "
          f"Sadakat: {m['sadakat_ayi']:>3} ay | Durum: {durum}")

# --- 2.2 Fonksiyon Tanımlama ---

def tutar_hesapla(aylik_ucret):                                       #Fonksiyon Tanımlama
    """
    Aylık ücretin üzerine %20 KDV ekleyip toplam tutarı döndürür.

    Parametre:
        aylik_ucret (float): KDV'siz aylık ücret
    Dönüş:
        float: KDV dahil toplam tutar
    """
    kdv_orani = 0.20                                                  #Değişken Tanımlama
    toplam = aylik_ucret * (1 + kdv_orani)                            #Aritmetik İşlem
    return toplam                                                     #Return İfadesi


# Fonksiyonu test edelim
print("===== KDV Hesaplama Testi =====")
ornek_ucret = 650.0                                                   #Değişken Tanımlama
kdvli_tutar = tutar_hesapla(ornek_ucret)                              #Fonksiyon Çağırma
print(f"KDV'siz: {ornek_ucret:.2f} TL  ->  KDV'li: {kdvli_tutar:.2f} TL")

# --- 2.3 Kütüphane Kullanımı ---

import math                                                           #Kütüphane İçe Aktarma
import datetime                                                       #Kütüphane İçe Aktarma

# Tüm müşterilerin KDV'li fatura toplamını hesapla                   #Döngü Kullanımı
toplam_fatura = 0                                                     #Değişken Tanımlama

print("===== Müşteri Faturaları (KDV Dahil) =====")
for m in musteriler_listesi:                                          #Döngü Kullanımı
    kdvli = tutar_hesapla(m["aylik_ucret"])                           #Fonksiyon Çağırma
    toplam_fatura += kdvli                                            #Toplama İşlemi
    print(f"  {m['ad_soyad']:20s} -> {kdvli:>10.2f} TL")

# math.ceil ile yukarıya yuvarlama                                   #Math Kütüphanesi
yuvarlanmis_toplam = math.ceil(toplam_fatura)                         #Ceil Fonksiyonu
print(f"\nToplam Fatura (ham)       : {toplam_fatura:.2f} TL")
print(f"Toplam Fatura (yuvarlanmış): {yuvarlanmis_toplam} TL")

# datetime ile bugünün tarihini ekleme                                #Datetime Kütüphanesi
bugun = datetime.date.today()                                         #Tarih Alma
print(f"\nFatura Tarihi: {bugun.strftime('%d/%m/%Y')}")

# --- 2.4 Hata Denetimi ve Set Kullanımı ---

# Tüm müşterilerin aldığı hizmetleri tek bir listede topluyoruz      #Liste Kullanımı
# (Aynı hizmet birden fazla müşteride olduğu için tekrar edecek)
tum_hizmetler_tekrarli = []                                           #Boş Liste Oluşturma

for m in musteriler_listesi:                                          #Döngü Kullanımı
    for hizmet in m["alinan_hizmetler"]:                              #İç İçe Döngü
        tum_hizmetler_tekrarli.append(hizmet)                         #Listeye Ekleme

print("===== Tekrarlı Hizmet Listesi =====")
print(tum_hizmetler_tekrarli)
print(f"Toplam eleman sayısı (tekrarlı): {len(tum_hizmetler_tekrarli)}")

# set() ile benzersiz hale getirme                                   #Set Kullanımı
benzersiz_hizmetler = set(tum_hizmetler_tekrarli)                     #Set Dönüşümü

print("\n===== Benzersiz Hizmet Listesi (Set) =====")
for hizmet in sorted(benzersiz_hizmetler):                            #Sıralama
    print(f"  • {hizmet}")
print(f"Benzersiz hizmet sayısı: {len(benzersiz_hizmetler)}")

# --- 2.5 Churn Riski Tespiti ---

def churn_riski_kontrol(musteri):                                     #Fonksiyon Tanımlama
    """
    Bir müşterinin churn (ayrılma) riskinde olup olmadığını belirler.

    Churn riski kriterleri:
      - Abonelik aktif değilse (aktif_mi == False)
      - VEYA sadakat süresi 6 aydan kısa ise
      - VEYA aylık ücret 200 TL'nin altında ise (düşük bağlılık)

    Parametre:
        musteri (dict): Müşteri sözlüğü
    Dönüş:
        bool: True ise churn riski var
    """
    if not musteri["aktif_mi"]:                                       #Koşullu İfade
        return True                                                   #Return İfadesi
    if musteri["sadakat_ayi"] < 6:                                    #Koşullu İfade
        return True
    if musteri["aylik_ucret"] < 200:                                  #Koşullu İfade
        return True
    return False                                                      #Return İfadesi


print("===== Churn Riski Analizi =====")
churn_sayaci = 0                                                      #Değişken Tanımlama

for m in musteriler_listesi:                                          #Döngü Kullanımı
    risk = churn_riski_kontrol(m)                                     #Fonksiyon Çağırma
    if risk:                                                          #Koşullu İfade
        churn_sayaci += 1                                             #Sayaç Artırma
        print(f"  ⚠️  {m['ad_soyad']:20s} -> CHURN RİSKİ VAR "
              f"(Aktif: {m['aktif_mi']}, Sadakat: {m['sadakat_ayi']} ay, "
              f"Ücret: {m['aylik_ucret']:.0f} TL)")
    else:
        print(f"  ✅ {m['ad_soyad']:20s} -> Güvende")

print(f"\nToplam churn riskli müşteri: {churn_sayaci} / {len(musteriler_listesi)}")