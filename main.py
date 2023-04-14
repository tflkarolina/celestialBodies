
import tkinter as tk
from tkinter import messagebox
from typing import List

import CialoNiebieskie
from CialoNiebieskie import *

#SORTOWANIE ROSNACO
def sortuj_odleglosc():
    lista_cial.delete(0, tk.END)
    for cialo in CialoNiebieskie.bucket_sort_odl():
        lista_cial.insert(tk.END, cialo)

def sortuj_masa():
    lista_cial.delete(0, tk.END)
    for cialo in CialoNiebieskie.bucket_sort_masa():
        lista_cial.insert(tk.END, cialo)

def sortuj_okres():
    lista_cial.delete(0, tk.END)
    for cialo in CialoNiebieskie.bucket_sort_okres():
        lista_cial.insert(tk.END, cialo)

#SORTOWANIE MALEJACO
def sortuj_odleglosc_mal():
    lista_cial.delete(0, tk.END)
    for cialo in CialoNiebieskie.bucket_sort_odl_mal():
        lista_cial.insert(tk.END, cialo)

def sortuj_masa_mal():
    lista_cial.delete(0, tk.END)
    for cialo in CialoNiebieskie.bucket_sort_masa_mal():
        lista_cial.insert(tk.END, cialo)

def sortuj_okres_mal():
    lista_cial.delete(0, tk.END)
    for cialo in CialoNiebieskie.bucket_sort_okres_mal():
        lista_cial.insert(tk.END, cialo)

def dodaj_cialo():
    try:
        nazwa = nazwa_entry.get()
        masa = masa_entry.get()
        masa = float(masa)
        odleglosc = odleglosc_entry.get()
        odleglosc = float(odleglosc)
        okres = okres_entry.get()
        okres = float(okres)

        if masa<0 or odleglosc<0 or okres<0:
            raise ValueError

        nowe_cialo = CiałoNiebieskie(nazwa, masa, odleglosc, okres)
        ciala_niebieskie.append(nowe_cialo)
        messagebox.showinfo("Powiadomienie", "Pomyślnie dodano planetę")
        sortuj_odleglosc()

    except ValueError:
        messagebox.showerror("Błąd", "Zły typ danych")
        return

def usun_cialo():
    ciala = lista_cial.curselection()
    for cialo in ciala[::-1]:
        ciala_niebieskie.pop(cialo)
    messagebox.showinfo("Powiadomienie", "Pomyślnie usunięto planetę")
    sortuj_odleglosc()

def edytuj_cialo():
    ciala = lista_cial.curselection()
    for cialo in ciala[::-1]:
        ciala_niebieskie.pop(cialo)

    try:
        nazwa = nazwa_entry.get()
        masa = masa_entry.get()
        masa = float(masa)
        odleglosc = odleglosc_entry.get()
        odleglosc = float(odleglosc)
        okres = okres_entry.get()
        okres = float(okres)

        if masa < 0 or odleglosc < 0 or okres < 0:
            raise ValueError

        nowe_cialo = CiałoNiebieskie(nazwa, masa, odleglosc, okres)
        ciala_niebieskie.append(nowe_cialo)
        sortuj_odleglosc()

    except ValueError:
        messagebox.showerror("Błąd", "Zły typ danych")
        return

    messagebox.showinfo("Powiadomienie", "Pomyślnie edytowano planetę")
    sortuj_odleglosc()


#GUI
root = tk.Tk()
root.title("Układ Słoneczny")

space = tk.Label(root, text="", bg='#99AAFF')
space.pack()

sort = tk.Label(root,text= "Sortuj obiekty w porządku rosnącym:", bg='#99AAFF')
sort.pack()

odleglosc_button = tk.Button(root,text="według odległości", command=sortuj_odleglosc, bg='#ECD4FF')
odleglosc_button.pack()

masa_button = tk.Button(root, text="według masy", command=sortuj_masa, bg='#ECD4FF')
masa_button.pack()

okres_button = tk.Button(root, text="według okresu obiegu dookoła Słońca", command=sortuj_okres, bg='#ECD4FF')
okres_button.pack()

space0 = tk.Label(root, text="",bg='#99AAFF')
space0.pack()

sort1 = tk.Label(root,text= "Sortuj obiekty w porządku malejącym:", bg='#99AAFF')
sort1.pack()

odleglosc_button_mal = tk.Button(root, text="według odległości", command=sortuj_odleglosc_mal, bg='#ECD4FF')
odleglosc_button_mal.pack()

masa_button_mal= tk.Button(root, text="według masy", command=sortuj_masa_mal, bg='#ECD4FF')
masa_button_mal.pack()

okres_button_mal = tk.Button(root, text="według okresu obiegu dookoła Słońca", command=sortuj_okres_mal, bg='#ECD4FF')
okres_button_mal.pack()

space1 = tk.Label(root, text="", bg='#99AAFF')
space1.pack()

dane = tk.Label(root,text= "Dane planety:", bg='#99AAFF')
dane.pack()

nazwa_label = tk.Label(root, text="Nazwa:", bg='#CCFFDD')
nazwa_label.pack()

nazwa_entry = tk.Entry(root)
nazwa_entry.pack()

masa_label = tk.Label(root, text="Masa [10^24 kg]:", bg='#CCFFDD')
masa_label.pack()

masa_entry = tk.Entry(root)
masa_entry.pack()

odleglosc_label = tk.Label(root, text="Odległość od Słońca [au]:", bg='#CCFFDD')
odleglosc_label.pack()

odleglosc_entry = tk.Entry(root)
odleglosc_entry.pack()

okres_label = tk.Label(root, text="Okres obiegu dookoła Słońca [lata zwrotnikowe]:", bg='#CCFFDD')
okres_label.pack()

okres_entry = tk.Entry(root)
okres_entry.pack()

space2 = tk.Label(root, text="", bg='#99AAFF')
space2.pack()

wpisz = tk.Label(root, text="Aby dodać planetę, wpisz dane i naciśnij przycisk", bg='#99AAFF')
wpisz.pack()

dodaj_button = tk.Button(root, text="Dodaj ciało", command=dodaj_cialo, bg='#B7EAF7')
dodaj_button.pack()

space3 = tk.Label(root, text="", bg='#99AAFF')
space3.pack()

usn = tk.Label(root,text= "Aby usunąć planetę, wybierz z listy i naciśnij przycisk", bg='#99AAFF')
usn.pack()

usun_button = tk.Button(root, text="Usuń ciało", command=usun_cialo, bg='#B7EAF7')
usun_button.pack()

space4 = tk.Label(root, text="", bg='#99AAFF')
space4.pack()

ed = tk.Label(root,text= "Aby edytować planetę, wpisz dane, wybierz planetę z listy i naciśnij przycisk", bg='#99AAFF')
ed.pack()

edytuj_button = tk.Button(root, text="Edytuj ciało", command=edytuj_cialo,bg='#B7EAF7')
edytuj_button.pack()

space4 = tk.Label(root, text="", bg='#99AAFF')
space4.pack()

lista_cial = tk.Listbox(root, width=70)
lista_cial.pack()

root['background'] = '#99AAFF'
root.mainloop()