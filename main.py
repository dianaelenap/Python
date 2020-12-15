from produs import Product
import sqlite3

conn = sqlite3.connect('Python/produse.db')

c = conn.cursor()

querry1 = "SELECT * FROM stoc"
querry2 = "SELECT * FROM vanzari"

stoc = c.execute(querry1)

lista_stoc = []

#pentru fiecare row in stoc creez instanta de tip Product si salvez in lista_stoc
for row in stoc:
    p = Product(row[1],row[2])
    lista_stoc.append(p)

vanzari = c.execute(querry2)

lista_vanzari = []
cantitate_zi = []

#pentru fiecare row in stoc creez instanta de tip Product si salvez in lista_vanzari
for row in vanzari:
    p = Product(row[1],row[2])
    lista_vanzari.append(p)
    cantitate_zi.append(row[2]/row[3])#calculez necesarul de produse pentru o zi (cantitate/nr_zile)

conn.commit()

conn.close()

if __name__ == "__main__":
    time_period = int(input("Perioada de timp(zile): "))

    cantitate_necesara = []

    #calculez cantitatea necesara pentru fiecare produs in parte pentru perioada ceruta
    for i in range(0,len(cantitate_zi)):
        cantitate_necesara.append(cantitate_zi[i]*time_period)

    lista_cumparaturi = []

    for i in range(0,len(lista_stoc)):
        diferenta = lista_stoc[i].quantity - cantitate_necesara[i]
        diferenta = round(diferenta)
        if(diferenta >= 0):#exista suficient stoc
            continue
        else:
            diferenta = diferenta * (-1)
            p = Product(lista_stoc[i].name,diferenta)
            lista_cumparaturi.append(p)

    for x in lista_cumparaturi:
        print("Pentru %s trebuie cumparat %d " % (x.name,x.quantity))