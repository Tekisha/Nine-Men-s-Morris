from random import random 
import logika
import bot
import hashmap
import time
def pvc():

    tabla =["O"]*24 #tablu predstavlja 24 clana liste (O-prazno polje,1-igrac 1,2-igrac 2)
    logika.print_tabla(tabla)

    broj_poteza=0

    igrac=logika.prvi_na_potezu() #odabir ko ima prvi potez,igrac ili racunar

    if igrac: #u zavisnosti ko prvi pocinje dodjeljuje se oznaka 1 ili 2
        oznaka_igraca="1"
        oznaka_racunara="2"
    else:
        oznaka_igraca="2"
        oznaka_racunara="1"

    print("FAZA 1")
    print("\n")
    while broj_poteza<18:  #prva faza
        if igrac:
            print("==========================================================================")
            print("Na potezu je IGRAC "+oznaka_igraca+" !")
            print("\n")
            if logika.odigraj(1,tabla,oznaka_igraca,broj_poteza):
                tabla_pobeda_igrac=[oznaka_igraca]*24
                logika.print_tabla(tabla_pobeda_igrac)
                print("==========================================================================")
                print("POBIJEDIO JE IGRAC "+oznaka_igraca+" !")
                print("==========================================================================")
                break
            igrac=False
            broj_poteza+=1
            logika.print_tabla(tabla)
        else:
            print("==========================================================================")
            print("Na potezu je IGRAC "+oznaka_racunara+"(racunar) !")
            print("\n")
            start=time.time()
            tabla=bot.odigraj(broj_poteza,tabla,oznaka_racunara,oznaka_igraca) #funkcija vraca novo stanje table
            
            if logika.kraj_igre(tabla,1,oznaka_racunara):
                tabla_pobeda_racunar=[oznaka_racunara]*24
                logika.print_tabla(tabla_pobeda_racunar)
                print("==========================================================================")
                print("POBIJEDIO JE IGRAC "+oznaka_racunara+"(racunar) !")
                print("==========================================================================")
                break
            igrac=True
            broj_poteza+=1
            logika.print_tabla(tabla)
            end=time.time()
            print("evalutaion time:"+ str(end-start))    
            #print(broj_poteza)
    

    print("\n")
    print("FAZA 2")
    print("\n")
    while True:
        if broj_poteza<=150:
            if igrac:
                print("==========================================================================")
                print("Na potezu je IGRAC "+oznaka_igraca+" !")
                print("\n")
                if logika.odigraj(2,tabla,oznaka_igraca,broj_poteza):
                    tabla_pobeda_igrac=[oznaka_igraca]*24
                    logika.print_tabla(tabla_pobeda_igrac)
                    print("==========================================================================")
                    print("POBIJEDIO JE IGRAC "+oznaka_igraca+" !")
                    print("==========================================================================")
                    break
                igrac=False
                broj_poteza+=1
                logika.print_tabla(tabla)
            else:
                print("==========================================================================")
                print("Na potezu je IGRAC "+oznaka_racunara+"(racunar) !")
                print("\n")
                start=time.time()
                tabla=bot.odigraj(broj_poteza,tabla,oznaka_racunara,oznaka_igraca) #funkcija vraca novo stanje table

                if logika.kraj_igre(tabla,2,oznaka_racunara):
                    tabla_pobeda_racunar=[oznaka_racunara]*24
                    logika.print_tabla(tabla_pobeda_racunar)
                    print("==========================================================================")
                    print("POBIJEDIO JE IGRAC "+oznaka_racunara+"(racunar) !")
                    print("==========================================================================")
                    break
                igrac=True
                broj_poteza+=1
                logika.print_tabla(tabla)
                end=time.time()
                print("evalutaion time:"+ str(end-start)) 
                #print(broj_poteza)
        else:
            print("Neresen rezultat.")
            break
    

            

if __name__=="__main__":
    pvc()