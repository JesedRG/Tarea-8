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