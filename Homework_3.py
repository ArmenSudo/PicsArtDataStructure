# ______________________________________________________________________________________________________________
#                                          Վարժություն 1.9
# ______________________________________________________________________________________________________________

"""

    Վարժություն 1.9
    Ունենք inc և dec ֆունկցիաները։ inc-ը վերադարձնում է արգումենտին գումարած 1 արժեքը,
    իսկ dec-ը արգումենտից հանած 1 արժեքը

    def inc(a):
        return a + 1
    def dec(a):
        return a - 1

    Կիրառելով պարամետրերի փոխարինման մոդելը, պարզաբանեք հետևյալ ֆունկցիաներից
    յուրաքանչյուրից առաջացող գործընթացները, դրանցից որն է ռեկուրսիվ, որը պոչավոր ռեկուրսիվ,
    պատասխանը հիմնավորեք

    def add1(a, b):
        if a == 0:
            return b
        else:
            inc(add1(dec(a), b))

    def add2(a, b):
        if a == 0:
            return b
        else:
            return add2(dec(a), inc(b))

    Օրինակի համար դիտարկեք add1(4, 5) և add2(4, 5) կանչերը

"""


"""
    inc ֆունկցիան ռեկուրսիվ ֆունկցիա է քանի որ այն սպասում է որ add1(dec(a)), b)
    ֆունկցիան կատարվի որը իր հերթին առաջացնում է մեկ այլ այդ տիպի սպասումներ։
    Ամեն անգամ add1(dec(a)), b) ֆունկցիան կանչելիս նախ a-ի արժեքը փոքրացվում է 1-ով։
    Եվ այդպես այնքան մինչև որ a==0 ճիշտ լինի։
    Դիտարկենք add1(4, 5)`
        add1(4, 5) -> inc(add1(dec(4), 5)) -> inc(add1(3, 5)) -> inc(inc(add1(dec(3), 5))) ->
        -> inc(inc(add1(2, 5))) -> inc(inc(inc(add1(dec(2), 5))) -> inc(inc(inc(add1(1, 5))) ->
        -> inc(inc(inc(inc(add1(dec(1), 5))) -> inc(inc(inc(inc(add1(0, 5))) -> inc(inc(inc(inc(5)))) ->
        -> inc(inc(inc(6))) -> inc(inc(7)) -> inc(8) -> 9
"""

"""
    add2 ֆունկցիան պոչավոր ռեկուրսիվ է քանի որ այն ինքն իրեն կանչում է,
    սակայն անհրաժեշտութկուն չկա կանչից հետո լոկալ տիրույթը պահպանելու,
    որովհետև այն ոչ մի տվյալ չի պահում այլ փոխանցում է նոր կանչին։
    add2 ֆունկցիան ստանում է երկու արժեք a և b որից հետո ստուգում է
    եթե a-ն հավասար է 0-ի ապա վերադարձնում է b-ի արժեքը եթե ոչ 
    ապա կանչում է ինքն իրեն, և որպես փոխանցվող արժեք տալիս է dec(a), inc(b)
    որից 1-ինը փոքրացնում է a թիվը 1-ով իսկ 2-րդը մեծացնում է b-Ն 1-ով։
    Այս գործողությունները կրկնվում է այնքան քանի դեռ a թիվը չի հավասարվում 0-ի։
    Դիտարկենք add2(4, 5)`
        1) add2(4, 5) -> add2(dec(4), inc(5)) -> add2(3, 6) -> add2(dec(3), inc(6)) ->
            -> add2(2, 7) -> add2(dec(2), inc(7)) -> add2(1, 8) -> add2(dec(1), dec(8)) ->
            -> add2(0, 9) -> 9 վերադարձնում է 9։ 

"""


# ______________________________________________________________________________________________________________
#                                          Վարժություն 1.10
# ______________________________________________________________________________________________________________
"""

    Վարժություն 1.10
    Հաջորդ ֆունկցիան հաշվարկում է մաթեմատիկական ֆունկցիա, որը հայտնի է Ակերմանի ֆունկցիա անվամբ
    
    >>> def ackermann(x, y):
        if y == 0:
            return 0
        elif x == 0:
            return 2 * y
        elif y == 1:
            return 2
        else:
            return ackermann(x - 1, ackermann(x, y - 1))
    
    
    
    Ի՞նչ կլինի հետևյալ կանչերի արդյունքը
    
    ackermann(1, 5)
    
    ackermann(2, 4)
    
    ackermann(3, 3)
    
    
    Կարճ նկարագրեք, թե ինչ են հաշվում a1, a2, և a3 ֆունկցիաները
    
    >>> def a1(n):
        return ackermann(0, n)
    >>> def a2(n):
        return ackermann(1, n)
    >>> def a3(n):
        return ackermann(2, n)

"""


def ackermann(x, y):
    if y == 0:
        return 0
    elif x == 0:
        return 2 * y
    elif y == 1:
        return 2
    else:
        return ackermann(x - 1, ackermann(x, y - 1))


print(ackermann(1, 5))  # -> 32

print(ackermann(2, 4))  # -> 65536

print(ackermann(3, 3))  # -> 65536


def a1(n):
    return ackermann(0, n)


print(a1(65))

"""
    a1 ֆունկցիան կանչում է ackermann(0, n) 
    որի հաշվարկի արդյունքում վերադարձնում է 2*n, 
    որը իր հերթին վերադարձնում է որպես a1 արդյունք 
"""


def a2(n):
    return ackermann(1, n)


print(a2(5))

"""
    a2 ֆունկցիան կանչում է ackermann(1, n) 
    որի հաշվարկի արդյունքում կանչվում է ackermann(0, ackermann(1, n - 1)), 
    և այդ կերպ այնքան մինչև n-1 -ի արժեքը ստտացվի 1, որից հետո ֆունկցիան կվերադարձնի 2
    և հետ քայլերով կհասնի սկզբնական կանչի վայրը և կտա մեզ պատասխան։(Այս դեպքում մենք համարում
    ենք որ n>1 հակառակ դեպքում ֆունկցիան 1-ի դեպքում կվերադարձնի 2, իսկ 0-ի դեպքում 0)
    
"""


def a3(n):
    return ackermann(2, n)


"""

    a3 ֆունկցիան կանչում է ackermann(2, n) 
    որի հաշվարկի արդյունքում կանչվում է ackermann(1, ackermann(2, n - 1)), որից հետո
    կանչվում է ackerman(0, ackermann(1, ackermann(2, n - 1) - 1))), որից հետո
    ու այսպես կանչվում է այնքան մինչև բազային դեպքին հասնելը։
    
"""
