for i in range(3):
    for j in range(2):
        print(f"{i}",{j})

#gorev 3 satır ve 5 sutnluk * çiz
for i in range(3): # 3 satir
    for j in range(5): # her satirda 5 yildiz
        print("*", end="") # * i yazdir ve ayni satirda kal.
    print() # satir sonuna gelince alt satira gec
#Üçgen şekli oluştur
for i in range(1,6):
    print()
    for j in range(i):
        print("*", end="")
