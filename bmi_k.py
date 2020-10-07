# _*_ coding: utf-8 _*_

#Kalkulator BMI.
print("Kalkulator BMI.")
wzrost = float(input("Podaj swój  wzrost w cm: "))
waga = float(input("Podaj ile ważysz w kg: "))
bmi = round(waga / ((wzrost / 100) ** 2), 2)
print("Przy wadze", waga, "i wzroście", wzrost, "m twoje BMI wynosi: ", bmi, ".")

#Kalkularor kalorii dla kobiet.
print("Kalkulator dziennego zapotrzebowania na kalorie dla kobiet.")
wiek = float(input("Podaj swój wiek w latach: "))
s = -167 #współczynnik zależny od płci.
print("Wprowadź wartość współczynnika zależnego od swojego stylu życia:\
\nPraca siedząca, brak dodatkowej aktywności fizycznej:                      1.2\
\nPraca niefizyczna, mało aktywny tryb życia:                                1.4\
\nLekka praca fizyczna, regularne ćwiczenia 3-4 razy (ok. 5h) w tygodniu:    1.6\
\nPraca fizyczna, regularne ćwiczenia od 5razy (ok. 7h) w tygodniu:          1.8\
\nPraca fizyczna ciężka, regularne ćwiczenia 7 razy w tygodniu:              2.0")
saf = float(input()) #współczynnik zależny od stylu życia.
ppm = 10 * waga + 6.25 * wzrost - 5 * wiek + s
dznk = round(ppm * saf)
print("Twoje dzienne zapotrzebowanie na kalorie wynosi:", dznk, "kalorii.")
