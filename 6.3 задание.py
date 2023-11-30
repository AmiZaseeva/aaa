while True:
    try:
        import random
        n=int(input('Введите количество элементов в списке :'))
        if n > 0:
            a = [random.randint(-100000,100000) for i in range(n)]
            countnegativ = 0
            for num in a:
                if num < 0:
                    countnegativ += 1

            b=[]
            for i in range(0,len(a)):
                if a[i]>0:
                    b.append(a[i])
                else:
                    b.append(a[i]*(-1))
            minindex=0
            for j in range(1,len(b)):
                if b[j]<b[minindex]:
                    minindex=j
            newb=[]
            for i in range(minindex+1,len(b)):
                newb.append(b[i])
            summa=0
            for k in range(0,len(newb)):
                summa+=newb[k]
            print("Исходная строка ", a)
            print('Количество отрицательных элементов :', countnegativ)
            print('Сумма модулей ', summa)
            break
        else:
            print('Ошибка!!!Введите положительно число')
    except ValueError:
        print('Ошибка!!! Введите число')
