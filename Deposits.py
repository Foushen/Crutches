a = int(input("На сколько лет хотите открыть вклад: "))
b = int(input("Процентная ставка(%): "))
b = b * 0.01 + 1
c = 2   
d = float(input("Сумма изначального вклада: "))
f = float(input("Сумма ежегодного вклада: "))
while c < a:
    d = d * b + f
    c +=1
d = float('{:.2f}'.format(d))
print("За", a, "лет вклада, вы заработаете примерно", d, "BYN")
    