import sympy as sy

funzione = input("Posso realizzare una delle seguenti task richieste dal problema. Quale desideri? \n 1. Lista di numeri primi fino ad N \n 2. Genera sequenza di fibonacci \n 3. Parser di log files che estragga timestamp ed errore\n")

def prime_generator(N):
    lista_numeri = [x for x in range(N+1) if sy.isprime(x)]
    print(lista_numeri)
    return 

match funzione:
    case "1":
        N = input("Vuoi i numeri primi fino a...? ")
        N = int(N)
        prime_generator(N)
        
    case _:
        print("input non valido")
