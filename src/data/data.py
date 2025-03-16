class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """
    
    def invertir_lista(self, lista):
        """
        Invierte el orden de los elementos en una lista sin usar reversed() o lista[::-1].
        
        Args:
            lista (list): Lista a invertir
            
        Returns:
            list: Lista con los elementos en orden inverso
        """
        lista_invertida = []
        for i in range(len(lista) - 1, -1, -1):
            lista_invertida.append(lista[i])
        return lista_invertida
    
        pass
    
    def buscar_elemento(self, lista, elemento):
        
        for i in range(len(lista)):
            if lista[i] == elemento:
                return i
        return -1
    
    pass

    
   
    def eliminar_duplicados(self, lista):
        """
        Elimina elementos duplicados de una lista sin usar set().
        Mantiene el orden original de aparición.
        """
        resultado = []
        seen = {}  
        for elem in lista:
            key = (elem, type(elem))  
            if key not in seen:
                seen[key] = True
                resultado.append(elem)
        return resultado
    
    pass




 

    
    pass

    def merge_ordenado(self, lista1, lista2):
        """
        Combina dos listas ordenadas en una sola lista ordenada.
        
        Args:
            lista1 (list): Primera lista ordenada
            lista2 (list): Segunda lista ordenada
            
        Returns:
            list: Lista combinada y ordenada
        """
        
        lista_mergeada = []
        i, j = 0, 0

        while i < len(lista1) and j < len(lista2):
            if lista1[i] < lista2[j]:
                lista_mergeada.append(lista1[i])
                i += 1
            else:
                lista_mergeada.append(lista2[j])
                j += 1

        while i < len(lista1):
            lista_mergeada.append(lista1[i])
            i += 1

        while j < len(lista2):
            lista_mergeada.append(lista2[j])
            j += 1

        return lista_mergeada
        pass
    
    def rotar_lista(self, lista, k):
        """
        Rota los elementos de una lista k posiciones a la derecha.
        
        Args:
            lista (list): Lista a rotar
            k (int): Número de posiciones a rotar
            
        Returns:
            list: Lista rotada
        """
   
    
        if not lista:
            return lista
        
        n = len(lista)
        k = k % n  

        resultado = lista[-k:] + lista[:-k]
        return resultado

        pass
    
    def encuentra_numero_faltante(self, lista):
        """
        Encuentra el número faltante en una lista de enteros del 1 al n.
        
        Args:
            lista (list): Lista de enteros del 1 al n con un número faltante
            
        Returns:
            int: El número que falta en la secuencia
        """
        pass
    
    def es_subconjunto(self, conjunto1, conjunto2):
        """
        Verifica si conjunto1 es subconjunto de conjunto2 sin usar set.
        
        Args:
            conjunto1 (list): Posible subconjunto
            conjunto2 (list): Conjunto principal
            
        Returns:
            bool: True si conjunto1 es subconjunto de conjunto2, False en caso contrario
        """
        pass
    
    def implementar_pila(self):
        """
        Implementa una estructura de datos tipo pila (stack) usando listas.
        
        Returns:
            dict: Diccionario con métodos push, pop, peek y is_empty
        """
        pass
    
    def implementar_cola(self):
        """
        Implementa una estructura de datos tipo cola (queue) usando listas.
        
        Returns:
            dict: Diccionario con métodos enqueue, dequeue, peek y is_empty
        """
        pass
    
    def matriz_transpuesta(self, matriz):
        """
        Calcula la transpuesta de una matriz.
        
        Args:
            matriz (list): Lista de listas que representa una matriz
            
        Returns:
            list: Matriz transpuesta
        """
        pass