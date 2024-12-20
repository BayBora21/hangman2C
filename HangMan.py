import tkinter as tk
import random

# Kelime veritabanını dosyadan okuma
def dosyadan_kelime_sec(dosya_adi="kelime_dataset.txt"):
    try:
        with open(dosya_adi, mode="r", encoding="utf-8") as file:
            satirlar = file.readlines()[1:]  # Başlığı atla
            kelime_bilgileri = [satir.strip().split('\t') for satir in satirlar]
            secilen_kelime = random.choice(kelime_bilgileri)
            return {
                "Kelime": secilen_kelime[0],
                "Kategori": secilen_kelime[1],
            }
    except FileNotFoundError:
        print("Dosya bulunamadı!")
        return None

# Küresel değişkenler
secilen_kelime = ""  # Seçilen rastgele kelimeyi tutar
tahmin_edilen_harfler = []  # Kullanıcının tahmin ettiği harflerin listesini tutar
yanlis_tahminler = 0  # Yanlış tahmin sayısını tutar
harf_hakki = 7  # Kullanıcının başlangıçta sahip olduğu harf hakkı

# Oyun başlatma fonksiyonu
def oyunu_baslat():
    global secilen_kelime, tahmin_edilen_harfler, yanlis_tahminler, harf_hakki

    secilen_kelime = dosyadan_kelime_sec()  # Dosyadan rastgele kelime seçilir
    tahmin_edilen_harfler = []  # Tahmin edilen harfler sıfırlanır
    yanlis_tahminler = 0  # Yanlış tahminler sıfırlanır
    harf_hakki = 7  # Harf hakkı 7'ye sıfırlanır
    ekran_guncelle()

    # Başlangıçta butonları aktif hale getir
    tahmin_et_butonu.config(state=tk.NORMAL)
    kelime_tahmin_et_butonu.config(state=tk.NORMAL)
    bitir_butonu.config(state=tk.NORMAL)
    yeni_oyun_butonu.config(state=tk.DISABLED)
    oyun_bilgisi_paneli.pack_forget()  # Başlangıç panelini gizle
    oyun_paneli.pack()  # Oyun panelini göster

    # Pencereyi büyüt
    root.geometry("800x800")

# Ekranı güncelleme fonksiyonu
def ekran_guncelle():
    # Kelimeyi harf harf aralarında boşluk olacak şekilde göster
    gorunen_kelime = ' '.join([harf if harf in tahmin_edilen_harfler else '_' for harf in secilen_kelime["Kelime"]])
    kelime_etiketi.config(text=gorunen_kelime)
    yanlis_tahmin_etiketi.config(text=f"Yanlış Tahminler: {yanlis_tahminler}")
    harf_hakki_etiketi.config(text=f"Kalan Harf Hakkınız: {harf_hakki}")
    kategori_etiketi.config(text=f"Kategori: {secilen_kelime['Kategori']}")  # Kategori bilgisi gösteriliyor

    # Hangman adam resmi (yanlış tahminlere göre güncellenir)
    hangman_resimleri = [
        '',  # 0 yanlış tahmin: hiç bir şey yok
        'O',  # 1 yanlış tahmin: kafa
        'O\n|',  # 2 yanlış tahmin: kafa + gövde
        'O\n|\n/',  # 3 yanlış tahmin: kafa + gövde + sağ kol
        'O\n|\n/\\',  # 4 yanlış tahmin: kafa + gövde + kollar
        'O\n|\n/\\\n|',  # 5 yanlış tahmin: kafa + gövde + kollar + bacak
        'O\n|\n/\\\n|\\',  # 6 yanlış tahmin: kafa + gövde + kollar + bacak
        'O\n|\n/\\\n|\\/\\'  # 7 yanlış tahmin: tam hangman
    ]
    hangman_etiketi.config(text=hangman_resimleri[yanlis_tahminler] if yanlis_tahminler < len(hangman_resimleri) else "Game Over!")
    
    # Oyun bitti mi kontrolü
    if yanlis_tahminler >= len(hangman_resimleri):
        sonuc_etiketi.config(text="Kaybettiniz! Yeni Oyun Başlatın.")
        tahmin_et_butonu.config(state=tk.DISABLED)  # Buton devre dışı bırakılır

    elif all(harf in tahmin_edilen_harfler for harf in secilen_kelime["Kelime"]):
        sonuc_etiketi.config(text="Tebrikler! Kazandınız!")
        tahmin_et_butonu.config(state=tk.DISABLED)  # Buton devre dışı bırakılır

    # Eğer harf hakkı bitmişse, oyun bitir
    if harf_hakki == 0:
        sonuc_etiketi.config(text="Harf Hakkınız Bitti! Yeni Oyun Başlatın.")
        tahmin_et_butonu.config(state=tk.DISABLED)  # Buton devre dışı bırakılır

# Kullanıcıdan harf tahmini alma fonksiyonu
def harf_tahmin_et():
    global yanlis_tahminler, harf_hakki
    tahmin = tahmin_girisi.get().lower()  # Kullanıcının girdiği harfi alır ve küçük harfe çevirir
    
    # Geçerli bir tahmin yapıldıysa (tek harf ve daha önce tahmin edilmediyse)
    if tahmin and len(tahmin) == 1 and tahmin not in tahmin_edilen_harfler:
        tahmin_edilen_harfler.append(tahmin)  # Tahmin edilen harfler listesine eklenir
        if tahmin not in secilen_kelime["Kelime"]:
            yanlis_tahminler += 1  # Yanlış tahmin sayısı artırılır
            harf_hakki -= 1  # Harf hakkı bir azalır
        ekran_guncelle()  # Ekran güncellenir

    tahmin_girisi.delete(0, tk.END)  # Giriş kutusu temizlenir

# Kullanıcıdan kelime tahmini alma fonksiyonu
def kelime_tahmin_et():
    global yanlis_tahminler, harf_hakki
    tahmin = kelime_tahmin_girisi.get().lower()  # Kullanıcının girdiği kelimeyi alır
    
    # Geçerli bir tahmin (kelime) yapıldıysa
    if tahmin and len(tahmin) == len(secilen_kelime["Kelime"]):
        if tahmin == secilen_kelime["Kelime"]:
            sonuc_etiketi.config(text="Tebrikler! Kazandınız!")
            tahmin_et_butonu.config(state=tk.DISABLED)  # Buton devre dışı bırakılır
            kelime_tahmin_et_butonu.config(state=tk.DISABLED)  # Kelime tahmin butonu devre dışı bırakılır
        else:
            yanlis_tahminler += 1  # Yanlış tahmin sayısı artırılır
            harf_hakki -= 1  # Harf hakkı bir azalır
            ekran_guncelle()  # Ekran güncellenir
    
    kelime_tahmin_girisi.delete(0, tk.END)  # Giriş kutusu temizlenir

# Oyunu bitirme fonksiyonu
def oyunu_bitir():
    global harf_hakki
    sonuc_etiketi.config(text="Oyunu Bitirdiniz. Yeni Oyun Başlatın.")
    tahmin_et_butonu.config(state=tk.DISABLED)  # Buton devre dışı bırakılır
    kelime_tahmin_et_butonu.config(state=tk.DISABLED)  # Kelime tahmin butonu devre dışı bırakılır
    yeni_oyun_butonu.config(state=tk.NORMAL)  # Yeni oyun butonu aktif edilir
    harf_hakki = 0  # Harf hakkı sıfırlanır

# Yeni oyun başlatma fonksiyonu
def yeni_oyun_baslat():
    oyunu_baslat()  # Yeni oyun başlatılır
    yeni_oyun_butonu.config(state=tk.DISABLED)  # Yeni oyun butonu devre dışı bırakılır
    bitir_butonu.config(state=tk.NORMAL)  # Bitir butonu aktif edilir

# Ana pencereyi oluşturuyoruz
root = tk.Tk()
root.title("Hangman Oyunu")
root.configure(bg="#000000")  # Arka plan rengini siyah

# Pencere boyutunu ayarlıyoruz
root.geometry("600x600")  # Başlangıçta daha küçük bir pencere

# Başlangıçta gösterilecek panel (oyun bilgisi)
oyun_bilgisi_paneli = tk.Frame(root, bg="#000000")
oyun_bilgisi_paneli.pack(pady=30)

# Yeni oyun başlatma butonu
baslat_butonu = tk.Button(oyun_bilgisi_paneli, text="Oyunu Başlat", command=oyunu_baslat, font=('Arial', 18), bg="#4CAF50", fg="white", width=20, height=2, relief="solid", bd=2)
baslat_butonu.pack()

# Diğer oyun panelini oluşturuyoruz ve başlangıçta gizliyoruz
oyun_paneli = tk.Frame(root, bg="#000000")

# Kelimeyi ve tahminleri gösteren etiket
kelime_etiketi = tk.Label(oyun_paneli, text="", font=('Arial', 36), bg="#000000", fg="#FFFFFF", width=20)
kelime_etiketi.pack(pady=20)

# Kategori etiketini ekliyoruz
kategori_etiketi = tk.Label(oyun_paneli, text="", font=('Arial', 18), bg="#000000", fg="#98FB98")
kategori_etiketi.pack(pady=10)

# Yanlış tahminleri gösteren etiket
yanlis_tahmin_etiketi = tk.Label(oyun_paneli, text="Yanlış Tahminler: 0", font=('Arial', 18), bg="#000000", fg="#FFB6C1")
yanlis_tahmin_etiketi.pack(pady=10)

# Harf hakkı etiketini ekliyoruz
harf_hakki_etiketi = tk.Label(oyun_paneli, text="Kalan Harf Hakkınız: 7", font=('Arial', 18), bg="#000000", fg="#ADD8E6")
harf_hakki_etiketi.pack(pady=10)

# Hangman adam resmi
hangman_etiketi = tk.Label(oyun_paneli, text="", font=('Arial', 24), bg="#000000", fg="white")
hangman_etiketi.pack(pady=20)

# Kullanıcı tahmini için giriş kutusu (harf)
tahmin_girisi = tk.Entry(oyun_paneli, font=('Arial', 18), width=10)
tahmin_girisi.pack(pady=10)

# Tahmin etme butonu (harf)
tahmin_et_butonu = tk.Button(oyun_paneli, text="Tahmin Et (Harf)", command=harf_tahmin_et, state=tk.DISABLED, font=('Arial', 18), bg="#B0E0E6", fg="black", width=20, height=2)
tahmin_et_butonu.pack(pady=10)

# Kullanıcı tahmini için giriş kutusu (kelime)
kelime_tahmin_girisi = tk.Entry(oyun_paneli, font=('Arial', 18), width=15)
kelime_tahmin_girisi.pack(pady=10)

# Kelime tahmin etme butonu
kelime_tahmin_et_butonu = tk.Button(oyun_paneli, text="Tahmin Et (Kelime)", command=kelime_tahmin_et, state=tk.DISABLED, font=('Arial', 18), bg="#FFB6C1", fg="black", width=20, height=2)
kelime_tahmin_et_butonu.pack(pady=10)

# Sonuç etiketleri
sonuc_etiketi = tk.Label(oyun_paneli, text="", font=('Arial', 18), bg="#000000", fg="white")
sonuc_etiketi.pack(pady=20)

# Bitirme butonu
bitir_butonu = tk.Button(oyun_paneli, text="Oyunu Bitir", command=oyunu_bitir, state=tk.DISABLED, font=('Arial', 18), bg="#FAD02E", fg="black", width=20, height=2)
bitir_butonu.pack(pady=20)

# Yeni oyun başlatma butonu
yeni_oyun_butonu = tk.Button(oyun_paneli, text="Yeni Oyun Başlat", command=yeni_oyun_baslat, state=tk.DISABLED, font=('Arial', 18), bg="#98FB98", fg="black", width=20, height=2)
yeni_oyun_butonu.pack(pady=10)

# Pencereyi başlat
root.mainloop()
