from module1 import*
while True:
    print("Funktsioonid".center(50,"+"))
    v=input("arithmetic- A; \nis_year_leap- Y; \nsquare- S; \neason- D; \nbank- B  \nis_prime- F \ndate- G \nxor_cipher- K")
    if v.upper()=="A":
        a=float(input("Arv 1: "))
        b=float(input("Arv 2: "))
        c=input("Tehe: ")
        result=arithmetic(a,b,c)
        print(result)
    elif v.upper()=="Y":
        year=int(input("Sisesta aasta: "))
        result=is_year_leap(year)
        print(result)
    elif v.upper()=="S":
        kv=int(input("Sisesta ruudu külg: "))
        result=square(kv)
        print(result)
    elif v.upper()=="D":
        kuu=int(input("Sisesta kuu numbrid: "))
        result=season(kuu)
        print(result)
    elif v.upper()=="B":
        a=float(input("Sisesta deposiidi number: "))
        years=int(input("Kui palju aastat on möödas?"))
        result=bank(a,years)
        print(result)
    elif v.upper()=="F":
        a=int(input("Sisesta number: "))
        result=is_prime(a)
        print(result)
    elif v.upper()=="K":
        print("Kodeerimine".center(60,"*"))
        result=xor_cipher(input("Sisesta tekst"), input("Sisesta võti :"))
        print(result)
        print("Dekodeerimine". center(60,"*"))
        de_rezult=xor_uncipher(result, input("Sisesta võti:"))
        print(de_rezult)
    elif v.upper()=="G":
        day=int(input("Sisesta päev: "))
        month=int(input("Sisesta kuu: "))
        year=int(input("Sisesta aasta: "))
        result=date(day,month,year)
        print(result)