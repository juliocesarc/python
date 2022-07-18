file = open('aula44/arquivo.txt', 'w+')
file.write('Linha1\n')
file.write('Linha2\n')
file.write('Linha3\n')

file.seek(0)
print('lendo linhas:')
print(file.read())
print('#' * 12)

file.seek(0)
print(file.readline(), end = '')
print(file.readline(), end = '')
print(file.readline(), end = '')
print('#' * 12)


file.seek(0)
for linha in file.readlines():
    print(linha, end = '')
print('#' * 12)

file.seek(0, 0)
for linha in file:
    print(linha, end = '')



file.close()
