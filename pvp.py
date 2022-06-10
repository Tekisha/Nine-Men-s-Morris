import logika
import hashmap

def pVp():
    tabla =["O"]*24#tablu predstavlja 24 clana liste (O-prazno polje,1-igrac 1,2-igrac 2)
   

    logika.print_tabla(tabla)

    broj_poteza=0

    igrac1=True

    print("FAZA 1")
    print("\n")
    while broj_poteza<18:  #prva faza
        if igrac1:
            print("Na potezu je IGRAC 1!")
            print("\n")
            if logika.odigraj(1,tabla,"1",broj_poteza):
                logika.print_tabla(tabla)
                print("Pobijedio je igrac 1!")
                break
            igrac1=False
            broj_poteza+=1
            logika.print_tabla(tabla)
        else:
            print("Na potezu je IGRAC 2!")
            print("\n")
            if logika.odigraj(1,tabla,"2",broj_poteza):
                logika.print_tabla(tabla)
                print("Pobijedio je igrac 2!")
                break
            igrac1=True
            broj_poteza+=1
            logika.print_tabla(tabla)
    

    print("\n")
    print("FAZA 2")
    print("\n")
    while True:
        if igrac1:
            print("Na potezu je IGRAC 1!")
            print("\n")
            if logika.odigraj(2,tabla,"1",broj_poteza):
                logika.print_tabla(tabla)
                print("Pobijedio je igrac 1!")
                break
            igrac1=False
            broj_poteza+=1
            logika.print_tabla(tabla)
        else:
            print("Na potezu je IGRAC 2!")
            print("\n")
            if logika.odigraj(2,tabla,"2",broj_poteza):
                logika.print_tabla(tabla)
                print("Pobijedio je igrac 2!")
                break
            igrac1=True
            broj_poteza+=1
            logika.print_tabla(tabla)

    

            

if __name__=="__main__":
    pVp()