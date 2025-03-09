import keyword


print ("Calculator")
num1 = int (input ("Number 1:"))
num2 = int (input ("Number 2:"))
print ("Add:", num1 + num2, "Subtract:", num1-num2, "Multiply:", num1 * num2, "Divide:", num1 / num2, "Power:", num1 ** num2, "Remainder:", num1 % num2)
print ("Python Keywords:")
print (keyword.kwlist)