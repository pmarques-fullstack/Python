x = 5
y = "Maria"
print(x)      # retorna 5
print(y)      # retorna Maria

x = 4         # x é do tipo int
x = "José"   # x é agora do tipo str
print(x)      # retorna José

x = str(3)       # x será '3'
y = int(3)       # y será 3
z = float(3)     # z será 3.0

x = 5
y = "Maria"
print(type(x))   # retorna <class 'int'> 
print(type(y))   # retorna <class 'str'>

x, y, z = "Maria", "José", "Marta"
print(x)      # retorna Maria
print(y)      # retorna José
print(z)      # retorna Marta

x = y = z = "Maria"
print(x)      # retorna Maria
print(y)      # retorna Maria
print(z)      # retorna Maria
