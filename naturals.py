class Natural:
    def __init__(self, number):
        """Принимает строку, выдает натуральное число, Смирнов Иван"""
        self.A = list(int(i) for i in number)
        self.n = len(self.A)

    def __str__(self):
        """Возвращает строковое представление числа. Малых Андрей"""
        return "".join(map(str, self.A))


def COM_NN_D(a, b):
    """Сравнение натуральных чисел: 2 - если первое больше второго, 0, если равно, 1 иначе. Виноградов Андрей"""
    if a.n == b.n:
        for i in range(a.n):
            if a.A[i] > b.A[i]:
                return 2
            elif a.A[i] < b.A[i]:
                return 1
        return 0
    elif a.n > b.n:
        return 2
    else:
        return 1


def MUL_ND_N(a, x):
    """Умножение натурального числа на цифру. Дитятьев Иван"""
    if x != 0:
        a.A.reverse()
        ost = 0
        for i in range(a.n):
            e = a.A[i]
            a.A[i] = (((e * x) + ost) % 10)
            ost = (((e * x) + ost) // 10)
        if i == a.n - 1 and ost > 0:
            a.A.append(ost)
        o = ""
        a.A.reverse()
        for i in a.A:
            o = o + str(i)
        return Natural(o)
    else:
        return Natural('0')


def SUB_NN_N(a1, b1):
    """Вычитание из первого большего натурального числа второго меньшего или равного. Виноградов Андрей"""
    a = Natural(str(a1))
    b = Natural(str(b1))
    Ifer = COM_NN_D(a, b)
    D = Natural("")
    a.A.reverse()
    b.A.reverse()
    if Ifer == 2:
        c = [0] * a.n
        last = (b.n) - 1
        for i in range(a.n):
            k = i + 1
            if i > last:
                c[i] = a.A[i]
            else:
                if a.A[i] >= b.A[i]:
                    c[i] = a.A[i] - b.A[i]

                else:
                    while a.A[k] == 0:
                        a.A[k] = 9
                        k += 1
                    a.A[k] -= 1
                    c[i] = 10 + a.A[i] - b.A[i]
        c.reverse()
        k = 0
        j = 0
        while c[k] == 0:
            k += 1
        ans = [0] * (a.n - k)
        for i in range(k, a.n):
            ans[j] = c[i]
            j += 1
        D.A = ans
        D.n = a.n - k
    elif Ifer == 1:
        c = [0] * b.n
        last = (a.n) - 1
        for i in range(b.n):
            k = i + 1
            if i > last:
                c[i] = b.A[i]
            else:
                if b.A[i] >= a.A[i]:
                    c[i] = b.A[i] - a.A[i]

                else:
                    while b.A[k] == 0:
                        b.A[k] = 9
                        k += 1
                    b.A[k] -= 1
                    c[i] = 10 + b.A[i] - a.A[i]
        c.reverse()
        k = 0
        j = 0
        while c[k] == 0:
            k += 1
        ans = [0] * (b.n - k)
        for i in range(k, b.n):
            ans[j] = c[i]
            j += 1
        D.A = ans
        D.n = b.n - k
    else:
        D.A = '0'
        D.n = 1
    return D


def MUL_Nk_N(a, k):
    """Умножение натурального числа на 10^k. Ташимбетов Тимур"""
    c = a.A.copy()
    D = Natural("")
    for i in range(k):
        c.append(0)
    D.A = c
    return D


def ADD_NN_N(a1, b1):
    """Сложение натуральных чисел. Виноградов Андрей"""
    a = Natural(str(a1))
    b = Natural(str(b1))
    if COM_NN_D(a, b) != 2:
        tmp = b
        b = a
        a = tmp
    a.A.reverse()
    b.A.reverse()
    for i in range(a.n - b.n):
        b.A.append(0)
    for i in range(a.n):
        e = a.A[i]
        f = b.A[i]
        a.A[i] = (e + f) % 10
        if (e + f) >= 10:
            if i == a.n - 1:
                a.A.append(1)
                b.A.append(0)
            b.A[i + 1] += 1
    a.A.reverse()
    ans = ""
    for x in a.A:
        ans += str(x)
    return Natural(ans)


def NZER_N_B(a):
    """Проверка на ноль: если число не равно нулю, то 'да' иначе 'нет'. Айрапетов Давид"""
    if a.A[0] == 0 and a.n == 1:
        return True
    else:
        return False


def ADD_1N_N(a):
    """Добавление 1 к натуральному числу. Айрапетов Давид"""
    i = 0
    a.A.reverse()
    while a.A[i] == 9 and i + 1 < a.n:
        a.A[i] = 0
        i += 1
    if i == a.n:
        a.A.append(1)
        a.n += 1
    else:
        a.A[i] = a.A[i] + 1
    a.A.reverse()
    return a


def MUL_NN_NN(a, b):
    """Умножение натуральных чисел. Таланков Влад"""
    if str(a) != '0' and str(b) != '0':
        a.A.reverse()
        res = Natural('0')
        tens = 0
        for j in range(a.n):
            if a.A[j] == 0:
                tens += 1
            else:
                multiplier = a.A[j]
                b_copy = Natural(str(b))
                temp1 = MUL_ND_N(b_copy, multiplier)
                temp2 = MUL_Nk_N(temp1, tens)
                res = ADD_NN_N(temp2, res)
                tens += 1
        a.A.reverse()
        return res
    else:
        return Natural('0')


def DIV_NN_N(a1, b1):
    """Частное от деления большего натурального числа на меньшее или равное натуральное с остатком. Угрюмов Михаил"""
    a = Natural(str(a1))
    b = Natural(str(b1))
    temp = Natural(str(b))
    n = Natural(str(1))
    while COM_NN_D(a, b) == 2:
        b = ADD_NN_N(b, temp)
        n = ADD_1N_N(n)
        if COM_NN_D(a, b) == 0:
            return n
        if COM_NN_D(a, b) == 1:
            return SUB_NN_N(n, 1)

        
def MOD_NN_N(a1, b1):
    """Остаток от деления большего натурального числа на меньшее или равное натуральное с остатком(делитель отличен от нуля). Виноградов Андрей"""
    a = Natural(str(a1))
    b = Natural(str(b1))
    k = Natural('0')
    flag = 0
    Ifer = COM_NN_D(a, b)
    #Алгоритм использует формулу Делимое = Частное * Делитель + Остаток
    if Ifer == 2:
        Div = DIV_NN_N(a, b)
        Del = MUL_NN_NN(Div, b)
        if COM_NN_D(a, Del) != 0:

            while flag == 0:
                Del = ADD_1N_N(Del)
                k = ADD_1N_N(k)
                if COM_NN_D(a, Del) == 0:
                    flag = 1
    if Ifer == 1:
        Div = DIV_NN_N(b, a)
        Del = MUL_NN_NN(Div, a)
        if COM_NN_D(b, Del) != 0:
            while flag == 0:
                Del = ADD_1N_N(Del)
                k = ADD_1N_N(k)
                if COM_NN_D(b, Del) == 0:
                    flag = 1
    return k


if __name__ == '__main__':
    a = Natural('10343423423423423423423423423400')
    b = Natural('1')
    # Если вам нужно число без цифр длиной ноль, передайте пустую строку
    c = Natural('')
    print(a, b)
    print(MUL_NN_NN(a, b))
    print(a, b)

