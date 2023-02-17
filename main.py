def vatCalculate(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result
Price = int(input("Price: "))
print(vatCalculate(Price), "THB")