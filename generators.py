# Los generadores son "sugar syntax" de los iteradores
#En este archivo crearemos la sesión de Fibonacci ahora
#en formato de generador

from html.entities import name2codepoint
import time

def fibogen():
    n1 = 0
    n2 = 1
    counter = 0
    while True:
        if counter == 0:
            counter += 1
            yield n1
        elif counter ==1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            n1, n2 = n2, aux
            counter += 1
            yield aux

if __name__ == "__main__":
    fibonacci = fibogen()
    for element in fibonacci:
        print (element)
        time.sleep (.5)