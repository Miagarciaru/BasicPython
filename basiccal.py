
num1 = input ("Enter a number: ") #por defecto pone el numero como strings
num2 = input ("Enter another number: ")
result = num1+num2

print (result) #no es la respuesta, pone 1213

result = int(num1) + int(num2) #solo sirve si son enteros las entradas
print (result) #retorna el valor verdadero

result = float(num1) + float(num2) 
print (result)
