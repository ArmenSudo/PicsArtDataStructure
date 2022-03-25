#  ___________________ Վարժություն 1.11 ________________________________________

"""
        f ֆունկցիան սահմանվում է հետևայլ կերպ.
        f(n) = n, եթե n < 3
        f(n) = f(n - 1) + f(n - 2) + f(n - 3), եթե n >= 3
        n-ը կարող է լինել միայն 0 և դրական ամբողջ թիվ։
        Իրականացրեք լուծումը ռեկուրսիվ, իտերատիվ և պոչավոր ռեկուրսիվ տարբերակներով։
"""


# Recursion
def f1(n):
    if n < 0:
        return "Wrong Input!"
    else:
        if n < 3:
            return n
        return f1(n - 1) + f1(n - 2) + f1(n - 3)


print("Recursion -> ", f1(7))


# Loop

def f2(n):
    a = 0
    b = 1
    c = 2
    while n > 0:
        a, b, c = b, c, a + b + c
        n -= 1
    return a


print("Loop -> ", f2(7))


# Tail recursion
def f3(n, a=0, b=1, c=2):
    return a if n == 0 else f3(n - 1, b, c, a + b + c)


print("Tail recursion -> ", f3(7))


#  ___________________________________________________________________________


#  ___________________ Վարժություն 1.12 ________________________________________
# https://wethecomputerguys.files.wordpress.com/2014/05/untitled3.png?w=474
# Օգտվելով հետևյալ հղումից կստանանք մեր պատասխանը

def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


def pas(n, m):
    if m < 0 or n < m:
        return "Wrong Input!"
    return int(fact(n) / (fact(m) * fact(n - m)))


print("Pascal's Pyramid -> ", pas(3, 3))

# _______________________________________________________________________________


#  ___________________ Վարժություն 1.12 Տ2 ________________________________________

def pas2(m, n):
    if m < 1 or n < 1 or n > m:
        return "Wrong Input"
    return 1 if n == 1 or n == m else pas2(m - 1, n) + pas2(m - 1, n - 1)


print("Pascal's Pyramid -> ", pas2(5, 5))

# _______________________________________________________________________________
