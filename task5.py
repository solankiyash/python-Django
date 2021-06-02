# 1. Create a class cal1 that will calculate sum of three numbers. Create
# setdata() method which has three parameters that contain numbers.
# Create display() method that will calculate sum and display sum.

class cls():
	n1=""
	n2=""
	n3=""
	def setdata(self,n1,n2,n3):
		self.n1=n1
		self.n2=n2
		self.n3=n3
	def display(self):
		sum=self.n1+self.n2+self.n3
		print("sum of three num is",sum)
c=cls()
c.setdata(10,20,30)
c.display()

# 2. Create a class cal2 that will calculate area of a circle. Create setdata()
# method that should take radius from the user. Create area() method
# that will calculate area . Create display() method that will display area .

class cls():
	r=""
	def setdata(self):
		self.r=int(input("Enter the radius"))
	def display(self):
		area=3.1415*self.r*self.r
		print("sum of three num is",area)
c=cls()
c.setdata()
c.display()

# 3. Create a class cal3 that will calculate simple interest. Create
# constructor method which has three parameters .Create calInterest()
# method that will calculate Interest . Create display() method that will
# display Interest

class cls():
	r=""
	p=""
	n=""
	si=""
	def __init__(self,p,r,n):
		self.p=p
		self.r=r
		self.n=n
	def setdata(self):
		self.si = (self.p*self.r*self.n)/100
	def display(self):
		print("simple intrest is",self.si)
c=cls(2000,2,2)
c.setdata()
c.display()

# 4. Create a class cal4 that will calculate square of a number. Create
# setdata() method which has one parameters that contain number.
# Create display() method that will calculate sum.(Function should
# return value)

class cal4 ():
    a=""
    sqr=""
    def setdata4(self,a):
        self.a=a
    def display4(self):
        self.sqr=self.a*self.a
        print("squr of num is :",self.sqr) 
c1 = cal4()
c1.setdata4(50) 
c1.display4()


# 5. Consider an employee class, which contains fields such as name and
# designation. And a subclass, which contains a field salary. Write a
# program for inheriting this relation
class cal4 ():

    def emdetails(self):
        print("employee name:")
        print("employee designation:")

class emp(cal4):
    def salary(self):
        print("employee salary:")
e1=emp()
e1.emdetails()
e1.salary()


# 6. Create a class cal5 that will calculate area of a rectangle. Create
# constructor method which has two parameters .Create calArea()
# method that will calculate area of a rectangle. Create display() method
# that will display area of a rectangle.

class cal4():
    l=""
    b=""
    a=""
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def calarea(self):
        self.a=self.l*self.b
    def display(self):
        print("area of rect is :" ,self.a)
cl=cal4(35,45)
cl.calarea()
cl.display()            


# 7. Create a class cal6 that will calculate area of a square. Create setdata()
# method that should take length from the user. Create area() method
# that will calculate area . Create display() method that will display area .

class cal7():
    l=""
    a=""
    def calculate(self):
        self.l=int(input("enter the first number:"))
        self.a=self.l*self.l
    def area(self):
        print("area of square is:",self.a)
c1=cal7()
c1.calculate()
c1.area()


# 8. Write a program with use of inheritance: Define a class publisher that
# stores the name of the title. Derive two classes book and tape, which
# inherit publisher. Book class contains member data called page no and
# tape class contain time for playing. Define functions in the appropriate
# classes to get and print the details.

class publisher():
    t=''

    def title(self):
        self.t= input('Enter the name of the Title :')

class book(publisher):
    pnum=''

    def page(self):
        self.pnum= int(input('Enter the page number :'))

    def disp8(self):
        print('The title name is :',self.t)
        print('The page number is :',self.pnum)

class tape(publisher):
    time=''
    def timep(self):
        self.time= int(input('Enter time for playing :'))

    def disp8(self):
        print('The time for playing is :',self.time)


c8a=book()
c8a.title()
c8a.page()
c8b=tape()
c8b.timep()
c8a.disp8()
c8b.disp8()

# 9. Create a class called scheme with scheme_id,
# scheme_name,outgoing_rate, and message_charge. Derive customer
# class form scheme and include cust_id, name and mobile_no
# data.Define necessary functions to read and display data.

class scheme():
    scheme_id=104
    scheme_name='unlimited call'
    outgoing_rate=252
    message_charge=3

class customer(scheme):
    cust_id='yash41'
    name='solanki yash'
    mobile_no=1234567890

    def detail(self):
        print('customer name :',self.name)
        print('customer id :',self.cust_id)
        print('customer mobile number :',self.mobile_no)
        print('scheme id :',self.scheme_id)
        print('scheme name :',self.scheme_name)
        print('scheme outgoing rate :',self.outgoing_rate)
        print('scheme message rate :',self.message_charge)

c9=customer()
c9.detail()

# 10.Create a arith class. The class should have a parameterized constructor
# and methods to add, subtract and multiply two numbers and to return
# the answers.

class cal10():
    n1=''
    n2=''

    def __init__(self,num1,num2):
        self.n1=num1
        self.n2=num2

    def cal(self):
        add= self.n1 + self.n2
        sub= self.n1 - self.n2
        multi=self.n1 * self.n2

        print('addition is :',add)
        print('subtraction is :',sub)
        print('multiplication is :',multi)

c10=cal10(25,55)
c10.cal() 




