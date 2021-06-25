def showBill():#บิลคิดเงิน
    totalPrice=0
    print("-------My food-------")
    for number in range(len(listMenu)):
        totalPrice+=(listMenu[number][1])
        print(listMenu[number][0],"                  ",listMenu[number][1],"BATH")

    print("total price","          ",totalPrice,"BATH")

menuPrice= {"กระเพราหมูสับ":50,"ข้าวผัดหมู":45,"ก๋วยเตี๋ยวหมู":40,"น้ำเปล่า":10}#ราคาขออาหาร

print("Welcome to OAT RESTUARANT")
listMenu=[]

while True:
    print("input (exit) after your order finish.")
    menuCook=input("name of menu:")

    if menuCook.lower() == "exit":
        break
    else:

        listMenu.append([menuCook,menuPrice[menuCook]])


print(listMenu)




showBill()






