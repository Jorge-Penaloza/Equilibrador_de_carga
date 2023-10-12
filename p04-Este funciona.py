import random


# Generar lista de 15 valores aleatorios
lista = [random.randint(0, 40) for i in range(15)]
print("Lista original:", lista, "media",sum(lista)/3)
lista_original = lista
# Ordenar la lista de menor a mayor
lista.sort()

# Crear 3 grupos vacíos
grupo1 = []
grupo2 = []
grupo3 = []

idGrupo1 = []
idGrupo2 = []
idGrupo3 = []

# Asignar los valores a los grupos de forma equilibrada
contador = 0
while lista:
    id = len(lista)
    valor = lista.pop()
    print("id ",id,"valor ",valor )

    if sum(grupo1) <= sum(grupo2) and sum(grupo1) <= sum(grupo3):
        grupo1.append(valor)
    elif sum(grupo2) <= sum(grupo1) and sum(grupo2) <= sum(grupo3):
        grupo2.append(valor)
    else:
        grupo3.append(valor)
    
# Imprimir los grupos resultantes
print("Grupos:")
for i, grupo in enumerate([grupo1, grupo2, grupo3]):
    print(f"Grupo {i+1}:")
    for j, valor in enumerate(grupo):
        print(f"  {j}: {valor}")
    print(f"  Suma: {sum(grupo)}")
