import colorama
from colorama import Fore

print(Fore.RED + "Starting.......\n")
print(Fore.BLUE + "           ------------------- ")
print(Fore.BLUE + "           |                  ")
print(Fore.BLUE + "           |                  ")
print(Fore.BLUE + "           |                  ")
print(Fore.BLUE + "           |                  ")
print(Fore.BLUE + "           |       -----------")
print(Fore.BLUE + "           |       |         |")
print(Fore.BLUE + "           |       |         |   ------- |------| |       -------- |       | |      |-------| _________ |------| |-----|")
print(Fore.BLUE + "           |                 |   |       |      | |       |        |       | |      |       |     |     |      | |_____|")
print(Fore.BLUE + "           |                 |   |       |------| |       |        |       | |      |-------|     |     |      | |\_")
print(Fore.BLUE + "           -------------------   |------ |      | |------ |------- |-------| |----- |       |     |     |------| |  \_")
pas = int(input("\n" + Fore.CYAN + "Please enter the password: "))
if (pas == 2015):
    print("Welcome, Priyanshu Bag")
    print(Fore.GREEN + " Plan ====== Pro(Premium)")
    print("------------------------------------------------------------------------------------------------\n\n")

    o = 0
    nc = 1
    while (o == 0):
        op = int(input(Fore.YELLOW + "Enter your choice:\n1.power calculation                               11.Unit convertor (meter)\n2.multiplication                                  12.Unit convertor (litre)\n3.division                                        13.Unit Converter (gram)\n4.addition                                        14.Area finder(2D)\n5.subtaction                                      15.volume finder(3D)\n6.division (remainder)                            16.Temperature convertor\n7.root finder\n8.division (divident)\n9.division (divisor)\n10.division (divisor with remainder)\n----------------> "))
        print("\n\n")
        if (op == 1):
            print("                                                   Session --",nc,"                                  ")
            no = float(input("Enter the number: "))
            p = int(input("Enter the power: "))
            ans = no**p
            nc = nc + 1
            print("The answer is",ans,"\n\n                                                   Session --",nc,"                                  ")
        elif (op == 2):
            print("                                                   Session --",nc,"                                  ")
            no = float(input("Enter the number: "))
            p = float(input("Enter the other number: "))
            ans = no*p
            nc = nc + 1
            print("The answer is",ans,"\n\n                                                   Session --",nc,"                                  ")
        elif (op == 3):
            print("                                                   Session --",nc,"                                  ")
            no = float(input("Enter the divident: "))
            p = float(input("Enter the divisor: "))
            ans = no/p
            nc = nc + 1
            print("The answer is",ans,"\n\n                                                   Session --",nc,"                                  ")
        elif (op == 4):
            print("                                                   Session --",nc,"                                  ")
            no = float(input("Enter the number: "))
            p = float(input("Enter the other number: "))
            ans = no + p
            nc = nc + 1
            print("The answer is",ans,"\n\n                                                   Session --",nc,"                                  ")
        elif (op == 5):
            print("                                                   Session --",nc,"                                  ")
            no = float(input("Enter the number from which you want to substract: "))
            p = float(input("Enter the number which you want to subtract: "))
            ans = no - p 
            nc = nc + 1
            print("The answer is",ans,"\n\n                                                   Session --",nc,"                                  ")
        elif (op == 6):
            print("                                                   Session --",nc,"                                  ")
            no = int(input("Enter the divident: "))
            p = int(input("Enter the divisor: "))
            ans = no%p 
            nc = nc + 1
            print("The answer is",ans,"\n\n                                                   Session --",nc,"                                  ")
        elif (op == 7):
            print("                                                   Session --",nc,"                                  ")
            no = float(input("Enter the number: "))
            import math
            ans = math.sqrt(no)
            nc = nc + 1
            print("The answer is",ans,"\n\n                                                   Session --",nc,"                                  ")
        elif (op == 8):
            print("                                                   Session --",nc,"                                  ")        
            opt = int(input("Do you have you remainder as 0? (1.No ; 2.Yes): "))
            if (opt == 1):
                no = float(input("Enter the divisor: "))
                p = float(input("Enter the quotient: "))
                ans = no*p 
                nc = nc + 1
                print("The answer is",ans,"\n\n                                                   Session --",nc,"                                  ")
            else:
                no = float(input("Enter the divisor: "))
                p = int(input("Enter the quotient: "))
                re = int(input("Enter the remainder: "))
                ans = (no*p) + re
                nc = nc + 1
                print("The answer is",ans,"\n\n                                                   Session --",nc,"                                  ")
        elif (op == 9):
            print("                                                   Session --",nc,"                                  ")
            no = float(input("Enter the quotient: "))
            p = float(input("Enter the divident: "))
            ans = p/no
            nc = nc + 1
            print("The answer is",ans,"\n\n                                                   Session --",nc,"                                  ")
        elif (op == 10):
            print("                                                   Session --",nc,"                                  ")
            no = float(input("Enter the quotient: "))
            p = float(input("Enter the divident: "))
            ans = p/no
            nc = nc + 1
            rem = p%no
            print("The remainder is",rem)
            print("The divisor (in interger) is",int(ans))
            print("The divisor (in decimal) is",ans,"\n\n                                                   Session --",nc,"                                  ")
        elif (op == 11):
            ions = int(input("Please enter the given unit:\n1.Km\n2.Hm\n3.Dm\n4.m\n5.dm\n6.cm\n7.mm\n------------>"))
            nons = int(input("\nPlease enter the coverting unit:\n1.Km\n2.Hm\n3.Dm\n4.m\n5.dm\n6.cm\n7.mm\n------------>"))
            if (ions == 1 and nons == 1):
                op = float(input("Enter the value of the given unit: "))
                ans = op
                nc = nc + 1
                print("The answer is",ans,"Km\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 1 and nons == 2):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10
                nc = nc + 1
                print("The answer is",ans,"Hm\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 1 and nons == 3):
                op = float(input("Enter the value of the given unit: "))
                ans = op*100
                nc = nc + 1
                print("The answer is",ans,"Dm\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 1 and nons == 4):
                op = float(input("Enter the value of the given unit: "))
                ans = op*1000
                nc = nc + 1
                print("The answer is",ans,"m\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 1 and nons == 5):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10000
                nc = nc + 1
                print("The answer is",ans,"dm\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 1 and nons == 6):
                op = float(input("Enter the value of the given unit: "))
                ans = op*100000
                nc = nc + 1
                print("The answer is",ans,"cm\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 1 and nons == 7):
                op = float(input("Enter the value of the given unit: "))
                ans = op*1000000
                nc = nc + 1
                print("The answer is",ans,"mm\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 2 and nons == 1):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10)
                nc = nc + 1
                print("The answer is",ans,"Km\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 2 and nons == 2):
                op = float(input("Enter the value of the given unit: "))
                ans = op
                nc = nc + 1
                print("The answer is",ans,"Hm\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 2 and nons == 3):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10
                nc = nc + 1
                print("The answer is",ans,"Dm\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 2 and nons == 4):
                op = float(input("Enter the value of the given unit: "))
                ans = op*100
                nc = nc + 1
                print("The answer is",ans,"m\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 2 and nons == 5):
                op = float(input("Enter the value of the given unit: "))
                ans = op*1000
                nc = nc + 1
                print("The answer is",ans,"dm\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 2 and nons == 6):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10000
                nc = nc + 1
                print("The answer is",ans,"cm\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 2 and nons == 7):
                op = float(input("Enter the value of the given unit: "))
                ans = op*100000
                nc = nc + 1
                print("The answer is",ans,"mm\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 3 and nons == 1):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/100)
                nc = nc + 1
                print("The answer is",ans,"Km\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 3 and nons == 2):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10)
                nc = nc + 1
                print("The answer is",ans,"Hm\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 3 and nons == 3):
                op = float(input("Enter the value of the given unit: "))
                ans = op
                nc = nc + 1
                print("The answer is",ans,"Dm\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 3 and nons == 4):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10
                nc = nc + 1
                print("The answer is",ans,"m\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 3 and nons == 5):
                op = float(input("Enter the value of the given unit: "))
                ans = op*100
                nc = nc + 1
                print("The answer is",ans,"dm\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 3 and nons == 6):
                op = float(input("Enter the value of the given unit: "))
                ans = op*1000
                nc = nc + 1
                print("The answer is",ans,"cm\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 3 and nons == 7):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10000
                nc = nc + 1
                print("The answer is",ans,"mm\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 4 and nons == 1):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/1000)
                nc = nc + 1
                print("The answer is",ans,"Km\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 4 and nons == 2):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/100)
                nc = nc + 1
                print("The answer is",ans,"Hm\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 4 and nons == 3):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10)
                nc = nc + 1
                print("The answer is",ans,"Dm\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 4 and nons == 4):
                op = float(input("Enter the value of the given unit: "))
                ans = op
                nc = nc + 1
                print("The answer is",ans,"m\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 4 and nons == 5):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10
                nc = nc + 1
                print("The answer is",ans,"dm\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 4 and nons == 6):
                op = float(input("Enter the value of the given unit: "))
                ans = op*100
                nc = nc + 1
                print("The answer is",ans,"cm\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 4 and nons == 7):
                op = float(input("Enter the value of the given unit: "))
                ans = op*1000
                nc = nc + 1
                print("The answer is",ans,"mm\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 5 and nons == 1):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10000)
                nc = nc + 1
                print("The answer is",ans,"Km\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 5 and nons == 2):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/1000)
                nc = nc + 1
                print("The answer is",ans,"Hm\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 5 and nons == 3):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/100)
                nc = nc + 1
                print("The answer is",ans,"Dm\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 5 and nons == 4):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10)
                nc = nc + 1
                print("The answer is",ans,"m\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 5 and nons == 5):
                op = float(input("Enter the value of the given unit: "))
                ans = op
                nc = nc + 1
                print("The answer is",ans,"dm\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 5 and nons == 6):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10
                nc = nc + 1
                print("The answer is",ans,"cm\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 5 and nons == 7):
                op = float(input("Enter the value of the given unit: "))
                ans = op*100
                nc = nc + 1
                print("The answer is",ans,"mm\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 6 and nons == 1):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/100000)
                nc = nc + 1
                print("The answer is",ans,"Km\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 6 and nons == 2):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10000)
                nc = nc + 1
                print("The answer is",ans,"Hm\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 6 and nons == 3):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/1000)
                nc = nc + 1
                print("The answer is",ans,"Dm\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 6 and nons == 4):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/100)
                nc = nc + 1
                print("The answer is",ans,"m\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 6 and nons == 5):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10)
                nc = nc + 1
                print("The answer is",ans,"dm\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 6 and nons == 6):
                op = float(input("Enter the value of the given unit: "))
                ans = op
                nc = nc + 1
                print("The answer is",ans,"cm\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 6 and nons == 7):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10
                nc = nc + 1
                print("The answer is",ans,"mm\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 7 and nons == 1):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/1000000)
                nc = nc + 1
                print("The answer is",ans,"Km\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 7 and nons == 2):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/100000)
                nc = nc + 1
                print("The answer is",ans,"Hm\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 7 and nons == 3):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10000)
                nc = nc + 1
                print("The answer is",ans,"Dm\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 7 and nons == 4):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/1000)
                nc = nc + 1
                print("The answer is",ans,"m\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 7 and nons == 5):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/100)
                nc = nc + 1
                print("The answer is",ans,"dm\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 7 and nons == 6):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10)
                nc = nc + 1
                print("The answer is",ans,"cm\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 7 and nons == 7):
                op = float(input("Enter the value of the given unit: "))
                ans = op
                nc = nc + 1
                print("The answer is",ans,"mm\n\n                                                    Session --",nc,"                                 ")
        elif (op == 12):
            ions = int(input("Please enter the given unit:\n1.Kl\n2.Hl\n3.Dl\n4.l\n5.dl\n6.cl\n7.ml\n------------>"))
            nons = int(input("\nPlease enter the coverting unit:\n1.Kl\n2.Hl\n3.Dl\n4.l\n5.dl\n6.cl\n7.ml\n------------>"))
            if (ions == 1 and nons == 1):
                op = float(input("Enter the value of the given unit: "))
                ans = op
                nc = nc + 1
                print("The answer is",ans,"Kl\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 1 and nons == 2):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10
                nc = nc + 1
                print("The answer is",ans,"Hl\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 1 and nons == 3):
                op = float(input("Enter the value of the given unit: "))
                ans = op*100
                nc = nc + 1
                print("The answer is",ans,"Dl\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 1 and nons == 4):
                op = float(input("Enter the value of the given unit: "))
                ans = op*1000
                nc = nc + 1
                print("The answer is",ans,"l\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 1 and nons == 5):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10000
                nc = nc + 1
                print("The answer is",ans,"dl\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 1 and nons == 6):
                op = float(input("Enter the value of the given unit: "))
                ans = op*100000
                nc = nc + 1
                print("The answer is",ans,"cl\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 1 and nons == 7):
                op = float(input("Enter the value of the given unit: "))
                ans = op*1000000
                nc = nc + 1
                print("The answer is",ans,"ml\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 2 and nons == 1):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10)
                nc = nc + 1
                print("The answer is",ans,"Kl\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 2 and nons == 2):
                op = float(input("Enter the value of the given unit: "))
                ans = op
                nc = nc + 1
                print("The answer is",ans,"Hl\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 2 and nons == 3):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10
                nc = nc + 1
                print("The answer is",ans,"Dl\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 2 and nons == 4):
                op = float(input("Enter the value of the given unit: "))
                ans = op*100
                nc = nc + 1
                print("The answer is",ans,"l\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 2 and nons == 5):
                op = float(input("Enter the value of the given unit: "))
                ans = op*1000
                nc = nc + 1
                print("The answer is",ans,"dl\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 2 and nons == 6):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10000
                nc = nc + 1
                print("The answer is",ans,"cl\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 2 and nons == 7):
                op = float(input("Enter the value of the given unit: "))
                ans = op*100000
                nc = nc + 1
                print("The answer is",ans,"ml\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 3 and nons == 1):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/100)
                nc = nc + 1
                print("The answer is",ans,"Kl\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 3 and nons == 2):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10)
                nc = nc + 1
                print("The answer is",ans,"Hl\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 3 and nons == 3):
                op = float(input("Enter the value of the given unit: "))
                ans = op
                nc = nc + 1
                print("The answer is",ans,"Dl\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 3 and nons == 4):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10
                nc = nc + 1
                print("The answer is",ans,"l\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 3 and nons == 5):
                op = float(input("Enter the value of the given unit: "))
                ans = op*100
                nc = nc + 1
                print("The answer is",ans,"dl\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 3 and nons == 6):
                op = float(input("Enter the value of the given unit: "))
                ans = op*1000
                nc = nc + 1
                print("The answer is",ans,"cl\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 3 and nons == 7):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10000
                nc = nc + 1
                print("The answer is",ans,"ml\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 4 and nons == 1):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/1000)
                nc = nc + 1
                print("The answer is",ans,"Kl\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 4 and nons == 2):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/100)
                nc = nc + 1
                print("The answer is",ans,"Hl\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 4 and nons == 3):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10)
                nc = nc + 1
                print("The answer is",ans,"Dl\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 4 and nons == 4):
                op = float(input("Enter the value of the given unit: "))
                ans = op
                nc = nc + 1
                print("The answer is",ans,"l\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 4 and nons == 5):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10
                nc = nc + 1
                print("The answer is",ans,"dl\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 4 and nons == 6):
                op = float(input("Enter the value of the given unit: "))
                ans = op*100
                nc = nc + 1
                print("The answer is",ans,"cl\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 4 and nons == 7):
                op = float(input("Enter the value of the given unit: "))
                ans = op*1000
                nc = nc + 1
                print("The answer is",ans,"ml\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 5 and nons == 1):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10000)
                nc = nc + 1
                print("The answer is",ans,"Kl\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 5 and nons == 2):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/1000)
                nc = nc + 1
                print("The answer is",ans,"Hl\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 5 and nons == 3):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/100)
                nc = nc + 1
                print("The answer is",ans,"Dl\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 5 and nons == 4):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10)
                nc = nc + 1
                print("The answer is",ans,"l\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 5 and nons == 5):
                op = float(input("Enter the value of the given unit: "))
                ans = op
                nc = nc + 1
                print("The answer is",ans,"dl\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 5 and nons == 6):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10
                nc = nc + 1
                print("The answer is",ans,"cl\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 5 and nons == 7):
                op = float(input("Enter the value of the given unit: "))
                ans = op*100
                nc = nc + 1
                print("The answer is",ans,"ml\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 6 and nons == 1):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/100000)
                nc = nc + 1
                print("The answer is",ans,"Kl\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 6 and nons == 2):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10000)
                nc = nc + 1
                print("The answer is",ans,"Hl\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 6 and nons == 3):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/1000)
                nc = nc + 1
                print("The answer is",ans,"Dl\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 6 and nons == 4):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/100)
                nc = nc + 1
                print("The answer is",ans,"l\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 6 and nons == 5):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10)
                nc = nc + 1
                print("The answer is",ans,"dl\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 6 and nons == 6):
                op = float(input("Enter the value of the given unit: "))
                ans = op
                nc = nc + 1
                print("The answer is",ans,"cl\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 6 and nons == 7):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10
                nc = nc + 1
                print("The answer is",ans,"ml\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 7 and nons == 1):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/1000000)
                nc = nc + 1
                print("The answer is",ans,"Kl\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 7 and nons == 2):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/100000)
                nc = nc + 1
                print("The answer is",ans,"Hl\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 7 and nons == 3):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10000)
                nc = nc + 1
                print("The answer is",ans,"Dl\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 7 and nons == 4):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/1000)
                nc = nc + 1
                print("The answer is",ans,"l\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 7 and nons == 5):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/100)
                nc = nc + 1
                print("The answer is",ans,"dl\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 7 and nons == 6):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10)
                nc = nc + 1
                print("The answer is",ans,"cl\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 7 and nons == 7):
                op = float(input("Enter the value of the given unit: "))
                ans = op
                nc = nc + 1
                print("The answer is",ans,"ml\n\n                                                    Session --",nc,"                                 ")
        elif (op == 13):
            ions = int(input("Please enter the given unit:\n1.Kg\n2.Hg\n3.Dg\n4.g\n5.dg\n6.cg\n7.mg\n------------>"))
            nons = int(input("\nPlease enter the coverting unit:\n1.Kg\n2.Hg\n3.Dg\n4.g\n5.dg\n6.cg\n7.mg\n------------>"))
            if (ions == 1 and nons == 1):
                op = float(input("Enter the value of the given unit: "))
                ans = op
                nc = nc + 1
                print("The answer is",ans,"Kg\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 1 and nons == 2):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10
                nc = nc + 1
                print("The answer is",ans,"Hg\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 1 and nons == 3):
                op = float(input("Enter the value of the given unit: "))
                ans = op*100
                nc = nc + 1
                print("The answer is",ans,"Dg\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 1 and nons == 4):
                op = float(input("Enter the value of the given unit: "))
                ans = op*1000
                nc = nc + 1
                print("The answer is",ans,"g\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 1 and nons == 5):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10000
                nc = nc + 1
                print("The answer is",ans,"dg\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 1 and nons == 6):
                op = float(input("Enter the value of the given unit: "))
                ans = op*100000
                nc = nc + 1
                print("The answer is",ans,"cg\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 1 and nons == 7):
                op = float(input("Enter the value of the given unit: "))
                ans = op*1000000
                nc = nc + 1
                print("The answer is",ans,"mg\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 2 and nons == 1):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10)
                nc = nc + 1
                print("The answer is",ans,"Kg\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 2 and nons == 2):
                op = float(input("Enter the value of the given unit: "))
                ans = op
                nc = nc + 1
                print("The answer is",ans,"Hg\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 2 and nons == 3):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10
                nc = nc + 1
                print("The answer is",ans,"Dg\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 2 and nons == 4):
                op = float(input("Enter the value of the given unit: "))
                ans = op*100
                nc = nc + 1
                print("The answer is",ans,"g\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 2 and nons == 5):
                op = float(input("Enter the value of the given unit: "))
                ans = op*1000
                nc = nc + 1
                print("The answer is",ans,"dg\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 2 and nons == 6):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10000
                nc = nc + 1
                print("The answer is",ans,"cg\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 2 and nons == 7):
                op = float(input("Enter the value of the given unit: "))
                ans = op*100000
                nc = nc + 1
                print("The answer is",ans,"mg\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 3 and nons == 1):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/100)
                nc = nc + 1
                print("The answer is",ans,"Kg\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 3 and nons == 2):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10)
                nc = nc + 1
                print("The answer is",ans,"Hg\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 3 and nons == 3):
                op = float(input("Enter the value of the given unit: "))
                ans = op
                nc = nc + 1
                print("The answer is",ans,"Dg\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 3 and nons == 4):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10
                nc = nc + 1
                print("The answer is",ans,"g\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 3 and nons == 5):
                op = float(input("Enter the value of the given unit: "))
                ans = op*100
                nc = nc + 1
                print("The answer is",ans,"dg\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 3 and nons == 6):
                op = float(input("Enter the value of the given unit: "))
                ans = op*1000
                nc = nc + 1
                print("The answer is",ans,"cg\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 3 and nons == 7):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10000
                nc = nc + 1
                print("The answer is",ans,"mg\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 4 and nons == 1):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/1000)
                nc = nc + 1
                print("The answer is",ans,"Kg\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 4 and nons == 2):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/100)
                nc = nc + 1
                print("The answer is",ans,"Hg\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 4 and nons == 3):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10)
                nc = nc + 1
                print("The answer is",ans,"Dg\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 4 and nons == 4):
                op = float(input("Enter the value of the given unit: "))
                ans = op
                nc = nc + 1
                print("The answer is",ans,"g\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 4 and nons == 5):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10
                nc = nc + 1
                print("The answer is",ans,"dg\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 4 and nons == 6):
                op = float(input("Enter the value of the given unit: "))
                ans = op*100
                nc = nc + 1
                print("The answer is",ans,"cg\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 4 and nons == 7):
                op = float(input("Enter the value of the given unit: "))
                ans = op*1000
                nc = nc + 1
                print("The answer is",ans,"mg\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 5 and nons == 1):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10000)
                nc = nc + 1
                print("The answer is",ans,"Kg\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 5 and nons == 2):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/1000)
                nc = nc + 1
                print("The answer is",ans,"Hg\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 5 and nons == 3):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/100)
                nc = nc + 1
                print("The answer is",ans,"Dg\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 5 and nons == 4):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10)
                nc = nc + 1
                print("The answer is",ans,"g\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 5 and nons == 5):
                op = float(input("Enter the value of the given unit: "))
                ans = op
                nc = nc + 1
                print("The answer is",ans,"dg\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 5 and nons == 6):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10
                nc = nc + 1
                print("The answer is",ans,"cg\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 5 and nons == 7):
                op = float(input("Enter the value of the given unit: "))
                ans = op*100
                nc = nc + 1
                print("The answer is",ans,"mg\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 6 and nons == 1):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/100000)
                nc = nc + 1
                print("The answer is",ans,"Kg\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 6 and nons == 2):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10000)
                nc = nc + 1
                print("The answer is",ans,"Hg\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 6 and nons == 3):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/1000)
                nc = nc + 1
                print("The answer is",ans,"Dg\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 6 and nons == 4):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/100)
                nc = nc + 1
                print("The answer is",ans,"g\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 6 and nons == 5):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10)
                nc = nc + 1
                print("The answer is",ans,"dg\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 6 and nons == 6):
                op = float(input("Enter the value of the given unit: "))
                ans = op
                nc = nc + 1
                print("The answer is",ans,"cg\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 6 and nons == 7):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10
                nc = nc + 1
                print("The answer is",ans,"mg\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 7 and nons == 1):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/1000000)
                nc = nc + 1
                print("The answer is",ans,"Kg\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 7 and nons == 2):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/100000)
                nc = nc + 1
                print("The answer is",ans,"Hg\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 7 and nons == 3):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10000)
                nc = nc + 1
                print("The answer is",ans,"Dg\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 7 and nons == 4):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/1000)
                nc = nc + 1
                print("The answer is",ans,"g\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 7 and nons == 5):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/100)
                nc = nc + 1
                print("The answer is",ans,"dg\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 7 and nons == 6):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10)
                nc = nc + 1
                print("The answer is",ans,"cg\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 7 and nons == 7):
                op = float(input("Enter the value of the given unit: "))
                ans = op
                nc = nc + 1
                print("The answer is",ans,"mg\n\n                                                    Session --",nc,"                                 ")
        elif (op == 14):
            shape = int(input("Please enter the figure: \n1.Circle                        6.trapezoid                     11.hexagon\n2.Square/Rectangle              7.parallelogram                 12.octagon\n3.Triangle                      8.rhombus                       13.annulus\n4.Sector                        9.kite                          14.quadrilateral\n5.Ellipsis                     10.pentagon\n------------->"))
            if (shape == 1):
                pie = 3.14
                r = float(input("Please enter the the value of the radius: "))
                area = float(pie*(r**2))
                nc = nc + 1
                print("The answer is",area,"\n\n                                                    Session --",nc,"                                 ")
            elif (shape == 2):
                length = float(input("Please enter the length: "))
                breadth = float(input("Please enter the breadth: "))
                area = float(length*breadth)
                nc = nc + 1
                print("The answer is",area,"\n\n                                                    Session --",nc,"                                 ")
            elif (shape == 3):
                base = float(input("Please enter the base: "))
                height = float(input("Please enter the height: "))
                area = float(1/2 * base * height)
                nc = nc + 1
                print("The answer is",area,"\n\n                                                    Session --",nc,"                                 ")
            elif (shape == 4):
                Radius = float(input("Enter the value of the radius: "))
                Angle = float(input("Enter the value of the angle: "))
                area = float((Radius**2)*Angle / 2)
                nc = nc + 1
                print("The answer is",area,"\n\n                                                    Session --",nc,"                                 ")
            elif (shape == 5):
                large = float(input("Enter the value of the large radius: "))
                small = float(input("Enter the value of small radius: "))
                pie = 3.14
                area = float(pie*large*small)
                nc = nc + 1
                print("The answer is",area,"\n\n                                                    Session --",nc,"                                 ")
            elif (shape == 6):
                a = float(input("Enter the value of the first parallel line: "))
                b = float(input("Enter the value of the second parallel line: "))
                h = float(input("Enter the height of the trapezoid: "))
                area = float((a + b) * h / 2)
                nc = nc + 1
                print("The answer is",area,"\n\n                                                    Session --",nc,"                                 ")
            elif (shape == 7):
                h = float(input("Enter the height of the parallelogram: "))
                b = float(input("Enter the base of the parallelogram: "))
                area = float(b*h)
                nc =  nc + 1
                print("The answer is",area,"\n\n                                                    Session --",nc,"                                 ")
            elif (shape == 8):
                h = float(input("Enter the height of the rhombus: "))
                b = float(input("Enter the base of the rhombus: "))
                area = float(b*h)
                nc =  nc + 1
                print("The answer is",area,"\n\n                                                    Session --",nc,"                                 ")
            elif (shape == 9):
                e = float(input("Enter the length of the diagonally joined vertical line: "))
                f = float(input("Enter the length of the diagonally joined horizontal line: "))
                area = float((e * f) / 2)
                nc = nc + 1
                print("The answer is",area,"\n\n                                                    Session --",nc,"                                 ")
            elif (shape == 10):
                import math
                gg = math.sqrt(5*(5 + 2 * math.sqrt(5)))
                a = float(input("Enter the side of the pentagon: "))
                area = float(1/4 * gg * (a**2))
                nc = nc + 1
                print("The answer is",area,"\n\n                                                    Session --",nc,"                                 ")
            elif (shape == 11):
                import math
                gg = math.sqrt(3)
                a = float(input("Enter the length of the side: "))
                area = float(3/2*gg*(a**2))
                nc = nc + 1
                print("The answer is",area,"\n\n                                                    Session --",nc,"                                 ")
            elif (shape == 12):
                import math
                gg = math.sqrt(2)
                a = float(input("Enter the length of the side: "))
                area = float(2*(1 + gg)*(a**2))
                nc =  nc + 1
                print("The answer is",area,"\n\n                                                    Session --",nc,"                                 ")
            elif (shape == 13):
                pie = 3.14
                large = float(input("Enter the radius of the large circle: "))
                small = float(input("Enter the radius of the small circle: "))
                area = float(pie*(large**2 - small**2))
                nc = nc + 1
                print("The answer is",area,"\n\n                                                    Session --",nc,"                                 ")
            elif (shape == 14):
                e = float(input("Enter the first diagonal length: "))
                f = float(input("Enter the second diagonal length: "))
                a = float(input("Enter the value of angle formed at the intersection of the two diagonals: "))
                area = float(e * f * (180 - a))
                nc = nc + 1
                print("The answer is",area,"\n\n                                                    Session --",nc,"                                 ")
        elif (op == 15):
            shape = int(input("Enter your choice:\n1.sphere                    6.capsule\n2.cube\n3.cone\n4.cylinder\n5.cuboid\n---------------->"))
            if (shape == 1):
                pie = 3.14
                r = float(input("Enter the radius: "))
                v = float((4/3)*pie*(r**3))
                nc = nc + 1
                print("The answer is",v,"\n\n                                                    Session --",nc,"                                 ")
            elif (shape == 2):
                a = float(input("Enter the length of the height: "))
                v = float(a**3)
                nc = nc + 1
                print("The answer is",v,"\n\n                                                    Session --",nc,"                                 ")
            elif (shape == 3):
                pie = 3.14
                r = float(input("Enter the radius: "))
                h = float(input("Enter the height: "))
                v = float((1/3)*pie*(r**2)*h)
                nc = nc + 1
                print("The answer is",v,"\n\n                                                    Session --",nc,"                                 ")
            elif (shape == 4):
                pie = 3.14
                r = float(input("Enter the radius: "))
                h = float(input("Enter the height: "))
                v = float(pie*(r**2)*h)
                nc = nc + 1
                print("The answer is",v,"\n\n                                                    Session --",nc,"                                 ")
            elif (shape == 5):
                length = float(input("Enter the length: "))
                breadth = float(input("Enter the breadth: "))
                height = float(input("Enter the height: "))
                v = float(length*breadth*height)
                nc = nc + 1
                print("The answer is",v,"\n\n                                                    Session --",nc,"                                 ")
            elif (shape == 6):
                pie = 3.14
                r = float(input("Enter the radius: "))
                h = float(input("Enter the height: "))
                v = float(pie*(r**2)*h + (4/3)*pie*(r**3))
                nc = nc + 1
                print("The answer is",v,"\n\n                                                    Session --",nc,"                                 ")
        elif (op == 16):
            t = int(input("Enter your choice: \n1.Celsius --> Fahrenheit            3.Fahrenheit --> Celsius           5.Kelvin --> Celsius\n2.Celsius --> Kelvin                4.Fahrenheit --> Kelvin            6.Kelvin --> Fahrenheit\n\n----------------->"))
            if (t == 1):
                c = float(input("Enter the temperature: "))
                f = float(c*(9/5) + 32)
                nc = nc + 1
                print("The answer is",f,"°F\n\n                                                    Session --",nc,"                                 ")
            elif (t == 2):
                c = float(input("Enter the temperature: "))
                f = float(c + 273.15)
                nc = nc + 1
                print("The answer is",f,"K\n\n                                                    Session --",nc,"                                 ")
            elif (t == 3):
                c = float(input("Enter the temperature: "))
                f = float((c - 32)*5/9)
                nc = nc + 1
                print("The answer is",f,"°C\n\n                                                    Session --",nc,"                                 ")
            elif (t == 4):
                c = float(input("Enter the temperature: "))
                f = float(((c - 32)*5/9) + 273.15)
                nc = nc + 1
                print("The answer is",f,"K\n\n                                                    Session --",nc,"                                 ")
            elif (t == 5):
                c = float(input("Enter the temperature: "))
                f = float(c - 273.15)
                nc = nc + 1
                print("The answer is",f,"°C\n\n                                                    Session --",nc,"                                 ")
            elif (t == 6):
                c = float(input("Enter the temperature: "))
                f = float((c - 273.15) * (9/5) + 32)
                nc = nc + 1
                print("The answer is",f,"°F\n\n                                                    Session --",nc,"                                 ")
else:
    print(Fore.RED + "!!Wrong password!!")
print(Fore.WHITE + " ")
           
