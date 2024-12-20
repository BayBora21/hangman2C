    toplam_puan = 0
    dogru_harf_puani = 10
    yanlis_harf_puani  = -5
    bonus_can_puani = 5
    bonus_kelime_puani = 10
    maksimum_hak=7
    yanlis_tahminler=0


    # Puanlama Fonksiyonları
def guncel_puan(dogru_tahmin):
    global toplam_puan
    if dogru_tahmin:
        toplam_puan += dogru_harf_puani
    else:
        toplam_puan += yanlis_harf_puani

def nihai_puan_hesapla(kalan_canlar, kelime_uzunlugu):
    global toplam_puan
    bonus_puan = kalan_canlar * bonus_can_puani
    bonus_puan += kelime_uzunlugu * bonus_kelime_puani
    toplam_puan += bonus_puan
    return toplam_puan

final_puan = nihai_puan_hesapla (maksimum_hak - yanlis_tahminler, len())