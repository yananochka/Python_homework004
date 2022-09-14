# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.

import random

k = int(input('Введите степень k: '))
result = [f'{random.randint(-100, 101)}*x^{k}']
if k >= 3:
    for i in range(2, k):
        A = random.randint(-100, 101)
        if A < 0:
            result.append(f'{A}*x^{k+1-i}')  
        elif A > 0:
            result.append(f'+{A}*x^{k+1-i}')
        else:
            result.append('')
B = random.randint(-100, 101)
if B > 0:
    result.append(f'+{B}x')
elif B < 0:
    result.append(f'{B}x')
else:
    result.append('')

C = random.randint(-100, 101)
if C > 0:
    result.append(f'+{C}')
elif C < 0:
    result.append(f'{C}')
else: result.append('')

result = [''.join(result)]
print(result)

with open ('Task04.txt', 'w') as data:
    data.write(f'{result}')