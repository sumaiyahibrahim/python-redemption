# Tuple Unpacking practice with a function
work_hours = [('Sumaiyah', 100), ('Ali', 110), ('Zara', 90)]
def emp_of_month(work_hours):
    current_max = 0
    emp_of_month=''
    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            emp_of_month = employee
    return (emp_of_month,current_max)
employee, hours = emp_of_month(work_hours)
print(f"Employee of the Month: {employee}")
print(f"Hours Worked: {hours}")

#1: print Hello World
def sayHello():
    print("Hello World")
sayHello()

#2: print Hello Name
def sayHelloName(name):
    print(f"Hello {name}")
sayHelloName("Sumaiyah")

#3 - simple Boolean
def booleanCheck(x):
    if x == True:
        return "Hello"
    else:
        return "Good Bye"
print(booleanCheck(True))

#4 - using Booleans
def myfunc(x,y,z):
    if z == True:
       return x
    else:
       return y

myfunc('Hello','Goodbye',True)
# Returning 'Hello' if z is True, otherwise return 'Goodbye'
    
#5: simple math
def myfunc(a,b):
    return a+b
print(myfunc(12,13))

#6: is even
def isEven(x):
    if x % 2 == 0:
        return True
    else:
        pass
print(isEven(2))

#7: is greater
def is_greater(x,y):
    return x>y
print(is_greater(10,5))

#8: *args
def myfunc(*args):
    return sum(args)

#9: pick evens
def appendEven(*args):
    even_list = []
    for num in args:
        if num % 2 == 0:
            even_list.append(num)  
    return even_list
print(appendEven(1, 2, 3, 4, 5, 6, 7, 8, 9))

#10: skyline
def skyline(string):
    mylist = []
    for i in range(len(string)):
        if i % 2 == 0:
            mylist.append(string[i].upper())
        else:
            mylist.append(string[i].lower())
    return ''.join(mylist)

print(skyline("AnthrophobiahjgFGSkjhdHDSk"))
#--------- another way to do skyline ---------#
def skyline(string):
    list = []
    for index,letter in enumerate(string):
        if index % 2 == 0:
            list.append(letter.upper())
        else:
            list.append(letter.lower())
    return ''.join(list)
print(skyline("AnthrophobiahjgFGSkjhdHDSk"))

