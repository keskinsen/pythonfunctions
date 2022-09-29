# -*- coding: utf-8 -*-

sayi= int(input("sayi giriniz:"))
deger=1

if sayi<0:
    print("negatif sayiların faktöriyeli olmaz")
elif sayi==0:
    print("sifir faktöriyel= 1 ")
else:
    
    for i in range(sayi):
    
        deger= deger* (i+1)
    
    print(str(sayi)+ " faktötiyel= " +str(deger))
    
    
    
# def faktoriyelHesabi(a):
#     return (0,a,1)
# print(faktoriyelHesabi(5))
