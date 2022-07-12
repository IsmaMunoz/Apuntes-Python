#Programando Closures
#Es una forma de acceder a variables de otros scopes a través 
#de una nested function. Se retorna la nested function y esta
#recuerda el valor que imprime, aunque a la hora de ejecutarla
#no este dentro de su alcance.
def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "Solo puedes utilizar cadenas"
        return string * n
    return repeater

def run():
    repeat_5 = make_repeater_of (5)
    print(repeat_5("Hola"))
    repeat_10 = make_repeater_of (10)
    print(repeat_10("Hola"))


if __name__ == "__main__":
    run()