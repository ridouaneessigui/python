pizzas=("4 fromage", "végétarienne", "hawai", "calzone")
def AfficheP():
    print("List Des Pizzas",len(pizzas))
    print("-------------------")
    n = 1
    for i in pizzas:
        print("pizza",n,":",i)
        n=n+1
    print("\n")
    print("Sorting Tuple")
    for i in sorted(pizzas):
        print("pizza:", i)


    print("\n")
    print("La premiere pizza: ",pizzas[0])
    print("La derniere pizza: ",pizzas[3])
    print("Pizza à ajouter: ")
    res=input()
    if res=="oui":
        Aoui()
    else:
        AfficheP()


def Aoui():
    print("ajouter le: ")
    a = input("")
    listPizzas=list(pizzas)
    if a not in listPizzas:
         listPizzas.append(a)
    else:
        print("ERREUR:la pizza existe déjà")
    print(sorted(listPizzas))
    newList=list(reversed(listPizzas))
    print(newList)
    print(listPizzas[-3:])





AfficheP()