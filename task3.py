#w.a.p to calculate five num average

num1 = int(input("Enter the  num1 :"))
num2 = int(input("Enter the  num2 :"))
num3 = int(input("Enter the  num3 :"))
num4= int(input("Enter the  num4 :"))
num5 = int(input("Enter the  num5 :"))
avg = (num1+num2+num3+num4+num5)/5
print('the Average of five number is:',avg)


#w.a.p to check whether num is odd or even

x=int(input("enter the first number:"))
if x%2==0:
    print("no is Even")
else:
    print("no is odd")


#w.a.p to check the year is leap year or not

year=int(input("enter the first number:"))
if year % 4 == 0:
	print("yes year is leap year")
else:
	print("no not a leap year")
 

#w.a.p to check the num is zero,pos or neg

no=int(input("enter the first number:"))
if no>0:
    print("no is positive")
elif no<0:
    print("no is negative")
else:
    print("no is zero")

#w.a.p to  take two num find greatest num and also check num is equal

x=int(input("enter the first number:"))
y=int(input("enter the first number:"))
if x>y:
   print(x,"is greatest")
elif x==y:
    print("no is equal")
else:
    print(y,"is greatest")

#w.a.p  to find a factorial of given num

x=int(input("enter the first number:"))
fact=1
while x>0:
	fact=x*fact
	x -= 1
print("factorial is",fact)

#w.a.p to swap two num using third variable

x=int(input("enter the x:"))
y=int(input("enter the y:"))
z = x
x =y
y = z
print("x is become",x)
print("y is become",y)

#w.a.p to take two num and find smallest num

x=int(input("enter the first number:"))
y=int(input("enter the first number:"))
if x>y:
   print(y," is smallest number")
else:
   print(x,"is smallest number")

#W.a.p to check the given num is less than 100 or not if it is than find num is odd or not

x=int(input("enter the first number:"))
if x<100:
  if x%2 == 0:
      print(" num is lessthan 100 or num is even")
  else:
      print("num is lessthan 100 or num is odd")
else:
        print("it is greater than 100")


#w.a.p to take a num and print square  of a num if it is less than 10
x=int(input("enter the number:"))
y=0
if x<10:
	y=x*x
	print(y)
else:
	print("Number is greater than 10")

#w.a.p to take a num and check whether it is zero,pos or neg using nested if...else statement

x=int(input("enter the number:"))
if x>=0:
	if x == 0:
		print("zero")
	else:
		print("Number is positive")
else:
	print("Number is negavtive")
    
#w.a.p  to take 3 num and find gretest num using nested if...else statement.

x=int(input("enter the number:"))
y=int(input("enter the number:"))
z=int(input("enter the number:"))
if x > y :
	if x > z:
		print(x, "is greter")
	else:
		print(z,"is greter")
else:
	print(y,"is greter")

#w.a.p to swap 2 num without  taking third variable.

x = int(input("enter the value"))
y = int(input("enter the value"))
print("Befrore swaping value of x and y")
print ("x is :",x,"y is",y)
x,y = y,x
print("After swaping value of x and y")
print ("x is :",x,"y is",y)

#w.a.p to  take  starting number and ending num from the user and print following series.

x = int(input("enter the value"))
print ("number is",x)
while x>=0:
	print (x)
	x -= 3