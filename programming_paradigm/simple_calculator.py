#a simple calculator script
class SimpleCalculator:

    def add(self,a,b):
        #return of addition of a and b 
        return a + b
    
    def subtract(self,a,b):
        # return subtraction
        return a - b 
    
    def multiply(self,a,b):
        #multiply
        return a * b
    
    def divide(self,a,b):
        #division function, return none if B is 0 
        if b == 0:
            return None
        else:
            return a/b
        