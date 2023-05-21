import math

def trojkat(bok_a, bok_b, bok_c, h_a):
    pole = bok_a * h_a / 2
    obwod = bok_a+bok_b+bok_c
    return pole, obwod

print(f'Pole i obwód trójkąta wynosi: {trojkat(10,12,16,8)}')

def kolo(r):
    pole = math.pi*r**2
    obwod = 2*math.pi*r 
    return pole, obwod

print(f'Pole i obwód koła wynosi: {kolo(10)}')

def trapez(a_dol, b_gora, c_bok_1, d_bok_2, h):
    pole = ((a_dol+b_gora)/2)*h
    obwod = a_dol+b_gora+c_bok_1+d_bok_2
    return pole, obwod

print(f'Pole i obwód trapeza wynosi: {trapez(10,12,16,8,8)}')

def prostokat(a,b):
    pole = a*b
    obwod = 2*a+2*b
    return pole, obwod

print(f'Pole i obwód prostokąta wynosi: {prostokat(10,12)}')

def kwadrat(a):
    pole = a**2
    obwod = 4*a
    return pole, obwod

print(f'Pole i obwód kwadratu wynosi: {kwadrat(10)}')

def romb(a, h):
    pole = a*h
    obwod = 4*a
    return pole, obwod

print(f'Pole i obwód romba wynosi: {romb(10,8)}')
