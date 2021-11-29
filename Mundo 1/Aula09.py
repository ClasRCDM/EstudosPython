print('{0} Aula 9 {0}'.format('=' * 10))

frase = 'Curso em Vídeo Python'
print(frase[::4])
print(frase[::-4])

print(frase.count('o'))
print(frase.upper().count('O'))

print(len(frase))

frase_space = '    Curso em Vídeo Python     '
print(frase_space.strip())

print('Curso' in frase)
print(frase.find('Vídeo'))

print(frase.split())
