from collections import deque  

print ("deque")
de = deque([1, 2, 3, 3, 4, 2, 4, 5, 6, 3])
print(de)
  
print ("Позиция числа 4 : ")
print (de.index(4))

de.insert(4,3)

print ("Вставка 3 на 5 позицию : ")
print (de)

print ("Количество 4 : ")
print (de.count(4))

de.remove(3)

print ("Удалить первую тройку : ")
print (de)
print("\n\n")

from collections import ChainMap  
       
print ("ChainMap")

dic1 = { 'x' : 1, 'y' : 2 }
dic2 = { 'y' : 3, 'z' : 4 }
  
chain = ChainMap(dic1, dic2)
  
print ("Вывод всего, что есть : ")
print (chain.maps)
  
print ("Ключи : ")
print (list(chain.keys()))
  
print ("Значения : ")
print (list(chain.values()))
print("\n\n")


print  ("UserList") 
from collections import UserList
  
class MyList(UserList):
    def pop(self, s = None):
        print("Deletion not allowed")

L = MyList([1, 2, 3, 4])
 
print("Изначально :")
print(L)
 
print("Попытка :")
L.pop(1)
print("После :")
print(L)
print("\n\n")


print (" UserDict ")
from collections import UserDict
  
class MyDict(UserDict):
    def pop(self, s = None):
        print("Deletion not allowed")
     
# Driver's code
d = MyDict({'a':1,
    'b': 2,
    'c': 3})
 
print("Изначально :")
print(d)
print("Попытка :")
d.pop(1)
print("После :")
print(d)
print("\n\n")


from frozendict import frozendict
print("Что изначально :")
frzndct = frozendict({'a':1, 'b': 2, 'c': 3})

print("Хеширование :")
h = frzndct.__hash__()
print(h)

print("Hовый frozendict с добавленным / обновлённым значением")
frzndct = frzndct.set('a', 5)
print(frzndct)
frzndct = frzndct.set('d', 4)
print(frzndct)

print("Вывод по ключу :")
print(frzndct.key(2)) # c

print("Ключ по индексу :")
print(frzndct.value(2)) # 3

print("Что на этом мест :")
print(frzndct.item(2)) # ('c', 3)