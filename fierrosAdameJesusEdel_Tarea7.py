import os
import time
import random

try:
    import matplotlib.pyplot as plt
except:
    plt = None

class Lista:
    def __init__(self, *valores):
        self.datos = []
        for v in valores:
            self.datos.append(v)

    def tamaño(self):
        return len(self.datos)

    def cambiar(self, i, j):
        aux = self.datos[i]
        self.datos[i] = self.datos[j]
        self.datos[j] = aux

    def __str__(self):
        return str(self.datos)

    def bubble(self, cb=None):
        mov = 0
        n = self.tamaño()
        for i in range(n):
            for j in range(n - 1):
                if self.datos[j] > self.datos[j + 1]:
                    self.cambiar(j, j + 1)
                    mov += 1
                    if cb:
                        cb(mov)
        return mov

    def selection(self, cb=None):
        mov = 0
        n = self.tamaño()
        for i in range(n):
            m = i
            for j in range(i + 1, n):
                if self.datos[j] < self.datos[m]:
                    m = j
            if m != i:
                self.cambiar(i, m)
                mov += 1
                if cb:
                    cb(mov)
        return mov

    def insertion(self, cb=None):
        mov = 0
        n = self.tamaño()
        for i in range(1, n):
            j = i
            while j > 0 and self.datos[j - 1] > self.datos[j]:
                self.cambiar(j, j - 1)
                mov += 1
                if cb:
                    cb(mov)
                j -= 1
        return mov

    def merge(self, cb=None):
        mov = [0]

        def ordenar(arr):
            if len(arr) > 1:
                mitad = len(arr) // 2
                izq = arr[:mitad]
                der = arr[mitad:]

                ordenar(izq)
                ordenar(der)

                i = j = k = 0

                while i < len(izq) and j < len(der):
                    if izq[i] < der[j]:
                        arr[k] = izq[i]
                        i += 1
                    else:
                        arr[k] = der[j]
                        j += 1
                    k += 1
                    mov[0] += 1
                    if cb:
                        cb(mov[0])

                while i < len(izq):
                    arr[k] = izq[i]
                    i += 1
                    k += 1
                    mov[0] += 1
                    if cb:
                        cb(mov[0])

                while j < len(der):
                    arr[k] = der[j]
                    j += 1
                    k += 1
                    mov[0] += 1
                    if cb:
                        cb(mov[0])

        ordenar(self.datos)
        return mov[0]

    def quick(self, cb=None):
        mov = [0]

        def ordenar(bajo, alto):
            if bajo < alto:
                p = dividir(bajo, alto)
                ordenar(bajo, p - 1)
                ordenar(p + 1, alto)

        def dividir(bajo, alto):
            pivote = self.datos[alto]
            i = bajo - 1
            for j in range(bajo, alto):
                if self.datos[j] <= pivote:
                    i += 1
                    self.cambiar(i, j)
                    mov[0] += 1
                    if cb:
                        cb(mov[0])
            self.cambiar(i + 1, alto)
            mov[0] += 1
            if cb:
                cb(mov[0])
            return i + 1

        ordenar(0, self.tamaño() - 1)
        return mov[0]


def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')


def dibujar(lista, mov=0):
    print("\nMovimientos:", mov)
    print("-" * 30)
    for x in lista.datos:
        print(str(x).rjust(2), "|", "█" * x)
    print("-" * 30)


def menu():
    print("\n====== ORDENAMIENTOS ======")
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