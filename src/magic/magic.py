class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números perfectos, triangulo de pascal etc.
    """
    
    def fibonacci(self, n):
        """
        Calcula el n-ésimo número de la secuencia de Fibonacci.
        
        Args:
            n (int): Posición en la secuencia (empezando desde 0)
            
        Returns:
            int: El n-ésimo número de Fibonacci
        """
     
        return a and b

    def OR(self, a, b):
        return a or b

    def NOT(self, a):
        return not a

    def XOR(self, a, b):
        return a != b  # XOR devuelve True si los valores son diferentes

    def NAND(self, a, b):
        return not (a and b)  # NAND es la negación de AND

    def NOR(self, a, b):
        return not (a or b)  # NOR es la negación de OR

    def XNOR(self, a, b):
        return not (a != b)  # XNOR es la negación de XOR

    def implicacion(self, a, b):
        return (not a) or b  # La implicación lógica se define como ¬a ∨ b

    def bi_implicacion(self, a, b):
        return a == b  # La bi-implicación es verdadera cuando ambos valores son iguales

    def fibonacci(self, n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 0, 1
            for _ in range(n - 1):
                a, b = b, a + b
            return b



        pass
    
    def secuencia_fibonacci(self, n):
        """
        Genera los primeros n números de la secuencia de Fibonacci.
        
        Args:
            n (int): Cantidad de números a generar
            
        Returns:
            list: Lista con los primeros n números de Fibonacci
        """
     
        return a and b

    def OR(self, a, b):
        return a or b

    def NOT(self, a):
        return not a

    def XOR(self, a, b):
        return a != b  # XOR devuelve True si los valores son diferentes

    def NAND(self, a, b):
        return not (a and b)  # NAND es la negación de AND

    def NOR(self, a, b):
        return not (a or b)  # NOR es la negación de OR

    def XNOR(self, a, b):
        return not (a != b)  # XNOR es la negación de XOR

    def implicacion(self, a, b):
        return (not a) or b  # La implicación lógica se define como ¬a ∨ b

    def bi_implicacion(self, a, b):
        return a == b  # La bi-implicación es verdadera cuando ambos valores son iguales

    def fibonacci(self, n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 0, 1
            for _ in range(n - 1):
                a, b = b, a + b
            return b

    def secuencia_fibonacci(self, n):
        if n <= 0:
            return []
        secuencia = [0, 1]
        for _ in range(n - 2):
            secuencia.append(secuencia[-1] + secuencia[-2])
        return secuencia[:n]



        pass
    
    def es_primo(self, n):
        """
        Verifica si un número es primo.
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es primo, False en caso contrario
        """
   
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True



        pass
    
    def generar_primos(self, n):
        """
        Genera una lista de números primos hasta n.
        
        Args:
            n (int): Límite superior para generar primos
            
        Returns:
            list: Lista de números primos hasta n
        """
       
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def generar_primos(self, n):
        return [i for i in range(2, n + 1) if self.es_primo(i)]



        pass
    
    def es_numero_perfecto(self, n):
        """
        Verifica si un número es perfecto (igual a la suma de sus divisores propios).
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es un número perfecto, False en caso contrario
        """
   
        if n < 2:
            return False
        suma_divisores = sum(i for i in range(1, n) if n % i == 0)
        return suma_divisores == n


        pass
    
    def triangulo_pascal(self, filas):
        """
        Genera las primeras n filas del triángulo de Pascal.
        
        Args:
            filas (int): Número de filas a generar
            
        Returns:
            list: Lista de listas que representa el triángulo de Pascal
        """
    
        if filas <= 0:
            return []
        triangulo = [[1]]
        for i in range(1, filas):
            fila = [1]
            for j in range(1, i):
                fila.append(triangulo[i - 1][j - 1] + triangulo[i - 1][j])
            fila.append(1)
            triangulo.append(fila)
        return triangulo



        pass
    
    def factorial(self, n):
        """
        Calcula el factorial de un número.
        
        Args:
            n (int): Número para calcular su factorial
            
        Returns:
            int: El factorial de n
        """
   
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado



        pass
    
    def mcd(self, a, b):
        """
        Calcula el máximo común divisor de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El máximo común divisor de a y b
        """

        while b:
            a, b = b, a % b
        return abs(a)



        pass
    
    def mcm(self, a, b):
        """
        Calcula el mínimo común múltiplo de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El mínimo común múltiplo de a y b
        """
   
        while b:
            a, b = b, a % b
        return abs(a)

    def mcm(self, a, b):
        return abs(a * b) // self.mcd(a, b) if a and b else 0



        pass
    
    def suma_digitos(self, n):
        """
        Calcula la suma de los dígitos de un número.
        
        Args:
            n (int): Número para sumar sus dígitos
            
        Returns:
            int: La suma de los dígitos de n
        """
        pass
    
    def es_numero_armstrong(self, n):
        """
        Verifica si un número es de Armstrong (igual a la suma de sus dígitos elevados a la potencia del número de dígitos).
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es un número de Armstrong, False en caso contrario
        """
        pass
    
    def es_cuadrado_magico(self, matriz):
        """
        Verifica si una matriz es un cuadrado mágico (suma igual en filas, columnas y diagonales).
        
        Args:
            matriz (list): Lista de listas que representa una matriz cuadrada
            
        Returns:
            bool: True si es un cuadrado mágico, False en caso contrario
        """
        pass