urunler = []

while True:
    print("\n1-Ekle  2-Listele  6-Çıkış")
    secim = input("Seçimin: ")

    if secim == "1":
        ad = input("Ürün adı: ")
        adet = int(input("Adet: "))
        fiyat = float(input("Birim fiyat: "))
        urunler.append({"ad": ad, "adet": adet, "fiyat": fiyat})
        print("Ürün eklendi.")

    elif secim == "2":
        if len(urunler) == 0:
            print("Stokta ürün yok.")
        for i, urun in enumerate(urunler, start=1):
            uyari = "  <- KRİTİK" if urun["adet"] < 5 else ""
            print(f"{i}. {urun['ad']} | Adet: {urun['adet']} | Fiyat: {urun['fiyat']} TL{uyari}")

    elif secim == "6":
        break

    else:
        print("Geçersiz seçim.")