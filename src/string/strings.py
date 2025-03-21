class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """
    
    def es_palindromo(self, texto):
        """
        Verifica si una cadena es un palíndromo (se lee igual de izquierda a derecha y viceversa).
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si es palíndromo, False en caso contrario
        """
    
        texto = ''.join(c.lower() for c in texto if c.isalnum())  
        return texto == texto[::-1]

        pass
    
    def invertir_cadena(self, texto):
        """
        Invierte una cadena de texto sin usar slicing ni reversed().
        
        Args:
            texto (str): Cadena a invertir
            
        Returns:
            str: Cadena invertida
        """
    
        resultado = ""
        for caracter in texto:
            resultado = caracter + resultado  
        return resultado

        pass
    
    def contar_vocales(self, texto):
        """
        Cuenta el número de vocales en una cadena.
        
        Args:
            texto (str): Cadena para contar vocales
            
        Returns:
            int: Número de vocales en la cadena
        """
    
        vocales = "aeiouAEIOU"
        contador = 0
        for caracter in texto:
            if caracter in vocales:
                contador += 1
        return contador

        pass
    
    def contar_consonantes(self, texto):
        """
        Cuenta el número de consonantes en una cadena.
        
        Args:
            texto (str): Cadena para contar consonantes
            
        Returns:
            int: Número de consonantes en la cadena
        """

        vocales = "aeiouAEIOU"
        contador = 0
        for caracter in texto:
            if caracter.isalpha() and caracter not in vocales:
                contador += 1
        return contador

        pass
    
    def es_anagrama(self, texto1, texto2):
        """
        Verifica si dos cadenas son anagramas (contienen exactamente los mismos caracteres).
        
        Args:
            texto1 (str): Primera cadena
            texto2 (str): Segunda cadena
            
        Returns:
            bool: True si son anagramas, False en caso contrario
        """

        texto1 = ''.join(sorted(texto1.lower().replace(" ", "")))
        texto2 = ''.join(sorted(texto2.lower().replace(" ", "")))
        return texto1 == texto2

        pass
    
    def contar_palabras(self, texto):
        """
        Cuenta el número de palabras en una cadena.
        
        Args:
            texto (str): Cadena para contar palabras
            
        Returns:
            int: Número de palabras en la cadena
        """

        return len(texto.split())

        pass
    
    def palabras_mayus(self, texto):
        """
        Pon en Mayuscula la primera letra de cada palabra en una cadena.
        
        Args:
            texto (str): Cadena
            
        Returns:
            str: Cadena con la primera letra de cada palabra en mayúscula
        """
 
        return ' '.join(palabra.capitalize() for palabra in texto.split())

        pass
    
    def eliminar_espacios_duplicados(self, texto):
        """
        Elimina espacios duplicados en una cadena.
        
        Args:
            texto (str): Cadena con posibles espacios duplicados
            
        Returns:
            str: Cadena sin espacios duplicados
        """

        return ' '.join(texto.split())

        pass
    
    def es_numero_entero(self, texto):
        """
        Verifica si una cadena representa un número entero sin usar isdigit().
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si la cadena representa un número entero, False en caso contrario
        """
 
        if not texto:
            return False
        if texto[0] in ('-', '+'):
            texto = texto[1:]
        return all('0' <= c <= '9' for c in texto)
  
    pass
    
    def cifrar_cesar(self, texto, desplazamiento):
        """
        Aplica el cifrado César a una cadena de texto.
        
        Args:
            texto (str): Cadena a cifrar
            desplazamiento (int): Número de posiciones a desplazar cada letra
            
        Returns:
            str: Cadena cifrada
        """
    def descifrar_cesar(texto, desplazamiento):
     return "".join(
        chr((ord(c) - (ord('A') if c.isupper() else ord('a')) - desplazamiento) % 26 + (ord('A') if c.isupper() else ord('a')))
        if c.isalpha() else c for c in texto
    )
    pass

    
    def encontrar_subcadena(self, texto, subcadena):
        """""
        Encuentra todas las posiciones de una subcadena en un texto sin usar find() o index().
        
        Args:
            texto (str): Cadena principal
            subcadena (str): Subcadena a buscar
            
        Returns:
            list: Lista con las posiciones iniciales de cada ocurrencia
        """

        posiciones = []
        for i in range(len(texto) - len(subcadena) + 1):
            if texto[i:i + len(subcadena)] == subcadena:
                posiciones.append(i)
        return posiciones

        pass