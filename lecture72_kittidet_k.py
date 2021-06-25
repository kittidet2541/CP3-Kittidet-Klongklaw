print("Welcome to OAT RESTUARANT")
listMenu=[]

while True:
    print("input (exit) after your order finish.")
    menuCook=input("name of menu:")

    if menuCook.lower() == "exit":
        break
    else:
        menuPrice=int(input("price of menu:"))
        listMenu.append([menuCook,menuPrice])


print(listMenu)

def showBill():
    totalPrice=0
    print("-------My food-------")
    for number in range(len(listMenu)):
        totalPrice+=(listMenu[number][1])
        print(listMenu[number][0],"                  ",listMenu[number][1],"BATH")
    print("total price","          ",totalPrice,"BATH")



showBill()






