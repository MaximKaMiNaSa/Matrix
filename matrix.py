#На вход программе подаются два натуральных числа nn и mm — количество строк и столбцов в матрице. Создайте матрицу mult размером n \times mn×m и заполните её таблицей умножения по формуле mult[i][j] = i * j.
#Программа должна вывести таблицу умножения отводя на вывод каждого числа ровно 33 символа (для этого используйте строковый метод ljust()).

n = int(input())
m = int(input())

mult = []

for i in range(n):
    for j in range(m):
        mult.append([0]*m)

for i in range(n):
    for j in range(m):
        mult[i][j] = i * j

for x in range(n):
    print(*mult[x], sep=str().ljust(3))