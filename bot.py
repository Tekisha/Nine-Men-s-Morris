from cmath import inf
import logika
import stablo
from hashmap import HashMap
import time
import random



hashmap_faza1=HashMap() #skladisti vrednosti heuristika za fazu 1 (kljuc stanje table,vrednost heuristika)
hashmap_faza2=HashMap() #skladisti vrednosti heuristika za fazu 2 (kljuc stanje table,vrednost heuristika)


def kopiraj_tablu(tabla): #kopira prosledjenu tablu, vraca novi cvor stabla
    nova_tabla=["O"]*24
    for i in range(24):
        nova_tabla[i]=tabla[i]
    return nova_tabla

def ukloni_micu_mogucnosti(roditelj,cvor_tabla,oznaka_racunara): #generise sve mogucnosti izgleda table uklanjanjem mice, svaka nova tabla se smjesta u TreeNode cvor i dodaje kao dete prosledjenom roditelju
    protivnik=logika.odredi_protivnika(oznaka_racunara)

    for i in range(24):
        if cvor_tabla.data[i]==protivnik:
            if not logika.vezana_trojka(cvor_tabla.data,i,protivnik) or logika.broj_figura(cvor_tabla.data,protivnik)==3 :
                nova_tabla= stablo.TreeNode(kopiraj_tablu(cvor_tabla.data))
                nova_tabla.data[i]="O"
                nova_tabla.polje1=cvor_tabla.polje1
                nova_tabla.polje2=cvor_tabla.polje2
                nova_tabla.uklonjeno_polje=i
                nova_tabla.closed_morris=True
                nova_tabla.igrac=oznaka_racunara
                roditelj.add_child(nova_tabla)
            
def moguci_izgled_table_faza2(roditelj,oznaka_igraca): #generise sve mogucnosti izgleda table pomjeranjem mice u drugoj fazi
    for i in range(24):
        if(roditelj.data[i]==oznaka_igraca and logika.moguci_potezi(roditelj.data,i)>0):
            moguce_sledece_polje=logika.susjedna_polja(i)

            for moguce_polje in moguce_sledece_polje:
                if(roditelj.data[moguce_polje]=="O"):
                    nova_tabla= stablo.TreeNode(kopiraj_tablu(roditelj.data))
                    nova_tabla.data[moguce_polje]=oznaka_igraca
                    nova_tabla.data[i]="O"
                    nova_tabla.polje1=i
                    nova_tabla.polje2=moguce_polje


                    if (logika.vezana_trojka(nova_tabla.data,moguce_polje,oznaka_igraca)):
                        ukloni_micu_mogucnosti(roditelj,nova_tabla,oznaka_igraca)
                    else:
                        roditelj.add_child(nova_tabla)
def moguci_izgled_table_faza1(roditelj,oznaka_igraca): #generise sve mogucnosti izgleda table postavljanjem mice u prvoj fazi
    for i in range(24):
        if(roditelj.data[i]=="O"):
            nova_tabla=stablo.TreeNode(kopiraj_tablu(roditelj.data))  #nova_tabla predstavlja instancu objekta TreeNode
            nova_tabla.data[i]=oznaka_igraca
            nova_tabla.polje2=i

            

            if (logika.vezana_trojka(nova_tabla.data,i,oznaka_igraca)):
                ukloni_micu_mogucnosti(roditelj,nova_tabla,oznaka_igraca)
            else:
                roditelj.add_child(nova_tabla)
        

def kreiraj_stablo(koren,na_potezu,dubina,broj_poteza): #kreira stablo odredjene dubine, koren predstavlja trenutno stanje tabele, a deca mogucnosti sledeceg poteza

    
    sledeci_na_potezu=logika.odredi_protivnika(na_potezu)

    if dubina!=0 and not koren.game_over:
        if broj_poteza<18:
            moguci_izgled_table_faza1(koren,na_potezu)

            for dete in koren.children:
                kreiraj_stablo(dete,sledeci_na_potezu,dubina-1,broj_poteza+1)


        else:
            moguci_izgled_table_faza2(koren,na_potezu)
        
        
            for dete in koren.children:
                if logika.bool_moguci_potezi_igraca(dete.data,sledeci_na_potezu)!=0 and logika.broj_figura(dete.data,sledeci_na_potezu)>=3:
                    kreiraj_stablo(dete,sledeci_na_potezu,dubina-1,broj_poteza+1)
                else:
                    dete.game_over=True

    return




def odigraj(broj_poteza,tabla,oznaka_racunara,oznaka_igrac): #funkcija za odigravanje poteza od strane racunara, vraca novo stanje table
    
    stablo_tabli= stablo.Tree()
    koren=stablo.TreeNode(tabla)
    stablo_tabli.root=koren

    if broj_poteza<18:
        depth=3
    else:
        depth=4
    
    kreiraj_stablo(stablo_tabli.root,oznaka_racunara,depth,broj_poteza)#funkcija koja kreira stablo do odredjene dubine
    minimax(koren,depth,float(-inf),float(inf),broj_poteza,False,oznaka_igrac,oznaka_racunara,0)
    
    nova_tabla=["O"]*24
    polje1=None
    polje2=None
    uklonjeno_polje=None
    min=float(inf)
    random.shuffle(koren.children)
    for dete in koren.children:
        if dete.value is not None and dete.data is not None:
            if dete.game_over:
                nova_tabla=kopiraj_tablu(dete.data)
                polje1=dete.polje1
                polje2=dete.polje2
                uklonjeno_polje=dete.uklonjeno_polje
                min=dete.value
                break
            if dete.value<min:
                nova_tabla=kopiraj_tablu(dete.data)
                polje1=dete.polje1
                polje2=dete.polje2
                uklonjeno_polje=dete.uklonjeno_polje
                min=dete.value
    
    print("==============================================================================")

    if polje1 is not None:
        print("Racunar je pomerio figuru sa polja "+str(polje1)+" na polje "+str(polje2))
    else:
        print("Racunar je stavio figuru na polje: "+str(polje2))
    
    if uklonjeno_polje is not None:
        print("Racunar je uklonio figuru sa polja: "+str(uklonjeno_polje))

    return nova_tabla
    


def minimax(koren,dubina,alpha,beta,broj_poteza,je_igrac,oznaka_igrac,oznaka_racunar,broj_odnosenja): #obilazi stablo od listova ka korenu i vraca najbolji moguci potez

    

    if dubina==0 or koren.game_over:
        if broj_poteza<18:
            if hashmap_faza1[tuple(koren.data)]!=False:
                return hashmap_faza1[tuple(koren.data)]
        else:
            if hashmap_faza2[tuple(koren.data)]!=False:
                return hashmap_faza2[tuple(koren.data)]


        eval=evaluate(koren,broj_poteza,oznaka_igrac,oznaka_racunar,broj_odnosenja)
        if broj_poteza<18:
            hashmap_faza1[tuple(koren.data)]=eval
        else:
            hashmap_faza2[tuple(koren.data)]=eval
        return  eval

    
    if je_igrac:
        maxEval=float(-inf)

        for dete in koren.children:
            broj_odnosenja_dete=broj_odnosenja
            if dete.closed_morris== True and dete.igrac==oznaka_igrac:
                broj_odnosenja_dete+=1
            eval = minimax(dete,dubina-1,alpha,beta,broj_poteza+1,False,oznaka_igrac,oznaka_racunar,broj_odnosenja_dete)
            maxEval = max(maxEval,eval)

            dete.value=eval
            if eval>alpha:
                alpha=eval
                
            if beta<=alpha:
                break
        return maxEval
    else:
        minEval=float(inf)
        for dete in koren.children:
            broj_odnosenja_dete=broj_odnosenja
            if dete.closed_morris== True and dete.igrac==oznaka_racunar:
                broj_odnosenja_dete-=1
            eval = minimax(dete,dubina-1,alpha,beta,broj_poteza+1,True,oznaka_igrac,oznaka_racunar,broj_odnosenja_dete)
            minEval = min(minEval,eval)


            dete.value=eval
            if eval<beta:
                beta=eval
                
            if beta <= alpha:
                break
        return minEval

    




#heuristika==================================
# broj_odnosenja predstavlja razliku odnijetih figura od trenutnog do datog stanja
#ostale heuristike ispod
def evaluate(cvor,broj_poteza,igrac,racunar,broj_odnosenja): #racuna vrednost stanja na tabli
    if broj_poteza<18:
        vrednost=15*broj_odnosenja+20*zatvorena_trojka(cvor.closed_morris,cvor.igrac,igrac,racunar)+26*broj_vezanih_trojki(igrac,cvor.data,racunar)+1*broj_blokiranih_figura(igrac,cvor.data,racunar)+6*broj_figura(cvor.data,igrac,racunar)+12*(dvojka(cvor.data,igrac)-dvojka(cvor.data,racunar))+7*dupla_dvojka(cvor.data,igrac)
    else:
        otvoren_morris_igrac=otvoren_morris(cvor.data,igrac)
        otvoren_morris_racunar=otvoren_morris(cvor.data,racunar)
        dupli_morris_igrac=dupli_morris(cvor.data,igrac)
        dupli_morris_racunar=dupli_morris(cvor.data,racunar)
        vrednost=0*broj_odnosenja+16*zatvorena_trojka(cvor.closed_morris,cvor.igrac,igrac,racunar)+43*broj_vezanih_trojki(igrac,cvor.data,racunar)+10*broj_blokiranih_figura(igrac,cvor.data,racunar)+8*broj_figura(cvor.data,igrac,racunar)+42*(otvoren_morris_igrac-otvoren_morris_racunar)+20*(dupli_morris_igrac-dupli_morris_racunar)+1086*pobeda(cvor.data,igrac,racunar)

    return vrednost



def otvoren_morris(tabla,igrac): #provjerava da li je morris otvoren,tj da li se pomjeranjem jedne figure moze zatvoriti morris
    broj=0
    for i in range(24):
        if tabla[i]==igrac:
            susjedi=logika.susjedna_polja(i)
            for polje in susjedi:
                if tabla[polje]=="O":
                    tabla[i]="O"
                    tabla[polje]=igrac
                    if logika.vezana_trojka(tabla,polje,igrac):
                        broj+=1
                    tabla[i]=igrac
                    tabla[polje]="O"
    
    return broj

def dupli_morris(tabla,igrac): #provjerava da li neko polje cini i horizontalni i vertikalni morris
    broj=0
    for i in range(24):
        if tabla[i]==igrac:
            if logika.vezana_trojka(tabla,i,igrac):
                susjedi=logika.susjedna_polja(i)
                for polje in susjedi:
                    if tabla[polje]=="O":
                        tabla[i]="O"
                        tabla[polje]=igrac
                    if logika.vezana_trojka(tabla,polje,igrac):
                        broj+=1
                    tabla[i]=igrac
                    tabla[polje]="O"
    
    return broj

def dvojka(tabla,igrac): #racuna dvojke kojima fali jos jedna figura da bude vezana trojka
    broj=0

    for i in range(24):
        if tabla[i]==igrac:
            lista = trojke_polja(i)
            for trojka in lista:
                broj_igraca=0
                broj_praznih_polja=0
                for polje in trojka:
                    if tabla[polje]==igrac:
                        broj_igraca+=1
                    elif tabla[polje]=="O":
                        broj_praznih_polja+=1
                if broj_praznih_polja==1 and broj_igraca==2:
                    broj+=1
    return broj

def dupla_dvojka(tabla,igrac): #racuna duple dvojke kojima fali po jedna figura u horizontalnoj i u vertikalnoj trojci da bude dupli morris
    broj=0

    protivnik=logika.odredi_protivnika(igrac)

    for i in range(24):
        if tabla[i]==igrac: #ako je na polju igrac
            lista=trojke_polja(i) #vraca listu trojki koje cine vertikalnu i horizontalnu trojku sa tim poljem
            broj_trojki=0
            for trojka in lista:
                broj_igraca=0
                broj_praznih_polja=0
                for polje in trojka:
                    if tabla[polje]==igrac:
                        broj_igraca+=1
                    elif tabla[polje]=="O":
                        broj_praznih_polja+=1
                
                if broj_praznih_polja==1 and broj_igraca==2: #ako trojka ima dvije figura igraca i jedno slobodno polje znaci da je to dvojka
                    broj_trojki+=1

            if broj_trojki==2: #ako obe trojke imaju po dvije figure igraca i po jedno slobodno polje to je dupla dvojka
                broj+=1   

        elif tabla[i]==protivnik: #ako je na polju protivnik,isti princip kao za igraca (provjerava se odmah, da se ne bi moralo dva puta prolaziti kroz tablu posebno)
            lista=trojke_polja(i)
            broj_trojki=0
            for trojka in lista:
                broj_igraca=0
                broj_praznih_polja=0
                for polje in trojka:
                    if tabla[polje]==protivnik:
                        broj_igraca+=1
                    elif tabla[polje]=="O":
                        broj_praznih_polja+=1
                
                if broj_praznih_polja==1 and broj_igraca==2:
                    broj_trojki+=1

            if broj_trojki==2:
                broj-=1     

    return broj                
                 

def zatvorena_trojka(zatvoreno,potez,igrac,racunar): #ako je morris zatvoren u tom potezu, onda vraca odredjenu vrednost u zavisnosti ko je zatvorio morris
    if zatvoreno:
        if potez==racunar:
            return -1
        elif potez==igrac:
            return 1
    
    return 0
        

def broj_figura(tabla,igrac,racunar): #razlika figura
    broj_figura=0
    for i in range(24):
        if tabla[i]==igrac:
            broj_figura+=1
        elif tabla[i]==racunar:
            broj_figura-=1
    return broj_figura


def broj_blokiranih_figura(igrac,tabla,racunar): #razlika blokiranih figura
    broj=0
    

    for i in range(24):
        blokiran=True
        if tabla[i]==igrac:
            for polje in logika.susjedna_polja(i):
                if tabla[polje]=="O":
                    blokiran=False
            if blokiran:
                broj-=1
        elif tabla[i]==racunar:
            for polje in logika.susjedna_polja(i):
                if tabla[polje]=="O":
                    blokiran=False
            if blokiran:
                broj+=1

    
    return broj

def broj_vezanih_trojki(igrac,tabla,racunar): #broj morrisa
    broj=0
                         
    triple=triples()

    for trojka in triple:
        trojka_igrac=True
        trojka_racunar=True
        for polje in trojka:
            if tabla[polje]!=igrac:
                trojka_igrac=False
            if tabla[polje]!=racunar:
                trojka_racunar=False
        
        if trojka_igrac:
            broj+=1
        elif trojka_racunar:
            broj-=1



    return broj


# def dupla_trojka(tabla,igrac,racunar): #za svako polje provjerava da li se nalazi u duploj trojci
#     broj=0
    
    
#     for i in range(24): #provjeravamo svako polje
#         trojke=0
#         spojene_trojke=[]
#         if tabla[i]==igrac:  # ako je igrac na tom polju, provjeravamo da li formira trojku. Ako da, provjeravamo da li formira dvije trojke
#             if logika.vezana_trojka(tabla,i,igrac):
#                 lista=logika.susjedna_polja(i) #provjeravamo sva susjedna polja da li cine trojku sa poljem i
#                 for susjed in lista: 
#                     trojka=True
#                     polja_za_provjeru=polja_trojke(i,susjed)


#                     if polja_za_provjeru in spojene_trojke: #ako je moguca trojka vec provjerena formirana trojka, preskace se
#                         continue


#                     for polje in polja_za_provjeru:
#                         if tabla[polje]!=igrac:
#                             trojka=False 
#                             break
#                     if trojka:
#                         spojene_trojke.append(polja_za_provjeru)
#                         trojke+=1

#                 if trojke==2:
#                     broj+=1

#         if tabla[i]==racunar: #isti princip i za racunar
#             if logika.vezana_trojka(tabla,i,racunar):
#                 lista=logika.susjedna_polja(i)
#                 for susjed in lista:
#                     trojka=True
                    
#                     polja_za_provjeru=polja_trojke(i,susjed)


#                     if polja_za_provjeru in spojene_trojke:
#                         continue


#                     for polje in polja_za_provjeru:
#                         if tabla[polje]!=racunar:
#                             trojka=False 
#                             break
#                     if trojka:
#                         spojene_trojke.append(polja_za_provjeru)
#                         trojke+=1

#                 if trojke==2:
#                     broj-=1
        
#     return broj

def pobeda(tabla,igrac,racunar): #proverava da li je stanje na tabli pobjedonosno
    if logika.broj_figura(tabla,racunar)<3 or logika.bool_moguci_potezi_igraca(tabla,racunar)==0 : #pobeda igraca
        return 1
    elif logika.broj_figura(tabla,igrac)<3 or logika.bool_moguci_potezi_igraca(tabla,igrac)==0: #pobeda racunara
        return -1
    else:
        return 0             
    


def polja_trojke(polje,susjedno_polje): #vraca lista polja koja cine trojku
    if polje in [0,1,2] and susjedno_polje in [0,1,2]:
        return [0,1,2]
    elif polje in [0,3,5] and susjedno_polje in [0,3,5]:
        return [0,3,5]
    elif polje in [1,9,17] and susjedno_polje in [1,9,17]:
        return [1,9,17]
    elif polje in [2,4,7] and susjedno_polje in [2,4,7]:
        return [2,4,7]
    elif polje in [8,9,10] and susjedno_polje in [8,9,10]:
        return [8,9,10]
    elif polje in [8,11,13] and susjedno_polje in [8,11,13]:
        return [8,11,13]
    elif polje in [10,12,15] and susjedno_polje in [10,12,15]:
        return [10,12,15]
    elif polje in [16,17,18] and susjedno_polje in [16,17,18]:
        return [16,17,18]
    elif polje in [16,19,21] and susjedno_polje in [16,19,21]:
        return [16,19,21]
    elif polje in [18,20,23] and susjedno_polje in [18,20,23]:
        return [18,20,23]
    elif polje in [21,22,23] and susjedno_polje in [21,22,23]:
        return [21,22,23]
    elif polje in [22,14,6] and susjedno_polje in [22,14,6]:
        return [22,14,6]
    elif polje in [13,14,15] and susjedno_polje in [13,14,15]:
        return [13,14,15]
    elif polje in [5,6,7] and susjedno_polje in [5,6,7]:
        return [5,6,7]
    elif polje in [3,11,19] and susjedno_polje in [3,11,19]:
        return [3,11,19]
    elif polje in [20,12,4] and susjedno_polje in [20,12,4]:
        return [20,12,4]

def triples(): #vraca listu listi trojki
    return [
        [0,1,2],
        [0,3,5],
        [1,9,17],
        [2,4,7],
        [8,9,10],
        [8,11,13],
        [10,12,15],
        [16,17,18],
        [16,19,21],
        [18,20,23],
        [21,22,23],
        [22,16,6],
        [13,14,15],
        [5,6,7],
        [3,11,19],
        [20,12,4]
    ]

def trojke_polja(polje): #vraca trojke koje sadrze dato polje
    if polje==0:
        return [[0,1,2],[0,3,5]]
    elif polje==1:
        return [[0,1,2],[1,9,17]]
    elif polje==2:
        return [[0,1,2],[2,4,7]]
    elif polje==3:
        return [[0,3,5],[3,11,19]]
    elif polje==4:
        return [[2,4,7],[20,12,4]]
    elif polje==5:
        return [[0,3,5],[5,6,7]]
    elif polje==6:
        return [[5,6,7],[6,14,22]]
    elif polje==7:
        return [[5,6,7],[7,4,2]]
    elif polje==8:
        return [[8,9,10],[8,11,13]]
    elif polje==9:
        return [[8,9,10],[1,9,17]]
    elif polje==10:
        return [[8,9,10],[10,12,15]]
    elif polje==11:
        return [[3,11,19],[8,11,13]]
    elif polje==12:
        return [[10,12,15],[20,12,4]]
    elif polje==13:
        return [[8,11,13],[13,14,15]]
    elif polje==14:
        return [[13,14,15],[22,14,6]]
    elif polje==15:
        return [[13,14,15],[10,12,15]]
    elif polje==16:
        return [[16,17,18],[16,19,21]]
    elif polje==17:
        return [[16,17,18],[1,9,17]]
    elif polje==18:
        return [[16,17,18],[18,20,23]]
    elif polje==19:
        return [[3,11,19],[16,19,21]]
    elif polje==20:
        return [[18,20,23],[20,12,4]]
    elif polje==21:
        return [[16,19,21],[21,22,23]]
    elif polje==22:
        return [[21,22,23],[22,14,6]]
    elif polje==23:
        return [[21,22,23],[18,20,23]]

if __name__=="__main__":
    tabla=["O"]*24
    tabla[0]="1"
    tabla[1]="2"
    tabla[2] = "2"
    tabla[3] = "1"
    tabla[4] = "O"
    tabla[5] = "1"
    tabla[6] = "O"
    tabla[7] = "O"
    tabla[8] = "O"
    tabla[9] = "O"
    tabla[10] = "O"
    tabla[11] = "O"
    tabla[12] = "O"
    tabla[13] = "O"
    tabla[14] = "O"
    tabla[15] = "O"
    tabla[16] = "O"
    tabla[17] = "O"
    tabla[18] = "O"
    tabla[19] = "O"
    tabla[20] = "O"
    tabla[21] = "O"
    tabla[22]="O"
    tabla[23]="O"

    logika.print_tabla(tabla)
    start=time.time()
    # for i in range(600):
    print(broj_vezanih_trojki("1",tabla,"2"))
    print(broj_blokiranih_figura("1",tabla,"2"))
    #print(broj_vezanih_dvojki(tabla,"1"))
    #print(broj_vezanih_dvojki(tabla,"2"))
    print(broj_figura(tabla,"1","2"))
    #print(dupla_trojka(tabla,"1","2"))
