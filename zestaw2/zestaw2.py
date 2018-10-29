#2.10:
print('zad 2.10')
line = 'poszla ola do przedszkola ' \
       'zapomniala parasola'
print(line.split()) #wyswietlenie tablicy osobnych wyrazow(niekonieczne dla zadania)
print(len(line.split())) #liczba wyrazow, rozwiazanie postawionego problemu
#2.11:
print('\nzad.2.11')
napis = 'word'
result = '_'.join(napis)
print(result)
#2.12
print('\nzad.2.12')
line = 'Poszla ola do przedszkola ' \
       'zapomniala parasola'
result = ''.join(line[0] for line in line.split()) #wyraz z pierwszych liter wyrazow
result2 = ''.join(line[len(line)-1] for line in line.split()) #wyraz z ostatnich liter wyrazow
print(result)
print(result2)
#2.13
print('\nzad.2.13')
line = 'Poszla ola do przedszkola ' \
       'zapomniala parasola'
lineTab = line.split()
allDig = ''.join(lineTab)
print(len(allDig)) #rozwiazanie problemu liczba znakow
#2.14
print('\n2.14')
line = 'poszla ola do przedszkola ' \
       'zapomniala parasola '
wordsTab = line.split()
print(wordsTab)
count = ''
for i in wordsTab:
    if len(i) > len(count):
        count = i

print(count)
print(len(count))
#2.15
print('\nzad 2.15')
L = [4, 3, 2, 5, 3]
napis = ''.join(str(i) for i in L)
print(napis)
#2.16
print('\nzad 2.16')
line = 'GvR'
g = line[0] + 'uido '
v = line[1] + 'an '
r = line[2] + 'ossum'
napis = g+v+r
print(napis)
#2.17
print('\nzad 2.17')
line = 'Poszla ola do przedszkola ' \
       'zapomniala parasola'

lowLine = line.lower()
words = lowLine.split()
words.sort()
print(words)
words.sort(key=len)
print(words)
#2.18
print('\nzad 2.18')
l = 27300302300
result = str(l)
lz = 0
for i in result:
    if i == '0':
        lz += 1
print('\nliczba zer w liczbie', lz)
#2.19
print('\nzad 2.19')
L = [34, 40, 1, 4, 983, 678]
L2 = ' '.join(str(i).zfill(3) for i in L)
print(L2)
