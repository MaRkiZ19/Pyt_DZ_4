# В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод —
# -на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.

# n=int(input('Введите N: '))
# a=list(range(1,n+1))
# bushes=set(a)
# print(*bushes)
# import random
# berries=[]
# for i in range(n):
#     berries.append(random.randint(10,100))
# print(*berries)

# garden={state: city for city, state in zip(berries, bushes)}
# print(garden)
# z=1
# sum=[]*(n//3)
# res=0
#                                                                    # решить вопрос с подсчетом не вошедших кустов
# for i in range(len(garden)):
#     res = garden.get(z) + garden.get(z+1) + garden.get(z+2)        # ришить вопрос с синт.ошибкой
#     print(res)
#     sum.append(res)
#     z+=3
#     print(sum)



n=int(input('Введите количество кустов в грядке: '))

import random
berries=[]
for i in range(n):
    berries.append(random.randint(10,100))
#print(*berries)
assem=[]
for i in range(len(berries)-1):
    assem.append(berries[i-1]+berries[i]+berries[i+1])
assem.append(berries[-2]+berries[-1]+berries[0])
#print(assem)
print(max(assem))
       
