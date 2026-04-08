import os

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')


def dibujar(lista, mov=0):
    print("\nMovimientos:", mov)
    print("-" * 30)
    for x in lista.datos:
        print(str(x).rjust(2), "|", "█" * x)
    print("-" * 30)