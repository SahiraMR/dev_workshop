class Data:
    """
    Clase con, métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """
    
    def invertir_lista(self, lista):
        """
        Invierte el orden de los elementos en una lista sin usar reversed() o lista[::-1].
        """
        lista_invertida = []
        for i in range(len(lista) - 1, -1, -1):
            lista_invertida.append(lista[i])
        return lista_invertida
    
    def buscar_elemento(self, lista, elemento):
        """
        Busca un elemento en una lista y devuelve su índice (o -1 si no existe).
        Implementación manual sin usar index().
        """
        for i in range(len(lista)):
            if lista[i] == elemento:
                return i
        return -1
    
    def eliminar_duplicados(self, lista):
        """
        Elimina elementos duplicados de una lista sin usar set().
        Mantiene el orden original de aparición.
        """
        lista_sin_duplicados = []
        for elemento in lista:
            if elemento not in lista_sin_duplicados:
                lista_sin_duplicados.append(elemento)
        return lista_sin_duplicados
    
    def merge_ordenado(self, lista1, lista2):
        """
        Combina dos listas ordenadas en una sola lista ordenada.
        """
        resultado = []
        i, j = 0, 0
        while i < len(lista1) and j < len(lista2):
            if lista1[i] < lista2[j]:
                resultado.append(lista1[i])
                i += 1
            else:
                resultado.append(lista2[j])
                j += 1
        resultado.extend(lista1[i:])
        resultado.extend(lista2[j:])
        return resultado
    
    def rotar_lista(self, lista, k):
        """
        Rota los elementos de una lista k posiciones a la derecha.
        """
        k = k % len(lista)
        return lista[-k:] + lista[:-k]
    
    def encuentra_numero_faltante(self, lista):
        """
        Encuentra el número faltante en una lista de enteros del 1 al n.
        """
        n = len(lista) + 1
        suma_total = n * (n + 1) // 2
        suma_lista = sum(lista)
        return suma_total - suma_lista
    
    def es_subconjunto(self, conjunto1, conjunto2):
        """
        Verifica si conjunto1 es subconjunto de conjunto2 sin usar set.
        """
        for elemento in conjunto1:
            if elemento not in conjunto2:
                return False
        return True
    
    def implementar_pila(self):
        """
        Implementa una estructura de datos tipo pila (stack) usando listas.
        """
        pila = []
        return {
            "push": lambda x: pila.append(x),
            "pop": lambda: pila.pop() if pila else None,
            "peek": lambda: pila[-1] if pila else None,
            "is_empty": lambda: len(pila) == 0
        }
    
    def implementar_cola(self):
        """
        Implementa una estructura de datos tipo cola (queue) usando listas.
        """
        cola = []
        return {
            "enqueue": lambda x: cola.append(x),
            "dequeue": lambda: cola.pop(0) if cola else None,
            "peek": lambda: cola[0] if cola else None,
            "is_empty": lambda: len(cola) == 0
        }
    
    def matriz_transpuesta(self, matriz):
        """
        Calcula la transpuesta de una matriz.
        """
        return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
