#Crea un array o arreglo unidimensional donde le indiques
#el tamaño por teclado y crear una función que rellene
#el array o arreglo con los múltiplos de un número pedido
#por teclado.
#Por ejemplo, si defino un array de tamaño 5 y elijo un
#3 en la función, el array contendrá 3, 6, 9, 12, 15.
#Muéstralos por pantalla usando otra función distinta.
lista_t=[]
def llenar(n):
    numero_tamaño = int(input("De que tamaño desea la lista? :"))
    for i in range(numero_tamaño):
        lista_t.append((i+1)*n)
    presentar(n)
def presentar(n):
    print("Multiplos de un numero:",n)
    print(lista_t)
llenar(int(input("Escoja un numero del cual deee ver la lista de multiplos:")))