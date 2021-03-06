# Tipado est谩tico en Python
# Podemos convertir a Python a un lenguaje de tipado est谩tico 馃く. Para eso, usamos Static Typing, y es muy sencillo, solo debemos a帽adir una sintaxis adicional, en la cual declaramos variables con su tipo.

# a: int = 5
# b: str = 'Hola'
# c: bool = True

# print(a, b, c)
# Esto funciona desde Python 3.6 馃憖. Para hacerlo con funciones (con sus variables y con lo que retorna la funci贸n):

# def suma(a: int, b: int) -> int:
# 	return a + b

# print(suma(1, 2))
# Si le pasamos strings a la funci贸n suma, si funcionar谩 y nos va a regresar las strings sumadas, para evitar esto, debemos a帽adir un m贸dulo.

# Podemos hacer tipado en estructuras de datos. Para definir que una variable es de un tipo (de una estructura de datos), desde la versi贸n 3.9, podemos hacerlo con las palabras claves de ese tipo. Antes de la versi贸n 3.9, es con:

# from typing import Dict, List

# positives: List[int] = [1, 2, 3, 4, 5]

# users: Dict[str, int] = {
# 	'argentina': 1,
# 	'mexico': 34,
# 	'colombia': 45
# }

# countries: List[Dict[str, str]] = [
# 	{
# 		'name':'Argentina'
# 		'people':'45000'
# 	},
# 	{
# 		'name':'M茅xico'
# 		'people':'900000'
# 	},
# 	{
# 		'name':'Colombia'
# 		'people':'9999999'
# 	}
# ]
# Podemos hacer lo mismo con las tuplas:

# from typing import Tuple

# numbers: Tuple[int, float, int] = (1, 0.5, 1)
# Podemos definir nuestros propios tipos de variable y usarlas:

# from typing import Tuple, Dict, List

# CoordinateType = List[Dict[str, Tuple[int, int]]]

# coordinates: CoordinateType = [
# 	{
# 		'coord1': (1, 2),
# 		'coord2': (3, 5)
# 	},
# 	{
# 		'coord1': (0, 1),
# 		'coord2': (2, 5)
# 	}
# ]
# Para que Python considere este tipado est谩tico y no se salte, es con el m贸dulo mypy que nos detiene cuando hay errores de tipado 馃憖.k

def is_palindrome(string: str) -> bool:
    string = string.replace(" ","").lower()
    return string == string[::-1]

def run():
    print(is_palindrome("Ana"))

if __name__ == "__main__":
    run()