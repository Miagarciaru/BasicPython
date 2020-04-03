friends = ["Kevin" , "Karen", "Jim"]
print (friends) #imprime todos los datos en el arreglo
print (friends[0]) #imprime el primer elemento Kevin
print (friends[1:]) #exceptua el de la posición 0 Kevin
print (friends[1:3]) 

lucky_numbers = [42, 8, 15, 16, 23, 4]
print (lucky_numbers)

friends.extend(lucky_numbers) #añade los elementos de lucky_numbers a friends
print (friends)

friends.append("Creed") #añade Creed al final a friends
print (friends)

friends.insert(1, "Kelly") #añade Kelly a la posicion 1 a friends
print (friends)

friends.remove("Jim") #elimina a Jim de friends
print (friends)

friends.clear() #elimina toda la lista
print (friends)

friends = ["Kevin" , "Karen", "Jim"]
friends.pop() #elimina el ultimo en la lista
print (friends)

print (friends.index("Karen")) #da la posicion de Karen 

friends = ["Kevin" , "Karen", "Jim", "Jim"]
print (friends.count("Jim")) #cuenta cuantos Jim hay

lucky_numbers.sort() #los pone en orden
print (lucky_numbers)

lucky_numbers.reverse() #los pone en al revés
print (lucky_numbers)

friends2 = friends.copy() #copia todos los elementos de friends a friends2
print (friends2)
