### Tuples ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, "angel", "baeza", "angel")
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("angel"))
print(my_tuple.index("baeza"))
print(my_tuple.index("angel"))

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "abaeza"
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

del my_tuple
