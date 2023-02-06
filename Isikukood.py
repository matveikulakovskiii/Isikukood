from module1 import *
ikood=""
arvud=[]
ikoodid=[]

x=True
while not x:
       print("Работает")
else:
       print("Не работает")


print()
while True:
    a=input("tahad jätkata? yes=y/no=n: ")
    if a=="y" or a=="yes":
        ikood=input("Sisesta isikukood: ")
        if pikkus(ikood)==False:
            print("lIIGA PIKK VÕI LÜHIKE ISIKUKOOD")
            arvud.append(ikood)
        else:
            print("11 sümbolid")
            s=esnu(ikood)
            if s=="viga":
                print("Esimene sümbol ei ole õige")
                arvud.append(ikood)
            else:
                print(s)
                if sünnipäev(ikood)=="viga":
                    print("2-7 tähet on valesti sisestatud")
                else:
                    print(lause(ikood))
                    if kontrollnr(ikood)==int(ikood[-1]):
                        print("Ok")
                        ikoodid.append(ikood)
                    else:
                        print("!!!")
    else:
        ikoodid=naised_mehed(ikoodid)
        print(ikoodid)
        arvud=arvud_sorted(arvud)
        print(arvud)
        break

