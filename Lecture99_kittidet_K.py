from  tkinter import*
def leftClickButton(event):
    BMI=int(textBoxWeight.get())/(int((textBoxHight.get()))/100)**2
    if BMI<=18.5:
        labelBMI.configure(text="ต่ำกว่าเกณฑ์")
    elif BMI<=24.9:
        labelBMI.configure(text="ปกติ")
    elif BMI <= 29.9:
        labelBMI.configure(text="อ้วน")
    elif BMI >= 29.9:
        labelBMI.configure(text="เกินพิกัด")
MainWindow=Tk()
lableHight=Label(MainWindow,text="ส่วนสูง (cm.)")
lableHight.grid(row=0,column=0)
textBoxHight=Entry(MainWindow)
textBoxHight.grid(row=0,column=1)
lableWeight=Label(MainWindow,text="น้ำหนัก (kg.)")
lableWeight.grid(row=1,column=0)
textBoxWeight=Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
CalculateButton=Button(MainWindow,text="คำนวณ")
CalculateButton.grid(row=2)
CalculateButton.bind('<Button-1>',leftClickButton)
labelBMI=Label(MainWindow,text="ค่าBMI")
labelBMI.grid(row=2,column=1)

MainWindow.mainloop()
