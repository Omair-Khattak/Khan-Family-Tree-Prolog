
from pyswip import Prolog
prolog=Prolog()
prolog.consult("BackEnd.pl")


def Show_Relations():
    print("Enter 1 for Beti_______Enter 2 for Beta\t\t\t\t")
    print("Enter 3 for Dada_______Enter 4 for Nana\t\t\t\t")
    print("Enter 5 for Dadi_______Enter 6 for Nani\t\t\t\t")
    print("Enter 7 for Sala_______Enter 8 for Bahu\t\t\t\t")
    print("Enter 9 for Pota_______Enter 10 for Nawasa\t\t\t")
    print("Enter 11 for BaapDada_______Enter 12 for Khala\t\t\t")
    print("Enter 13 for Pota_______Enter 0 for Exit\t\t\t\n\t\t\t\t\t\t\t\t")
    print("#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")

def Khan_Family():
    print("#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#\n")
    print("\t\t\t\t\t\t\t\t\nKhan Family Members:\t\t\t\t\t\n\t\t\t\t\t\t\t\t")
    print("ChoteKhan, ChotiRani, BarreKhan, BarriRani\t\t\t")
    print("Salim, Kausar, Nadir, Asad, Nahid, Sumra\t\t\t")
    print("Rizwan, Burhan, Rashid, Akram, Salima, Sanam, Rabia\t\t\n")
    print("#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#\n\n")

def Continue_Stop():
        while(True):
            decide = input("\n#=#=#=#=#=> Enter C to Continue and S to Stop <=#=#=#=#=#\n")
            if decide == "C" or decide == "c":
                return True
            elif decide == "S"  or decide == "s":
                return False
            else:
                print("#=#=#=#=#=> Wrong Choice ! <=#=#=#=#=#\n")  


def main():
    print("#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#\n")

    inputt = None
    find = False

    while(inputt!=0):
        Show_Relations()    
        while True: 
            choice = {"0","1","2","3","4","5","6","7","8","9","10","11","12","13"}
            inputt=input("\n#==> Enter your preference for the type of relationship you want <==#\n")
            if inputt in choice:
                inputt = int(inputt)
                break
            else:
                print("\n#==> Wrong Choice <==#")
                continue
        if(inputt==1):
            Khan_Family()
            User_input=input("Enter person's Name whose Beti is required : ")
            User_input=User_input.lower()
            for i in prolog.query("beti(X,"+User_input+")"):
                find = True
                print("\n#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
                print("Ms.{0} is the beti of {1}.".format(i["X"], User_input))
                print("#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
                
        if(inputt==2):
            Khan_Family()  
            User_input=input("Enter person's Name whose Beta is required : ")
            User_input=User_input.lower()
            for i in prolog.query("beta(X,"+User_input+")"):
                find = True
                print("\n#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
                print("Mr.{0} is the beta of {1}.".format(i["X"], User_input))
                print("#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")

        if(inputt==3):
            Khan_Family()  
            User_input=input("Enter person's Name whose Dada is required : ")
            User_input=User_input.lower()
            for i in prolog.query("dada(X,"+User_input+")"):
                find = True
                print("\n#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
                print("Mr.{0} is the dada of {1}.".format(i["X"], User_input))
                print("#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
                
        if(inputt==4):
            Khan_Family()  
            User_input=input("Enter person's Name whose Nana is required : ")
            User_input=User_input.lower()
            for i in prolog.query("nana(X,"+User_input+")"):
                find = True
                print("\n#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
                print("Mr.{0} is the nana of {1}.".format(i["X"], User_input))
                print("#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
                
        if(inputt==5):
            Khan_Family()  
            User_input=input("Enter person's Name whose Dadi is required : ")
            User_input=User_input.lower()
            for i in prolog.query("dadi(X,"+User_input+")"):
                find = True
                print("\n#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
                print("Ms.{0} is the dadi of {1}.".format(i["X"], User_input))
                print("#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
                
        if(inputt==6):
            Khan_Family()  
            User_input=input("Enter person's Name whose Nani is required : ")
            User_input=User_input.lower()
            for i in prolog.query("nani(X,"+User_input+")"):
                find = True
                print("\n#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
                print("Ms.{0} is the nani of {1}.".format(i["X"], User_input))
                print("#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
            
        if(inputt==7):
            Khan_Family()  
            User_input=input("Enter person's Name whose Sala is required : ")
            User_input=User_input.lower()
            for i in prolog.query("sala(X,"+User_input+")"):
                find = True
                print("\n#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
                print("Mr.{0} is the sala of {1}.".format(i["X"], User_input))
                print("#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
                
        if(inputt==8):
            Khan_Family()  
            User_input=input("Enter person's Name whose Bahu is required : ")
            User_input=User_input.lower()
            for i in prolog.query("bahu(X,"+User_input+")"):
                find = True
                print("\n#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
                print("Ms.{0} is the bahu of {1}.".format(i["X"], User_input))
                print("#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
                

        if(inputt==9):
            Khan_Family()  
            User_input=input("Enter person's Name whose Pota is required : ")
            User_input=User_input.lower()
            for i in prolog.query("pota(X,"+User_input+")"):
                find = True
                print("\n#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
                print("Mr.{0} is the pota of {1}.".format(i["X"], User_input))
                print("#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
                
        if(inputt==10):
            Khan_Family()  
            User_input=input("Enter person's Name whose Nawasa is required : ")
            User_input=User_input.lower()
            for i in prolog.query("nawasa(X,"+User_input+")"):
                find = True
                print("\n#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
                print("Mr.{0} is the nawasa of {1}.".format(i["X"], User_input))
                print("#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
                
        if(inputt==11):
            Khan_Family()  
            User_input=input("Enter person's Name whose BaapDada is required : ")
            User_input=User_input.lower()
            for i in prolog.query("baapDada(X,"+User_input+")"):
                find = True
                print("\n#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
                print("Mr.{0} is the baapDada of {1}.".format(i["X"], User_input))
                print("#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
                
        if(inputt==12):
            Khan_Family()  
            User_input=input("Enter person's Name whose Khala is required : ")
            User_input=User_input.lower()
            for i in prolog.query("khala(X,"+User_input+")"):
                find = True
                print("\n#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
                print("Ms.{0} is the khala of {1}.".format(i["X"], User_input))
                print("#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
                

        if(inputt==13):
            Khan_Family()  
            User_input=input("Enter person's Name whose ChachaTaya is required : ")
            User_input=User_input.lower()
            for i in prolog.query("chachataya(X,"+User_input+")"):
                find = True
                print("\n#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
                print("Mr.{0} is the chachataya of {1}.".format(i["X"], User_input))
                print("#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")

        if find == False:
            print("\n#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
            print("No Relationship or Invalid Input.")
            print("#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")

        if Continue_Stop() == True:
            continue
        else:
            break
    print("\n\n#=#=#=#=#=#=#=#=#===> Thank You  <===#=#=#=#=#=#=#=#=#\n")
        

if __name__=="__main__":
    main()
