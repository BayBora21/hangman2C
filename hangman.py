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

