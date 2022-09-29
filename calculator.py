# -*- coding: utf-8 -*-

# operasyon= int(input("operasyon giriniz:"))

# print("operasyon:")
# print("1: topla")
# print("2: çıkar")
# print("3: çarp")
# print("4: böl")

def topla(sayi1,sayi2):
    return sayi1+sayi2
def cıkar(sayi1,sayi2):
     return sayi1-sayi2
def carp(sayi1,sayi2):
    return sayi1*sayi2
def bol(sayi1,sayi2):
    return sayi1/sayi2

operasyon= int(input("operasyon giriniz:"))
sayi1= int(input("sayi giriniz:"))
sayi2= int(input("sayi giriniz:"))


if operasyon == 1:
    print(topla(sayi1, sayi2))

elif operasyon== 2:
    print(cıkar(sayi1, sayi2))
    
elif operasyon== 3:
    print(carp(sayi1, sayi2)) 
    
elif operasyon== 4:
    print(bol(sayi1, sayi2))     

else:
    
    print("hatalı sayi girdiniz!")
   
