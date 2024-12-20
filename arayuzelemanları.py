import tkinter as tk

root = tk.Tk() #root değişkeniyle ana pencere oluşturma
root.title("Hangman Oyunu") 
root.configure(bg="#000000")  #pencerenin rengini değiştirme

root.geometry("600x600")  #pencere boyutunu ayarlama

oyun_paneli = tk.Frame(root, bg="#000000")  #oyun panelinin arka planı siyah olacak şekilde oluşturma
oyun_paneli.pack(pady=30)

#kelimeyi ve tahminleri gösteren beyaz metinli etiket
kelime_etiketi = tk.Label(oyun_paneli, text="", font=('Arial', 36), bg="#000000", fg="#FFFFFF", width=20)
kelime_etiketi.pack(pady=20)

#yanlış tahminleri gösteren pembe etiket
yanlis_tahmin_etiketi = tk.Label(oyun_paneli, text="Yanlış Tahminler: 0", font=('Arial', 18), bg="#000000", fg="#FFB6C1")
yanlis_tahmin_etiketi.pack(pady=10)

#harf hakkı etiketini gösteren mavi etiket
harf_hakki_etiketi = tk.Label(oyun_paneli, text="Kalan Harf Hakkınız: 7", font=('Arial', 18), bg="#000000", fg="#ADD8E6") 
harf_hakki_etiketi.pack(pady=10)

#hangman adam resmi
hangman_etiketi = tk.Label(oyun_paneli, text="", font=('Arial', 24), bg="#000000", fg="white")
hangman_etiketi.pack(pady=20)

#kullanıcının harf tahmini için giriş kutusu
tahmin_girisi = tk.Entry(oyun_paneli, font=('Arial', 18), width=10)
tahmin_girisi.pack(pady=10)

#kullanıcının harf tahmin etme butonu
tahmin_et_butonu = tk.Button(oyun_paneli, text="Tahmin Et (Harf)", state=tk.DISABLED, font=('Arial', 18), bg="#B0E0E6", fg="black", width=20, height=2)
tahmin_et_butonu.pack(pady=10)

#kullanıcının kelime tahmini için giriş kutusu
kelime_tahmin_girisi = tk.Entry(oyun_paneli, font=('Arial', 18), width=15)
kelime_tahmin_girisi.pack(pady=10)

#kullanıcının kelime tahmin etme butonu
kelime_tahmin_et_butonu = tk.Button(oyun_paneli, text="Tahmin Et (Kelime)", state=tk.DISABLED, font=('Arial', 18), bg="#E6E6FA", fg="black", width=20, height=2)
kelime_tahmin_et_butonu.pack(pady=10)

#oyunu bitirme butonu
bitir_butonu = tk.Button(oyun_paneli, text="Oyunu Bitir", state=tk.DISABLED, font=('Arial', 18), bg="#FAD02E", fg="black", width=20, height=2) 
bitir_butonu.pack(pady=20)

#yeni oyun başlatma butonu
yeni_oyun_butonu = tk.Button(oyun_paneli, text="Yeni Oyun Başlat", state=tk.DISABLED, font=('Arial', 18), bg="#98FB98", fg="black", width=20, height=2)
yeni_oyun_butonu.pack(pady=10)

#sonuç etiketleri
sonuc_etiketi = tk.Label(oyun_paneli, text="", font=('Arial', 18), bg="#000000", fg="white")
sonuc_etiketi.pack(pady=20)

#pencere çalıştırma
root.mainloop()






