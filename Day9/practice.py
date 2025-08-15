# even check function with if-else
def even_check(num):
    if num % 2 == 0:
        return "EVEN"
    else:
        return "ODD"
print(even_check(21))

# another way even check function with return statement
def even_check(num):
    return num % 2 == 0
print(even_check(21))

# returning TRUE if any of the number in the list is even
def any_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            return True
    return False # this return False statement is intended under the for loop so that it only returns False if no even number is found
print(any_even([1, 3, 5, 7, 8]))

# another way to check if any number in the list is even
def any_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            return True
        else:
            pass

# if any even number is found append it to a list
def any_even(numbers):
    even_list = []
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num) 
        else:
            pass
    return even_list  # return the list of even numbers found
print(any_even([1, 2, 3, 4, 5, 6]))

# checking prime numbers optimized 
def is_prime(num):
    if num <= 1:
        return False
    for n in range(2,int(num**0.5)+1):
        if num % n == 0:
            return False
    return True
print(is_prime(29))