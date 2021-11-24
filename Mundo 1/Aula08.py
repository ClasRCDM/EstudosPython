# import math
import emoji

from math import sqrt
from random import random

print('{0} AUla 08 {0}'.format('=' * 10))
print(emoji.emojize('HAHA :sunglasses:', use_aliases=True))

num = int(input('Digite um número: '))
# raiz = math.sqrt(num)
raiz = sqrt(num)
print(f'A raiz de {num} é {raiz:.2f}')
print('-' * 5)
print(random())
