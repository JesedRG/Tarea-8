import time
import random
from lista import Lista
from funcionesUtiles import limpiar, dibujar

try:
    import matplotlib.pyplot as plt
except:
    plt = None


def menu():
    print("====== ORDENAMIENTOS ======")
    print("1) Bubble Sort")
    print("2) Selection Sort")
    print("3) Insertion Sort")
    print("4) Merge Sort")
    print("5) Quick Sort")
    print("6) Grafica")
    print("7) Salir")
    print("===========================")


def grafica():
    if plt is None:
        print("No tienes matplotlib")
        input()
        return

    tamaños = [10, 20, 30, 40, 50]
    resultados = {"Bubble": [], "Selection": [], "Insertion": [], "Merge": [], "Quick": []}

    for n in tamaños:
        base = [random.randint(1, 100) for _ in range(n)]

        for nombre in resultados:
            l = Lista(*base)
            inicio = time.time()

            if nombre == "Bubble":
                l.bubble()
            elif nombre == "Selection":
                l.selection()
            elif nombre == "Insertion":
                l.insertion()
            elif nombre == "Merge":
                l.merge()
            elif nombre == "Quick":
                l.quick()

            fin = time.time()
            resultados[nombre].append(fin - inicio)

    for k in resultados:
        plt.plot(tamaños, resultados[k], label=k)

    plt.legend()
    plt.show()


def ejecutar(op):
    nombres = {
        "1": "Bubble Sort",
        "2": "Selection Sort",
        "3": "Insertion Sort",
        "4": "Merge Sort",
        "5": "Quick Sort"
    }

    try:
        n = int(input("Tamaño de lista (5-25): "))
    except:
        return

    if n < 5 or n > 25:
        return

    v = input("Velocidad 1(lento) 2(medio) 3(rapido): ")
    vel = {"1": 0.6, "2": 0.2, "3": 0.05}
    d = vel.get(v, 0.2)

    nums = []
    for i in range(n):
        nums.append(random.randint(1, 30))

    lista = Lista(*nums)

    limpiar()
    print("Algoritmo:", nombres[op])
    print("Lista inicial:", lista)
    dibujar(lista)

    input("\nEnter para empezar...")

    def anim(m):
        limpiar()
        print("Algoritmo:", nombres[op])
        dibujar(lista, m)
        time.sleep(d)

    if op == "1":
        total = lista.bubble(anim)
    elif op == "2":
        total = lista.selection(anim)
    elif op == "3":
        total = lista.insertion(anim)
    elif op == "4":
        total = lista.merge(anim)
    elif op == "5":
        total = lista.quick(anim)

    print("\nTerminado")
    print("Movimientos:", total)

    input("\nEnter para regresar al menú...")