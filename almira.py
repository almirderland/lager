# from random import randint

# x = randint(1,100)
# print(x)
# print("камень-ножницы-бумага")
# print("Вы будете играть с компьютером в камень-ножницы-бумага. Сделайте свой выбор")
# print("1 -- камень")
# print("2 -- ножницы")
# print("3 -- бумага")
# x = randint(1,3)
# n = int(input("Сделайте свой выбор"))
# if x == n:
#     print("Ничья")
# elif (x == 1 and n == 2) or (x == 2 and n == 3) or (x == 3 and n == 1):
#     print("Вы проиграли")
# else:
#     print("Вы победили")

n = int(input())
n = n//10000000
if n == 8777 or n ==8705 or n == 8771 or n == 8776 :
    print("Ваш абонент: Билайн")
elif n == 8727 or n== 8775:
    print("Ваш абонент: Актив")
elif n == 8701 or n== 8702 or n==8778:
    print("Ваш абонент: Ксел")
elif n == 8707 or n== 8747:
    print("Ваш абонент: Теле2")
else:
    print("Ошибка")