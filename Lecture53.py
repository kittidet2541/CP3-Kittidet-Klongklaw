def total_vat(total):
    totalvat=total+total*7/100
    return totalvat

total=int(input("total:"))
print(total_vat(total))