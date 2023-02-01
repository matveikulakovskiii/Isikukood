from module1 import *
ikood=""
while True:
    ikood=input("Sisesta isikukood: ")
    if pikkus(ikood)==False:
        print("lIIGA PIKK VÕI LÜHIKE ISIKUKOOD")
    else:
        print("11 sümbolid")
        s=esnu(ikood)
        if s=="viga":
            print("Esimene sümbol ei ole õige")
        else:
            print(s)
            if sünnipäev(ikood)=="viga":
                print("2-7 tähet on valesti sisestatud")
            else:
                print(lause(ikood))