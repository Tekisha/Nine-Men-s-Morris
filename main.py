from pvp import pVp
from pvc import pvc

def main():
   
    while True:

        print("MENI")
        print("1. Igrac vs Igrac")
        print("2. Igrac vs AI")
        print("Q izlaz")

        print("\n")

        opcija=input("Izaberite opciju igre: ")
        if opcija in ["1","1."]:
            pVp()
        elif opcija in ["2","2."]:
            pvc()
        elif opcija in ["Q","q"]:
            quit()
        else:
            print("Niste uneli ponudjenu opciju. Pokusajte ponovo!")









if __name__=="__main__":
    main()