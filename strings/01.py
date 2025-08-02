#Tek tırnak ile
'Burak zzz'
#Çift tırnak ile
"Burak zzz"
#3 tırnak ile
"""Burak zzz"""
a = "burak"
print(a[0]) # b

b = "Hello, World!"
print(b[2:5])

print(b[:5])

print(b.upper())
print(b.lower())
age = 35
txt = f"My name is Burak, I am {age}"
print(txt)
print(len(txt)) # 28
#Bastan sona 2 deger atlayarak stringi al.
print(a[::2])

#Example
string = "Benim adım Burak. Burak çok çalişkan birisidir."
lower_string = string.lower()
print(lower_string.count("burak")) # output:2