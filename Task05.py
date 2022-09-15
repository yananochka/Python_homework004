
# 34. Даны два файла в каждом из которых находится запись многочлена. 
# Сформировать файл, содержащий сумму многочленов

from operator import le
import re
import itertools


file1 = 'Mnogo.txt'
file2 = 'Mnogo_2.txt'

with open(str(file1), 'r') as data:
    pol = data.read()
with open(str(file2), 'r') as data:
    pol2 = data.read()

print(pol)
print(pol2)

pol = pol.replace('= 0', '')
pol = re.sub("[*|^| ]", " ", pol).split('+')
pol = [char.split(' ') for char in pol]
pol = [[x for x in list if x] for list in pol]
for i in pol:
    if i[0] == 'x': i.insert(0, 1)
    if i[-1] == 'x': i.append(1)
    if len(i) == 1: i.append(0)
pol = [tuple(int(x) for x in j if x != 'x') for j in pol]

pol2 = pol2.replace('= 0', '')
pol2 = re.sub("[*|^| ]", " ", pol2).split('+')
pol2 = [char.split(' ') for char in pol2]
pol2 = [[x for x in list if x] for list in pol2]
for i in pol2:
    if i[0] == 'x': i.insert(0, 1)
    if i[-1] == 'x': i.append(1)
    if len(i) == 1: i.append(0)
pol2 = [tuple(int(x) for x in j if x != 'x') for j in pol2]




raspack_pol = list(zip(*pol))
raspack_pol2 = list(zip(*pol2))
new_pol = []

chisla_pol = raspack_pol[0]
chisla_pol2 = raspack_pol2[0]
stepeni_pol = raspack_pol[1]
stepeni_pol2 = raspack_pol2[1]


if len(chisla_pol) > len(chisla_pol2):
    k = len(chisla_pol) - len(chisla_pol2)
    l = len(chisla_pol) - 1
    for i in range(k):
        new_pol.append(f'{chisla_pol[i]}*x^{l} + ')
        l -= 1
    for i in range(len(chisla_pol2)):
        while l > 1:
             new_pol.append(f'{chisla_pol2[i] + chisla_pol[k + i]}*x^{l} + ')
             l -= 1

if len(chisla_pol) < len(chisla_pol2):
    k = len(chisla_pol2) - len(chisla_pol)
    l = len(chisla_pol2) - 1
    for i in range(k):
        new_pol.append(f'{chisla_pol2[i]}*x^{l} + ')
        l -= 1
    for i in range(len(chisla_pol)):
        while l > 1:
             new_pol.append(f'{chisla_pol[i] + chisla_pol2[k + i]}*x^{l} + ')
             l -= 1
if len(chisla_pol) == len(chisla_pol2):
    for i in range(len(chisla_pol)-2):
        l = len(chisla_pol2) - 1
        new_pol.append(f'{chisla_pol2[i]}*x^{l-i} + ')
        l -= 1
new_pol.append(f'{chisla_pol[-2] + chisla_pol2[-2]}*x + ')
new_pol.append(f'{chisla_pol[-1] + chisla_pol2[-1]} = 0')
new_pol = [''.join(new_pol)]
print(new_pol)
