#Liste ÜZerinde Dönme
meyveler = ["elma","armut","muz"]
for meyve in meyveler:
    print(meyve)
#range() ile sayılar üzerinde dönme

for i in range(5): # 0 dan 4 e kadar.
    print(i)
#while
i = 0
while i < 5:
    print(i)
    i += 1

#2 den 20 ye kadar olan sayilar
for i in range(2,21):
    if(i % 2 == 0):
        print(i)
#Disiplin kazanılır yazdır5 kere
for i in range(5):
    print("Disiplin kazanılır")
# Kullanıcıdan bir sayi al ve o sayiları o sayıya kadar topla
sayi = int(input("Bir sayi gir: "))
toplam = 0
i = 1
while(i <= sayi):
    toplam += i
    i += 1
print("Toplam: ", toplam)
#kullanici 0 girene kadar  sayi almaya devam et. sonra toplami yazdir
toplam1 = 0
while True:
    sayi1 = int(input("Lutfen bir sayi girin ama sayi 0 olursa işlem durur."))
    if(sayi1 == 0):
        break
    toplam1 += sayi1
print("Toplam: ",toplam1)