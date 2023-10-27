class Triangulo:
    
    """
    - All sides zero
    - No side may have a length of zero
    - Each side must be shorter than the sum of all sides divided by 2;
    - One side equals the sum of the other
    
Propriedade da soma dos ângulos internos: A soma dos três ângulos internos de um triângulo sempre totaliza 180 graus. 
Esta propriedade é conhecida como a "Soma dos Ângulos Internos de um Triângulo".

Propriedade da desigualdade triangular: Em um triângulo, 
a soma de quaisquer dois lados deve ser maior que o comprimento do terceiro lado. 
Esta propriedade é crucial para determinar se determinados comprimentos podem formar um triângulo.

    """
    
    def __init__ (self, a, b, c):
        
        self.a = a
        self.b = b
        self.c = c
        
    def identify_triangule(self):
        
    
        #No side may have a length of zero
    
        
        if self.a == 0 or self.b == 0 or self.c == 0: #No side may have a length of zero
            
            return 'Isnt triangle cuz No side may have a length of zero'
        
        #- Each side must be shorter than the sum of all sides divided by 2;
        
        sum_of_all_sides = (self.a + self.b + self.c) / 2
        
        if self.a > sum_of_all_sides or self.b > sum_of_all_sides or self.c > sum_of_all_sides:
            
            return 'Isnt triangle cuz Each side must be shorter than the sum of all sides divided by 2'
        
        #Propriedade da desigualdade triangular
        
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            
            return 'Isnt triangle cuz the sum of any two sides must be greater than the length of the third side'
        
        #### Classificação por lados:
        
        #Equilatero 
        
        if self.a == self.b and self.a == self.c and self.b == self.c:
            
            #print('>>> Equilatero')
            pass
            
        #Isósceles 
        elif self.a == self.b and self.a != self.c or self.a == self.c and self.a != self.b or  self.b == self.c and self.b != self.a:
        
            #print('Isosceles')
            pass
            
        #Escaleno
        
        elif self.a  != self.b and  self.a != self.c and self.b  != self.c:
            
            #print('Escaleno')
            pass
            
        #### Classificação por ângulos ;(
            
i = Triangulo (1,-1,1)
j = Triangulo (1,1,2)
n = Triangulo (50, 10, 30)

print(i.identify_triangule(),"\n", j.identify_triangule(),"\n", n.identify_triangule())