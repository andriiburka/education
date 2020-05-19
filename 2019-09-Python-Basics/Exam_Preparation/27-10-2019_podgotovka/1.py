# Задача 1. Коледни лакомства
# Инна ще покани гости за Коледа и решава да ги посрещне с различни коледни лакомства.
# Тя отива до местната сладкарница, за да купи по няколко килограма от всеки вид.
# Напишете програма, която изчислява колко пари ще са необходими на Инна, според количеството и цените в сладкарницата.
# На конзолата ще бъдат въведени цените в лева на баклавата и мъфините и количеството щолен,
# бонбони и бисквити в килограми. Цените на лакомствата се формират както следва:
# •	Щолен – 60% по-скъп от баклавата
# •	Бонбони – 80% по-скъпи от мъфини
# •	Бисквити – 7.50 лв. за килограм

# Вход
# От конзолата се четат 5 числа:
# •	Първи ред – цена на баклавата на килограм. Реално число в интервала [0.00…40.00]
# •	Втори ред – цена на мъфините на килограм. Реално число в интервала [0.00…30.00]
# •	Трети ред – килограмите щолен. Реално число в интервала [0.00…50.00]
# •	Четвърти ред – килограмите бонбони. Реално число в интервала [0.00… 70.00]
# •	Пети ред – килограмите бисквити. Цяло число в интервала [0 ... 100]

# Обяснения
# Цена на щолена = 6.90 + 6.90 * 0.60 = 11.04 лв. за килограм
# Сума щолен = 1.5 * 11.04 = 16.56
# Цена на бонбоните = 4.20 + 4.20 * 0.80 =  7.56 лв. за килограм
# Сума бонбони = 2.5 * 7.56 = 18.90
# Сума бисквити = 1 * 7.50 = 7.50
# Сметка = 16.56 + 18.90 + 7.50 = 42.96

# Изход
# Да се отпечата на конзолата едно число с плаваща запетая: колко пари ще са нужни на Инна, за да закупи всички лакомства. Резултатът да се форматира до втория знак след десетичната запетая.

cena_baklava_kg = float(input())
cena_mafini_kg = float(input())
shtolen = 0

shtolen_kg = float(input())
bonboni_kg = float(input())
biskviti_kg = int(input())

shtolen = cena_baklava_kg + (cena_baklava_kg * 0.6)
suma_shtolen = shtolen_kg * shtolen

cena_bonboni_kg = cena_mafini_kg + (cena_mafini_kg * 0.8)
suma_bonboni = bonboni_kg * cena_bonboni_kg

suma_biskviti = 7.50 * biskviti_kg

smetka = suma_shtolen + suma_biskviti + suma_bonboni
print(f'{smetka:.2f}')
