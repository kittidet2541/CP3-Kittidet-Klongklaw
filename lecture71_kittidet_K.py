print("Welcome to OAT RESTUARANT")
listMenu=[]
listPrice=[]
while True:
    print("input (exit) after your order finish.")
    menuCook=input("name of menu:")

    if menuCook.lower() == "exit":
        break
    else:
        menuPrice=int(input("price of menu:"))
        listMenu.append(menuCook)
        listPrice.append(menuPrice)

print(listMenu)
print(listPrice)
def showBill():
    print("----My food----")
    for number in range(len(listMenu)):
        print(listMenu[number],"          ",listPrice[number])
    print("total price:","      ",sum(listPrice))

showBill()




