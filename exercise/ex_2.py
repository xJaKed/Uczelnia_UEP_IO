import math
# trojkat

a = 10
b = 20
c = 15
h = 12

obwod = a + b + c
pole = int((h * a) / 2)

print("Obwod trojkata wynosi " + str(obwod) + ", zas pole wynosi " + str(pole) + ".")

# romb

a_romb=10
h_romb=5
pole_rombu = int(a_romb*h_romb)
obwod_rombu = a*4
print("Obwod rombu wynosi " + str(obwod_rombu) + ", zas pole wynosi " + str(pole_rombu) + ".")

# kolo

pi=round(float(math.pi),2)
r_kolo = 5
pole_kolo = pi*(r_kolo)**2
obwod_kolo = 2*pi*r_kolo
print("Obwod kola wynosi " + str(obwod_kolo) + ", zas pole wynosi " + str(pole_kolo) + ".")

# prostokat

a_prost = 5
b_prost = 15
pole_prost=a_prost*b_prost
obwod_prost=2*a_prost+2*b_prost
print("Obwod prostokata wynosi " + str(obwod_prost) + ", zas pole wynosi " + str(pole_prost) + ".")