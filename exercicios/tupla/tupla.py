from collections import namedtuple

minha_tupla = ([1,2,3],['a','b','c'])
print(minha_tupla)
print(id(minha_tupla))
minha_tupla[0].append(4)
print(minha_tupla)
print(id(minha_tupla))

Coordenadas = namedtuple('Coordenadas', ['latitude','longitude'])
caelum_coordenadas = Coordenadas(-23.588254, -46.632477)
print(caelum_coordenadas)
print(caelum_coordenadas[0])
print(caelum_coordenadas.latitude)
print(caelum_coordenadas[1])
print(caelum_coordenadas.longitude)