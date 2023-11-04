#crear una funciom que reciba una lista de numeros y devuelva otra lista con los numeros pares

def pares(lista):
    lista_pares = []
    for i in lista:
        if i % 2 == 0:
            lista_pares.append(i)
    return lista_pares

def main():
    lista = [1,2,3,4,5,6,7,8,9,10]
    lista_pares = pares(lista)
    print(lista_pares)

if __name__ == "__main__":
    main()

# Path: borrador.py

