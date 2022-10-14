a = int(input('Digite o limite dos números a serem analisados: '))
x = [2]
for i in range(3,a + 1):
    d = False
    for b in range(len(x)):
        if i % x[b - 1] == 0:
            d = True
            break
    if d == True:
        continue
    x.append(i)
    print(i)        