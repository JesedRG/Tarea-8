from menu import menu, ejecutar, grafica
from funcionesUtiles import limpiar

def main():
    while True:
        limpiar()
        menu()
        op = input("Elige opción: ")

        if op == "7":
            break

        if op == "6":
            grafica()
            continue

        if op in ["1", "2", "3", "4", "5"]:
            ejecutar(op)


if __name__ == "__main__":
    main()