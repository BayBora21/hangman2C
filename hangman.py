import tkinter as tk
import pandas as pd
import random
import csv
import os
import sys

# veri seti
kelimeler = [
    {"Kelime": "Kedi", "Kategori": "Hayvanlar", "Zorluk": "Kolay"},
    {"Kelime": "İzmir", "Kategori": "Şehirler", "Zorluk": "Kolay"},
    {"Kelime": "Muz", "Kategori": "Meyveler", "Zorluk": "Kolay"},
    {"Kelime": "Org", "Kategori": "Müzik Aletleri", "Zorluk": "Kolay"},
    {"Kelime": "Panter", "Kategori": "Hayvanlar", "Zorluk": "Orta"},
    {"Kelime": "Berlin", "Kategori": "Şehirler", "Zorluk": "Orta"},
    {"Kelime": "Hurma", "Kategori": "Meyveler", "Zorluk": "Orta"},
    {"Kelime": "Keman", "Kategori": "Müzik Aletleri", "Zorluk": "Orta"},
    {"Kelime": "Ornitorenk", "Kategori": "Hayvanlar", "Zorluk": "Zor"},
    {"Kelime": "Lüleburgaz", "Kategori": "Şehirler", "Zorluk": "Zor"},
    {"Kelime": "Avokado", "Kategori": "Meyveler", "Zorluk": "Zor"},
    {"Kelime": "Saksafon", "Kategori": "Müzik Aletleri", "Zorluk": "Zor"},
]

# CSV dosyası türünde
with open("kelime_dataset.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["Kelime", "Kategori", "Zorluk"])
    writer.writeheader() 
    writer.writerows(kelimeler) 

print("Veri seti başarıyla oluşturuldu: kelime_dataset.csv")

def wordchecker():
while "_" in display_word:

    userletter = input("Bir Harf Giriniz: ").lower()
    
    if userletter in gameword:
      
        for i, letter in enumerate(gameword):
            if letter == userletter:

                display_word[i] = userletter
                
    else:
        loss_score += 1
        #need to add the hangman status increase
wordchecker()
