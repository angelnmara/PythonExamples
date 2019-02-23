squares = []
for x in range(10):
    squares.append(x**2)

print(squares)    

squares2 = list(map(lambda x:x*5, range(10)))

print(squares2)

squares3 = [x**2 for x in range(10)]

print(squares3)

lista = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(lista)

combs = []
for x in [1,2,3]:
        for y in [3,1,4]:
            if x!= y:
                    combs.append((x,y))

print(combs)

vec = [-4,-2,0,2,4]
print(vec)
vec2 = [x*2 for x in vec]
print(vec2)
vec3 = [x for x in vec if x >= 0]
print(vec3)
vec4 = [abs(x) for x in vec]
print(vec4)
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print(freshfruit)
freshfruitWeapon = [weapon.strip() for weapon in freshfruit]    # quita espacios
print(freshfruitWeapon)
cuadrado = [(x, x**2) for x in range(6)]
print(cuadrado)
vec5 = [[1,2,3], [4,5,6], [7,8,9]]
print(vec5)
vec6 = [num for elem in vec5 for num in elem]
print(vec6)

from math import pi
pilist = [str(round(pi,i)) for i in range(1,6)]
print(pilist)