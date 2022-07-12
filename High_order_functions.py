#Filter

# A partir de esta lista [1, 4, 5, 6, 9, 13, 19, 21]
# Crear una lista con impares [1, 5, 9, 19, 21]

# my_list = [1, 4, 5, 6, 9, 13, 19, 21]
# odd = list(filter(lambda x: x%2 != 0, my_list))
# print(odd)



#Map

# A partir de esta lista [1, 2, 3, 4, 5]
# Crear una lista con cuadrados de estos números [1, 4, 9, 16, 25]

# my_list = [1, 2, 3, 4, 5]
# Square = list(map(lambda x: x**2, my_list))
# print(Square)


#Reduce

# A partir de esta lista [2, 2, 2, 2, 2]
# Reducir al producto "32"

from functools import reduce

my_list = [2,2,2,2,2]
all_multiplied = reduce(lambda a, b: a * b, my_list)
print(all_multiplied)
