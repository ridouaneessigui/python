import sys
import os
dict={
      "Tapas":"Tomatoes, Olives, Ham",
      "Fajitas":"Tortilla, Chicken, Onion, Pepper",
      }


def Menu():
    print("Restaurant Projet Complete")
    print("--------------------------")
    print("1-Menu Complete")
    print("2-Commander un plat")
    print("3-Quitter le restaurant")
    monchoix=input()
    #os.system("cls")
    if monchoix=='1':
        menuchoix()
    elif monchoix=='2':
        order_food()
    elif monchoix== '3':
        sys.exit("Vous avez ratez l’occasion de manger ce délicieux plat")

def menuchoix():
    print("Nos Plats")
    print("1-Tapas")
    print("2-Fajitas")
    print("3-Menu")

    cc = choix(input())
    while cc != '3':
        cc = choix(input())

def choix(V1):
    if V1=='1':
        print("Tapas:", dict["Tapas"].split(","))
        food="Tapas"
    elif V1=='2':
        print("Fajitas: ",dict["Fajitas"].split(","))
        food = "Fajitas"
    elif V1 == '3':
        Menu()
    else:
        food="Null"
    return food



def order_food():
    food=input("Tapez Ta commande  ").split( )
    if food[0]=="eat":
        if food[1] in dict:
            print("Voici votre commande: " + food[1])
            print(food[1], dict[food[1]].split(","))
        else:
           print("Nous n’avons pas ce plat")
    else:
        Menu()

#Main
Menu()
