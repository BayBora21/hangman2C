import tkinter as tk
import random

import os
import sys
dosya_adi = "kelimeler.txt"  # Kelimelerin olduğu dosya adı
secilen_kelime = kelime_sec(dosya_adi)
gorunur_kelime = ["_" for _ in secilen_kelime]
yanlis_tahminler = 0
maksimum_hak = 7
toplam_puan = 0  # Puanlama için başlangıç değeri


def kelime_sec(dosya_adi):
    try:
        with open(dosya_adi, "r", encoding="utf-8") as dosya:
            kelimeler = dosya.read().splitlines()
        return random.choice(kelimeler).lower()
    except FileNotFoundError:
        messagebox.showerror("Hata", "Kelimeler dosyası bulunamadı!")
        exit()

---------------------------------------------------------------------------------------------------------------------------

import tkinter as tk
from tkinter import messagebox
import random

# ---- Veri Kaynağı: Kelimeler bir dosyadan seçilecek ----
def kelime_sec(dosya_adi):
    try:
        with open(dosya_adi, "r", encoding="utf-8") as dosya:
            kelimeler = dosya.read().splitlines()
        return random.choice(kelimeler).lower()
    except FileNotFoundError:
        messagebox.showerror("Hata", "Kelimeler dosyası bulunamadı!")
        exit()

# ---- Rastgele Bir Kelime Seç ----
dosya_adi = "kelimeler.txt"  # Kelimelerin olduğu dosya adı
secilen_kelime = kelime_sec(dosya_adi)
gorunur_kelime = ["_" for _ in secilen_kelime]
yanlis_tahminler = 0
maksimum_hak = 7
toplam_puan = 0  # Puanlama için başlangıç değeri

# ---- Puanlama Sistemine Ait Sabitler ----
PUAN_HARF_DOGRU = 10
PUAN_HARF_YANLIS = -5
PUAN_BONUS_CAN = 5
PUAN_KELIME_BONUS = 10

# ---- Puanlama Fonksiyonları ----
def puan_guncelle(dogru_tahmin):
    global toplam_puan
    if dogru_tahmin:
        toplam_puan += PUAN_HARF_DOGRU
    else:
        toplam_puan += PUAN_HARF_YANLIS

def nihai_puan_hesapla(kalan_canlar, kelime_uzunlugu):
    global toplam_puan
    bonus_puan = kalan_canlar * PUAN_BONUS_CAN
    bonus_puan += kelime_uzunlugu * PUAN_KELIME_BONUS
    toplam_puan += bonus_puan
    return toplam_puan

# ---- Harf Güncelleme ----
def harf_tahmin_et():
    global yanlis_tahminler, secilen_kelime, gorunur_kelime, maksimum_hak, toplam_puan
    harf = giris.get().lower()
    if len(harf) != 1 or not harf.isalpha():
        messagebox.showerror("Hata", "Lütfen sadece bir harf girin!")
        return

    if harf in gorunur_kelime:
        messagebox.showinfo("Uyarı", f"'{harf}' harfini zaten tahmin ettiniz!")
        return

    if harf in secilen_kelime:
        for i, karakter in enumerate(secilen_kelime):
            if karakter == harf:
                gorunur_kelime[i] = harf
        puan_guncelle(True)  # PUAN GÜNCELLEME (DOĞRU TAHMİN)
    else:
        yanlis_tahminler += 1
        puan_guncelle(False)  # PUAN GÜNCELLEME (YANLIŞ TAHMİN)

    # GUI güncellemesi
    kelime_label.config(text=" ".join(gorunur_kelime))
    puan_label.config(text=f"Puan: {toplam_puan}")
    hak_label.config(text=f"Kalan Hak: {maksimum_hak - yanlis_tahminler}")

    # Oyun Durumu Kontrolü
    if "_" not in gorunur_kelime:
        final_puan = nihai_puan_hesapla(maksimum_hak - yanlis_tahminler, len(secilen_kelime))
        messagebox.showinfo("Tebrikler!", f"Kelimeyi buldunuz! Nihai puanınız: {final_puan}")
        pencere.destroy()
    elif yanlis_tahminler >= maksimum_hak:
        messagebox.showinfo("Kaybettiniz", f"Doğru kelime: {secilen_kelime}. Toplam puanınız: {toplam_puan}")
        pencere.destroy()

# ---- GUI Oluşturma ----
pencere = tk.Tk()
pencere.title("Adam Asmaca")

# Kelime ve Puan Görselleri
kelime_label = tk.Label(pencere, text=" ".join(gorunur_kelime), font=("Arial", 24))
kelime_label.pack()

puan_label = tk.Label(pencere, text=f"Puan: {toplam_puan}", font=("Arial", 16))
puan_label.pack()

hak_label = tk.Label(pencere, text=f"Kalan Hak: {maksimum_hak - yanlis_tahminler}", font=("Arial", 16))
hak_label.pack()

# Harf Girişi ve Buton
giris = tk.Entry(pencere, font=("Arial", 16))
giris.pack()

tahmin_butonu = tk.Button(pencere, text="Tahmin Et", command=harf_tahmin_et, font=("Arial", 16))
tahmin_butonu.pack()

# Başlat
pencere.mainloop()

