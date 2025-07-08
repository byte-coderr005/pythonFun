#if koşul:
#koşul doğruysa burası çalışır
#elif başka_koşul:
# ilk koşul yanlışsa ve bu doğruysa burası çalışır.
yas = 18
if yas >= 18:
    print("REsit")
else:
    print("Reşit Degil")
    #Basit uygulama
#Klavyeden girilen not büyük mü kücük mü
not_ort = float(input("Lutfen notu girin:")) # float tipinde aldık.
if(not_ort >= 85):
    print("Pekiyi")
elif not_ort >= 70:
    print("iyi")
elif not_ort >= 50:
    print("Geçer")
else:
    print("Kaldi")

#ornek app
ad = input("Adinizi girin: ")
yas = int(input("Yasinizi girin: "))
if yas >= 18:
    resit = True
else:
    resit = False

ogrenci = {"ad": ad,
           "yas": yas,
           "resitMi":resit
}
for anahtar, deger in ogrenci.items():
    print(f"{anahtar}: {deger}")
