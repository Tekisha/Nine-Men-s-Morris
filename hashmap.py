from asyncio.events import BaseDefaultEventLoopPolicy
import random

from zmq import has

from map import Map, MapElement

class HashMap(object):

    def __init__(self,capacity=10000):
        self._data=capacity*[None]
        self._capacity=capacity
        self._size=0
        # self._keys=[]
        # self.prime= 193
        self.prime=109345121

        self._a=1+random.randrange(self.prime-1)
        self._b=random.randrange(self.prime)

    def __len__(self):
        return self._size
    
    def _hash(self,x): #x kljuc koji hash funkcija hashira i vraca vrednost za indeks
        hashed_value = (hash(x)*self._a+self._b)%self.prime #(ax+b)mod p
        compressed=hashed_value % self._capacity #hash vrednost mod kapacitet da bi se smanjila mogucnost kolizija
        return compressed

    def _resize(self,capacity):
        old_data=list(self.items())
        self._data=capacity*[None]
        self._size=0

        for (k,v) in old_data:
            self[k]=v
    
    def __getitem__(self,key): #prisupa elementu sa datim kljucem
        bucket_index = self._hash(key)
        return self._bucket_getitem(bucket_index, key)
    
    def __setitem__(self,key,value):
        bucket_index=self._hash(key)
        self._bucket_setitem(bucket_index,key,value)

       # if bucket_index not in self._keys:
            #self._keys.append(bucket_index)

        current_capacity = len(self._data)
        if self._size > current_capacity//2:
            self._resize(2*current_capacity-1)
        
    def __delitem__(self,key):
        bucket_index=self._hash(key)
        self._bucket_delitem(bucket_index,key)
        self._size-=1
    

    _MARKER = object()

    def _is_available(self,bucket_index):
        return self._data[bucket_index] is None or self._data[bucket_index] is self._MARKER

    def _find_bucket(self,bucket_index,key):
        available_slot=None

        while True:
            if self._is_available(bucket_index) : #ako je prazno mesto
                if available_slot is None:  
                    available_slot=bucket_index

                if self._data[bucket_index] is None:
                    return False, available_slot
                
            elif key == self._data[bucket_index].key:
                return True,bucket_index
            
            bucket_index = (bucket_index+1)%len(self._data)
                

    def _bucket_getitem(self,bucket_index,key):

        found,index= self._find_bucket(bucket_index,key)
        if not found:
            return False
        return self._data[index].value
    
    def _bucket_setitem(self, bucket_index, key, value):
        found, available_bucket_index = self._find_bucket(bucket_index, key)
        if not found:
            self._data[available_bucket_index]= MapElement(key,value)
            self._size += 1
        else:
            self._data[available_bucket_index].value = value
    
    def _bucket_delitem(self,bucket_index, key):
        found, index = self._find_bucket(bucket_index, key)
        if not found:
            raise KeyError("Ne postoji element sa trazenim kljucem.")
        
        self._data[index]= self._MARKER
    
    def __iter__(self):
        total_buckets=len(self._data)
        for i in range(total_buckets):
            if not self._is_available(i):
                yield self._data[i].key
    
    def items(self):
        total_buckets = len(self._data)
        for i in range(total_buckets):
            if not self._is_available(i):
                yield self._data[i].key, self._data[i].value
            
if __name__ == '__main__':
    hash_map = HashMap(24)
    hash_map[1]=10
    hash_map[2]=2

    for item in hash_map:
        print(hash_map[item])
    
    hash_map[1]=3
    del hash_map[2]

    for item in hash_map:
        if hash_map[item] is None:
            print("x")
        print(hash_map[item])

