#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pip._vendor.distlib.compat import raw_input

##RAW INPUT

print("ekrana yazdirma")
ad = raw_input()
print(ad)

#Carpma Islemi
print("Carpma Islemi - String ")
sayi1 = raw_input()
sayi2 = raw_input()
print(sayi1+sayi2)

print("Carpma Islemi - Number ")
sayi1 = raw_input()
sayi2 = raw_input()
print(int(sayi1)*int(sayi2))

##INPUT

sayi1 = input("Sayi giriniz:")
print(sayi1)


sayi1 = input("Karakter Giriniz:")
print(sayi1)