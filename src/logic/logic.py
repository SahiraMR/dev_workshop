class Logica:
    """
    Clase con métodos para realizar operaciones de lógica booleana y algoritmos.
    """
    
    def AND(self, a, b):
        """
        Implementa la operación lógica AND.
        
        Args:
            a (bool): Primer valor booleano
            b (bool): Segundo valor booleano
            
        Returns:
            bool: Resultado de a AND b
        """
         
        return a and b
        pass
    
    def OR(self, a, b):
        """
        Implementa la operación lógica OR.
        
        Args:
            a (bool): Primer valor booleano
            b (bool): Segundo valor booleano
            
        Returns:
            bool: Resultado de a OR b
        """
    
        return a or b

        pass
    
    def NOT(self, a):
        """
        Implementa la operación lógica NOT.
        
        Args:
            a (bool): Valor booleano
            
        Returns:
            bool: Resultado de NOT a
        """
    
        return a and b

    def OR(self, a, b):
        return a or b

    def NOT(self, a):
        return not a



        pass
    
    def XOR(self, a, b):
        """
        Implementa la operación lógica XOR (OR exclusivo).
        
        Args:
            a (bool): Primer valor booleano
            b (bool): Segundo valor booleano
            
        Returns:
            bool: Resultado de a XOR b
        """
        
        return a and b

    def OR(self, a, b):
        return a or b

    def NOT(self, a):
        return not a

    def XOR(self, a, b):
        return a != b  # XOR devuelve True si los valores son diferentes

        pass
    
    def NAND(self, a, b):
        """
        Implementa la operación lógica NAND (NOT AND).
        
        Args:
            a (bool): Primer valor booleano
            b (bool): Segundo valor booleano
            
        Returns:
            bool: Resultado de a NAND b
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



        pass
    
    def NOR(self, a, b):
        """
        Implementa la operación lógica NOR (NOT OR).
        
        Args:
            a (bool): Primer valor booleano
            b (bool): Segundo valor booleano
            
        Returns:
            bool: Resultado de a NOR b
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



        pass
    
    def XNOR(self, a, b):
        """
        Implementa la operación lógica XNOR (NOT XOR).
        
        Args:
            a (bool): Primer valor booleano
            b (bool): Segundo valor booleano
            
        Returns:
            bool: Resultado de a XNOR b
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


        pass
    
    def implicacion(self, a, b):
        """
        Implementa la operación lógica de implicación (a -> b).
        
        Args:
            a (bool): Primer valor booleano (antecedente)
            b (bool): Segundo valor booleano (consecuente)
            
        Returns:
            bool: Resultado de la implicación
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



        pass
    
    def bi_implicacion(self, a, b):
        """
        Implementa la operación lógica de bi-implicación (a <-> b).
        
        Args:
            a (bool): Primer valor booleano
            b (bool): Segundo valor booleano
            
        Returns:
            bool: Resultado de la bi-implicación
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



        pass
    
    
