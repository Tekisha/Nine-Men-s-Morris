
class RedError(Exception):
    pass

class Red(object):

    def __init__(self, kapacitet=20):
        self._velicina=0
        self._prvi=0
        self._kapacitet=kapacitet
        self._podaci=[None]*self._kapacitet
    
    def __len__(self):
        return self._velicina
    
    def is_empty(self):
        return self._velicina==0
    
    def prvi(self):
        if self.is_empty():
            raise RedError("Red je prazan. ")
        return self._podaci[self._prvi]
    
    def izbaci(self):
        if self.is_empty():
            raise RedError("Red je prazan.")
        
        element= self._podaci[self._prvi]
        self._podaci[self._prvi]=None

        self._prvi=(self._prvi +1)%self._kapacitet
        self._velicina-=1

        if 0<self._velicina<self._kapacitet//4:
            self._resize(self._kapacitet//2)
        
        return element

    def dodaj(self,e):
        if self.size==self._kapacitet:
            self._resize(2*self._kapacitet)
        
        index=(self.prvi+self._velicina)%self._kapacitet
        self._podaci[index]=e
        self._velicina+=1
    
    def _resize(self,kapacitet):
        trenutni_podaci=self._podaci
        trenutni_prvi=self.prvi

        self._podaci=[None]*kapacitet

        for e in range(self._velicina):
            self._podaci[e]=trenutni_podaci[trenutni_prvi]
            trenutni_prvi=(trenutni_prvi+1)%len(trenutni_podaci)

        self._prvi=0
        self._kapacitet=kapacitet
        
       