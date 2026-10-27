import tkinter as tk
from tkinter import ttk, messagebox

urunler = []

def ekle():
    ad = ad_giris.get()
    try:
        adet = int(adet_giris.get())
        fiyat = float(fiyat_giris.get())
    except ValueError:
        messagebox.showerror("Hata", "Adet ve fiyat sayı olmalı!")
        return
    if ad == "":
        messagebox.showerror("Hata", "Ürün adı boş olamaz!")
        return
    urunler.append({"ad": ad, "adet": adet, "fiyat": fiyat})
    ad_giris.delete(0, tk.END)
    adet_giris.delete(0, tk.END)
    fiyat_giris.delete(0, tk.END)
    listele()

def listele():
    for satir in tablo.get_children():
        tablo.delete(satir)
    for urun in urunler:
        durum = "KRİTİK" if urun["adet"] < 5 else "Normal"
        tablo.insert("", tk.END, values=(urun["ad"], urun["adet"], urun["fiyat"], durum))

pencere = tk.Tk()
pencere.title("Stok Takip")
pencere.geometry("500x400")

tk.Label(pencere, text="Ürün Adı").pack()
ad_giris = tk.Entry(pencere)
ad_giris.pack()

tk.Label(pencere, text="Adet").pack()
adet_giris = tk.Entry(pencere)
adet_giris.pack()

tk.Label(pencere, text="Fiyat").pack()
fiyat_giris = tk.Entry(pencere)
fiyat_giris.pack()

tk.Button(pencere, text="Ekle", command=ekle).pack(pady=10)

tablo = ttk.Treeview(pencere, columns=("ad", "adet", "fiyat", "durum"), show="headings")
tablo.heading("ad", text="Ürün")
tablo.heading("adet", text="Adet")
tablo.heading("fiyat", text="Fiyat")
tablo.heading("durum", text="Durum")
tablo.pack(fill="both", expand=True)

pencere.mainloop()