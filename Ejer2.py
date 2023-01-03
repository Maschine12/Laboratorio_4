lista_nota = [20,15,12,11,8,4,1]
print(lista_nota)
menor = lista_nota[0]
for i in range(len(lista_nota)):
    if menor > lista_nota[i]:
        menor = lista_nota[i]
print(menor)
#eliminar dato minimo
for j in range(len(lista_nota)):
    if menor == lista_nota[j]:
        lista_nota.remove(menor)
print(lista_nota)
