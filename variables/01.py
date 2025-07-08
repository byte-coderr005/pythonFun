print("Hello Python World!")
message = "Hello World!" #string metin
print(message)
yas = 25 # integer
boy = 1.75 #float
ogrenci_mi = True # boolean 
#degisken isimleri rakamla baslayamaz!
message = "Selam burak!"
print(message)
print(message.upper())
print(message.lower())
first_name = "Burak"
last_name = "Ozturk"
full_name = f"{first_name} {last_name}"
print(full_name)
#Liste
numbers = [1,2,3,4]
for i in numbers:
 print(i)
#Dictionary (Sozluk)
kisi = {
    "ad": "Burak",
    "yas" : 27,
    "sehir" : "Istanbul"
}
print(kisi["ad"])
for anahtar, deger in kisi.items():
    print(anahtar,":",deger)
#TUPLES
#listelere benzer ama degistirilemez. Bir kez tanımlandıktan sonra elemanları değiştirilemez.
renkler = ("kirmizi","yeşil","mavi")

#set 
#pythonda sırasız ve tekrarsız elemanlar içeren bir veri yapısıdır.
arabalar = {"bmw","mercedes","audi"}
arabalar.add("toyota")
arabalar.remove("bmw")
print("mercedes" in arabalar)