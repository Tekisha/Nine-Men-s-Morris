import random

def print_tabla(tabla):  #prikaz table
    print("\n")
    print("                PRIKAZ OZNAKA POLJA TABLE                                                 TRENUTNO STANJE TABLE")
    print("\n")
    print("(0)------------------------(1)-------------------------(2)                "+tabla[0] + "---------------------------" + tabla[1] + "---------------------------" + tabla[2])
    print("|                           |                           |                 |                           |                           |")
    print("|                           |                           |                 |                           |                           |")
    print("|                           |                           |                 |                           |                           |")
    print("|       (8)----------------(9)-----------------(10)     |                 |       " + tabla[8] + "-------------------" + tabla[9] + "--------------------" + tabla[10] + "      |")
    print("|       |                   |                    |      |                 |       |                   |                    |      |")
    print("|       |                   |                    |      |                 |       |                   |                    |      |")
    print("|       |                   |                    |      |                 |       |                   |                    |      |")
    print("|       |        (16)-----(17)-------(18)        |      |                 |       |         " + tabla[16] + "---------" + tabla[17] + "---------" + tabla[18] + "          |      |")
    print("|       |         |                   |          |      |                 |       |         |                   |          |      |")
    print("|       |         |                   |          |      |                 |       |         |                   |          |      |")
    print("|       |         |                   |          |      |                 |       |         |                   |          |      |")
    print("(3)----(11)-----(19)                 (20)-------(12)---(4)                "+tabla[3] + "-------" + tabla[11] + "---------" + tabla[19] + "                   " + tabla[20] + "----------" + tabla[12] + "------" + tabla[4])
    print("|       |         |                   |          |      |                 |       |         |                   |          |      |")
    print("|       |         |                   |          |      |                 |       |         |                   |          |      |")
    print("|       |         |                   |          |      |                 |       |         |                   |          |      |")
    print("|       |        (21)-----(22)-------(23)        |      |                 |       |         " + tabla[21] + "---------" + tabla[22] + "---------" + tabla[23] + "          |      |")
    print("|       |                   |                    |      |                 |       |                   |                    |      |")
    print("|       |                   |                    |      |                 |       |                   |                    |      |")
    print("|       |                   |                    |      |                 |       |                   |                    |      |")
    print("|       (13)--------------(14)-----------------(15)     |                 |       " +tabla[13] + "-------------------" +tabla[14] + "--------------------" +tabla[15] + "      |")
    print("|                           |                           |                 |                           |                           |")
    print("|                           |                           |                 |                           |                           |")
    print("|                           |                           |                 |                           |                           |")
    print("(5)------------------------(6)-------------------------(7)                "+tabla[5] + "---------------------------" +tabla[6] + "---------------------------" +tabla[7])
    print("\n")
 

def unos_polja(): #unos polja na koje se zeli staviti mica i provjera unosa
    while True:
        polje=input("Unesi polje table: ")
        if polje in ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23"]:
            return int(polje)
        print("Niste unijeli polje. Pokusajte ponovo!")

def je_prazno_polje(polje,tabla): #provjera da li je polje prazno
    if tabla[polje]=="O":
        return True
    return False

def  stavi_micu(polje,tabla,igrac): #kada igrac stavlja micu
    tabla[polje]=igrac
    #return tabla

def trojka(tabla,p1,p2,igrac): #provjera da li se na susjednim poljima koji mogu da cine trojku nalazi isti igrac,ako da onda je trojka spojena (p1 i p2 polja)
    if tabla[p1]==igrac and tabla[p2]==igrac:
        return True
    return False




def vezana_trojka(tabla,polje,igrac):   #provjera da li je neka trojka vezana
    if polje==0:
        return (trojka(tabla,1,2,igrac) or trojka(tabla,3,5,igrac))
    elif polje==1:
        return (trojka(tabla,0,2,igrac) or trojka(tabla,9,17,igrac))
    elif polje==2:
        return (trojka(tabla,0,1,igrac) or trojka(tabla,4,7,igrac))
    elif polje==3:
        return (trojka(tabla,0,5,igrac) or trojka(tabla,11,19,igrac))  
    elif polje==4:
        return (trojka(tabla,2,7,igrac) or trojka(tabla,12,20,igrac))
    elif polje==5:
        return (trojka(tabla,0,3,igrac) or trojka(tabla,6,7,igrac))
    elif polje==6:
        return (trojka(tabla,5,7,igrac) or trojka(tabla,14,22,igrac))
    elif polje==7:
        return (trojka(tabla,5,6,igrac) or trojka(tabla,2,4,igrac))
    elif polje==8:
        return (trojka(tabla,9,10,igrac) or trojka(tabla,11,13,igrac))
    elif polje==9:
        return (trojka(tabla,8,10,igrac) or trojka(tabla,1,17,igrac))
    elif polje==10:
        return (trojka(tabla,12,15,igrac) or trojka(tabla,9,8,igrac))
    elif polje==11:
        return (trojka(tabla,3,19,igrac) or trojka(tabla,8,13,igrac))
    elif polje==12:
        return (trojka(tabla,10,15,igrac) or trojka(tabla,20,4,igrac))
    elif polje==13:
        return (trojka(tabla,11,8,igrac) or trojka(tabla,14,15,igrac))
    elif polje==14:
        return (trojka(tabla,13,15,igrac) or trojka(tabla,6,22,igrac))
    elif polje==15:
        return (trojka(tabla,13,14,igrac) or trojka(tabla,12,10,igrac))
    elif polje==16:
        return (trojka(tabla,17,18,igrac) or trojka(tabla,19,21,igrac))
    elif polje==17:
        return (trojka(tabla,16,18,igrac) or trojka(tabla,9,1,igrac))
    elif polje==18:
        return (trojka(tabla,16,17,igrac) or trojka(tabla,20,23,igrac))
    elif polje==19:
        return (trojka(tabla,3,11,igrac) or trojka(tabla,16,21,igrac))
    elif polje==20:
        return (trojka(tabla,18,23,igrac) or trojka(tabla,12,4,igrac))
    elif polje==21:
        return (trojka(tabla,22,23,igrac) or trojka(tabla,19,16,igrac))
    elif polje==22:
        return (trojka(tabla,21,23,igrac) or trojka(tabla,14,6,igrac))
    elif polje==23:
        return (trojka(tabla,21,22,igrac) or trojka(tabla,20,18,igrac))

def broj_figura(tabla,igrac): #broji figure jednog igraca
    broj=0
    for i in range(24):
        if tabla[i]==igrac:
            broj+=1
    return broj

def odredi_protivnika(igrac): #vraca koju vrednost ima protivnik 1 ili 2
    if igrac=="1":
       return "2"
    else:
       return "1"

def ukloni_micu(tabla,igrac): #uklanja micu
    print("UKLANJANJE PROTIVNICKE MICE")

    protivnik=odredi_protivnika(igrac)
   
    
    while True:
        polje=unos_polja()

        if tabla[polje]!=str(igrac) and not je_prazno_polje(polje,tabla) and not vezana_trojka(tabla,polje,protivnik):
            tabla[polje]="O"
            break
        elif tabla[polje]!=str(igrac) and not je_prazno_polje(polje,tabla) and broj_figura(tabla,protivnik)==3:
            tabla[polje]="O"
            break
        else:
            print("Ne mozete ukloniti micu sa tog polja. Pokusajte ponovo!")

def susjedna_polja(polje): #vraca listu koju cine susjedna polja od polja koji je prosledjen 
    if polje==0:
        return [1,3]
    elif polje==1:
        return [0,2,9]
    elif polje==2:
        return [1,4]
    elif polje==3:
        return [0,5,11]
    elif polje==4:
        return [12,2,7]
    elif polje==5:
        return [3,6]
    elif polje==6:
        return [5,7,14]
    elif polje==7:
        return [6,4]
    elif polje==8:
        return [11,9]
    elif polje==9:
        return [8,10,17,1]
    elif polje==10:
        return [12,9]
    elif polje==11:
        return [3,19,8,13]
    elif polje==12:
        return [20,4,10,15]
    elif polje==13:
        return [11,14]
    elif polje==14:
        return [13,15,22,6]
    elif polje==15:
        return [14,12]
    elif polje==16:
        return [19,17]
    elif polje==17:
        return [16,18,9]
    elif polje==18:
        return [17,20]
    elif polje==19:
        return [11,21,16]
    elif polje==20:
        return [18,23,12]
    elif polje==21:
        return [19,22]
    elif polje==22:
        return [21,23,14]
    elif polje==23:
        return [22,20]

def moguci_potezi(tabla,polje): #vraca broj mogucih poteza figure iz tog polja
    broj_mogucih_poteza=0
    lista=susjedna_polja(polje)
    for susjedno_polje in lista:
        if tabla[susjedno_polje]=="O":
            broj_mogucih_poteza+=1
    return broj_mogucih_poteza

def moguci_potezi_igraca(tabla,igrac): #vraca ukupan broj mogucih poteza igraca
    broj_poteza=0
    for i in range(24):
        if tabla[i]==igrac:
            susjedi=susjedna_polja(i)
            for polje in susjedi:
                if tabla[polje]=="O":
                    broj_poteza+=moguci_potezi(tabla,i)
    
    return broj_poteza

def bool_moguci_potezi_igraca(tabla,igrac): #vraca true cim nadje moguci potez igraca, inace false (krace traje za provjeru kraja igre u odnosu na prethodnu funkciju)
    for i in range(24):
        if tabla[i]==igrac:
            susjedi=susjedna_polja(i)
            for polje in susjedi:
                if tabla[polje]=="O":
                    return True
    
    return False

def ponudjena_polja(tabla,polje):
    print("\n")
    print("Moguci potezi: ")
    lista=susjedna_polja(polje)
    for susjedno_polje in lista:
        if tabla[susjedno_polje]=="O":
            print(susjedno_polje)
    print("\n")

def ponudjena_polja_faza1(tabla):
    lista_poteza=[]
    print("\n")
    print("Moguci potezi:")
    for i in range(24):
        if tabla[i]=="O":
            lista_poteza.append(str(i))
    print(" ".join(lista_poteza))

def odigraj(faza,tabla,igrac,broj_poteza): #kada je igrac na potezu,vraca da li je doslo do pobjede
    

    if faza==1:
        while True:
            ponudjena_polja_faza1(tabla)
            polje=unos_polja()
            if je_prazno_polje(polje,tabla):
                stavi_micu(polje,tabla,igrac)
                if vezana_trojka(tabla,polje,igrac):
                    print_tabla(tabla)
                    ukloni_micu(tabla,igrac)
                break
            print("Polje nije prazno. Pokusajte ponovo!")
            
        

    elif faza==2:
        while True:
            print("Unesite polje figure koju zelite da pomerite.")
            polje=unos_polja()
            if tabla[polje]==igrac and moguci_potezi(tabla,polje)!=0:
                break
            elif tabla[polje]!=igrac:
                print("Na tom polju se ne nalazi vasa figura. Pokusajte ponovo!")
            else:
                print("Nemoguce je pomjeriti izabranu figuru. Pokusajte ponovo!")
        
        ponudjena_polja(tabla,polje)

        while True:
            print("Unesite susjedno polje polja figure gde zelite da je pomerite: ")
            potez=unos_polja()
            if potez in susjedna_polja(polje) and je_prazno_polje(potez,tabla):
                tabla[polje]="O"
                tabla[potez]=igrac
                break
            elif potez not in susjedna_polja(polje):
                print("Izabrano polje nije susedno polje date figure. Pokusajte ponovo!")
            else:
                print("Polje nije prazno. Pokusajte ponovo!")
        
        if vezana_trojka(tabla,potez,igrac):
            print_tabla(tabla)
            ukloni_micu(tabla,igrac)



    if kraj_igre(tabla,faza,igrac):
        return True
    else:
        return False

def kraj_igre(tabla,faza,igrac):
    if (broj_figura(tabla,"1")<3 and faza!=1 and igrac=="2") or (bool_moguci_potezi_igraca(tabla,"1")==0 and igrac=="2" and faza!=1):
        return True
    elif (broj_figura(tabla,"2")<3 and faza!=1 and igrac=="1") or (bool_moguci_potezi_igraca(tabla,"2")==0 and igrac=="1" and faza!=1):
        return True
    else:
        return False


#=================================#
#nudi mogucnost biranja ko ce imati prvi potez ili random odabir (ko igra prvi ima malu,skoro zanemarljivu,
# prednost u obicnoj mici, u nekim drugim izvedbama mice ta razlika je izrazenija)
def prvi_na_potezu(): 
    print("MENU")
    print("1. Vi ste prvi na potezu")
    print("2. Racunar je prvi na potezu")
    print("3. Nasumican odabir")

    while True:
        opcija=input("Unesite redni broj ponudjene opcije: ")
        if opcija in ["1","2","3","1.","2.","3."]:
            break
        print("Niste uneli redni broj ponudjene opcije. Pokusajte ponovo!")
    
    if opcija in ["1","1."]:
        return True
    elif opcija in ["2","2,"]:
        return False
    else:
        return bool(random.getrandbits(1))

if __name__=="__main__":
    print_tabla()