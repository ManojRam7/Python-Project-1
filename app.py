num1=int(input("enter first number"))
num2=int(input("enter second number"))

sum=num1+num2
difference=num1-num2
product=num1*num2
quotient=num1/num2

print("Sum:", sum)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)


is_weekend=bool(input("is it weekend ? Enter True or False"))
is_holiday=bool(input("is holiday ? Enter True or False"))
is_homeworkleft=bool(input("is home work left ? Enter True or False"))

if is_weekend or is_holiday and not is_homeworkleft:
    print("Then go and do your home work idiot")
else:
    print("you can enjoy the holiday")
