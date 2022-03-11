"""
    Վարժություն 1.3
    Ստեղծեք ֆունկցիա, որը որպես արգումենտ ստանում է երեք թվեր և
    վերադարձնում է դրանցից երկու մեծագույնների քառակուսիների գումարը։
"""


def maxSquareSum(a, b, c):
    if a > b > c or b > a > c:
        return a ** 2 + b ** 2
    elif a > c > b or c > a > b:
        return a ** 2 + c ** 2
    elif b > c > a or c > b > a:
        return b ** 2 + c ** 2


print("1.3 Exercise ->", maxSquareSum(3, 1, 4))

'''
    Վարժություն 1.5
    Ստեղծել ֆունկցիա, որը ստանում է երկու թվային արգումենտ` a և b,
    և վերադարձնում է a-ից մինչև b ընկած ամբողջ թվերի գումարը։
    Կարող եք ենթադրել, որ առաջին արգումենտը միշտ փոքր է երկրորդից։
'''


def sumOfIntNumber1(a, b):
    sumar = 0
    x = a
    while x <= b:
        sumar += x
        x += 1
    return sumar


print("1.5 Exercise ->", sumOfIntNumber1(12, 15))

'''
Վարժություն 1.6
    Իրականացնել նախորդ վարժությունում տրված ֆունկցիան՝ հաշվի առնելով, որ առաջին արգումենտը կարող է մեծ լինել երկրորդից։ 
    Այդ դեպքում ֆունկցիան պետք է վերադարձնի b-ից մինչև a ամբողջ թվերի գումարը։
'''


def sumOfIntNumber2(a, b):
    if a > b:
        a, b = b, a
    sumar = 0
    x = a
    while x <= b:
        sumar += x
        x += 1
    return sumar


print("1.6 Exercise ->", sumOfIntNumber2(19, 15))

'''
Վարժություն 1.7
Իրականացնել pow(a, b) ֆունկցիան՝ հաշվի առնելով, որ b-ն կարող է լինել նաև ոչ դրական։ Հիշեցնենք

a ** b = a ** b, եթե a > 0
a ** b = (1 / a ** (-b)), եթե b < 0
a ** b = 1, եթե b = 0

Նաև հաշվի առեք, որ a-ի b աստիճանը սխալ արտահայտություն է, եթե a-ն հավասար է 0, իսկ b-ն բացասական է

'''


def pow(a, b):
    count = 0
    res = 1
    while count < abs(b):
        res *= a
        count += 1
    if b < 0:
        if a == 0:
            return "0 devision error !"
        res = 1 / res
    return res


print("1.7 Exercise ->", pow(0, -1))
