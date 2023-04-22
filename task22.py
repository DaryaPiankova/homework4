n=int(input('Введите кол-во элементов первого множества: '))
m=int(input('Введите кол-во элементов второго множества: '))
list1=[]
list2=[]
for i in range(n):
    list1.append(int(input(f'Введите {i+1} элемент 1-го множества: ')))

for j in range(m):
    list2.append(int(input(f'Введите {j+1} элемент 2-го множества: ')))

set1=set(list1)
set2=set(list2)
new_set=set1.intersection(set2)
print(sorted(new_set))




