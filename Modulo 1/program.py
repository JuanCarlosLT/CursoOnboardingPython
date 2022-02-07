# program.py
from datetime import date
sum = 1 + 2
print(sum)
print('Hola desde la consola')
sum = 1 + 2 # 3
product = sum * 2
print(product)
planetas_en_el_sistema_solar = 8 # int, plutón era considerado un planeta pero ya es muy pequeño
distancia_a_alfa_centauri = 4.367 # float, años luz
puede_despegar = True #Boolean
transbordador_que_aterrizo_en_la_luna = "Apollo 11" #string
tipo = type(distancia_a_alfa_centauri)
print(tipo)
left_side = 10
right_side = 5
divicion = left_side / right_side # 2
print(divicion)
print(date.today())
print("Today's date is: " + str(date.today()))
print("Bienvenido al programa de bienvenida")
name = input("Introduzca su nombre ")
print("Saludos: " + name)
print("Calculadora")
first_number = input("Primer número: ")
second_number = input("Segundo número: ")
print(first_number + second_number)
print(int(first_number) + int(second_number))