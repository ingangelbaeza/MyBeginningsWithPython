### Loops ###

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else:
    print("Mi condición es mayor o igual que 10")

print("La ejecución continúa")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución")
        break
    print(my_condition)

print("La ejecución continúa")


my_list = [30, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_tuple = (35, 1.77, "anbgel", "baeza", "anbgel")

for element in my_tuple:
    print(element)

my_set = {"anbgel", "baeza", 30}

for element in my_set:
    print(element)

my_dict = {"Nombre": "anbgel", "Apellido": "baeza", "Edad": 30, 1: "Python"}

for element in my_dict:
    print(element)
    if element == "Edad":
        break
else:
    print("El bluce for para diccionario ha finalizado")

print("La ejecución continúa")

for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta")
else:
    print("El bluce for para diccionario ha finalizado")