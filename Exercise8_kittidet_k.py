userName=input("username:")
password=input("password:")
if userName=="kittidet" and password=="klongklaw":
    print("OAT SUPERMARKET")
    print("--------------------------------")
    print("apple =10(THB)")
    print("orange=15(THB)")
    print("durian=60(THB)")
    print("rice=12(THB)")
    apple=10
    orange =15
    durian=60
    rice=12
    piece=int(input("apple piece:"))
    totalApple=apple*piece
    piece=int(input("orange piece:"))
    totalOrange=orange*piece
    piece = int(input("durian piece:"))
    totalDurian=durian*piece
    piece = int(input("rice piece:"))
    totalRice=rice*piece
    print("---------------------------------------------------------------")
    print("total",totalApple+totalOrange+totalDurian+totalDurian,"THB")
    print("---------------------------------------------------------------")
    print("thank you(OAT SUPERMARKET)")
else:
    print("not available please run again")





