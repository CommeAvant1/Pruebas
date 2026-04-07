"""
pida el nombre del cliente , 
cuantas manzanos comprara y un precio. 
muestre el nombre y el total a pagar
"""
precio : float = 0.50

print("INGRESE SU NOMBRE")
nombre = input()

print("¿cuantas manzanas va a comprar?")
nmrDeManzanas = int(input())

costo = precio * nmrDeManzanas

print(f"se llama {nombre}, quiere comprar {nmrDeManzanas} manzanas y el el costo total es de {costo}")

"""
nom = input("Ingrese nombre:\n")
can = int(input("Ingrese cantidad manzanas: \n"))
pre = float(input("Ingrese precio:\n"))
tot = can pre
print(f"(nom) compro S/{tot}")
"""