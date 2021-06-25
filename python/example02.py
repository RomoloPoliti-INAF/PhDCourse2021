#!/usr/bin/env python3
class Ops2:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __dict__(self):
        print(f"il valore di x è {self.x}")
        
    def sum(self):
        return self.x+self.y
    
    def prod(self):
        return self.x*self.y
