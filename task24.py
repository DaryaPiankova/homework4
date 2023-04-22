x=int(input('введите число кустов: '))
list1=[]
for i in range(x):
    list1.append(int(input(f'Введит кол-во ягод на {i} кусте: ')))
print(list1)
y=0
z=0
sum=0
max_sum=0
for j in list1:
    if j+y+z>max_sum:
        max_sum=j+y+z
    z=y
    y=j
print (max_sum)

