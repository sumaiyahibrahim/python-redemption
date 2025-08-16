"""Create a function lesser(a, b) that:
- If both a and b are even → return the lesser number.
- If one or both are odd → return the greater number."""
def lesser(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)
    
"""Takes a two-word string
- Returns True if both words start with the same letter (case-insensitive)
- Otherwise, returns False"""
def animal_crackers(text):
    words = text.lower().split()  # split into words + ignore case
    return words[0][0] == words[1][0]

# Examples:
print(animal_crackers('Levelheaded Llama'))   # ➤ True
print(animal_crackers('crazy Kangaroo'))      # ➤ False

"""We’re given two integers, and we need to return:
- True if:
- Either of the numbers is 20
- The sum of both is 20
- False otherwise."""
def makes_twenty(n1, n2):
    return n1 == 20 or n2 == 20 or (n1 + n2) == 20

"""Capitalize the first and fourth letters of a given name."""
def old_macdonald(name):
    if len(name) < 4:
        return "Name too short!"
    
    first = name[0].upper()
    middle = name[1:3]
    fourth = name[3].upper()
    rest = name[4:]
    
    return first + middle + fourth + rest

"""Take a sentence and flip the word order like Master Yoda speaks
- If the sentence is "I am a programmer" → return "programmer a am I"."""
def master_yoda(sentence):
    words = sentence.split()       # ['I', 'am', 'home']
    reversed_words = words[::-1]   # ['home', 'am', 'I']
    return ' '.join(reversed_words) # Join back into a sentence

"""Find 33:
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
"""
def find_three(*num):
    for i in range(0,len(num)-1):
        if num[i] == 3 and num[i+1]==3:
            return True
    return False
print(find_three(2,3,3,5))

""" PAPER DOLL : Given a string, return a string where for every character in the original, there are three characters.
"""
def paper_doll(string):
    result = ''
    for char in string:
        result += char*3
    return result
print(paper_doll("Sumaiyah"))

"""BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
   If their sum exceeds 21 and there is an 11, subtract 10 from the sum. If the sum exceeds 21 and there is no 11, return 'BUST'."""
def blackjack(a,b,c):
    total = a+b+c
    if total <= 21:
        return total
    elif 11 in [a,b,c] and total <= 31:
        return total - 10
    elif total > 21:
        return "BUST"
print(blackjack(10, 11, 2))  

"""SUMMER OF '69: Return the sum of the numbers in the array, 
except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9).
return 0 if there are no numbers."""
def summer_69(arr):
    total = 0           
    add = True          
    for num in arr:     
        if add:         
            if num == 6:    
                add = False
            else:
                total += num  
        else:           
            if num == 9:     
                add = True
    return total

"""SPY GAME: Write a function that takes a list of integers and returns True if it contains a 007 sequence."""
def spy_game(nums):
    code = [0,0,7,'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code)==1
print(spy_game([1,2,3,0,0,7,3]))

"""COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number."""
def count_primes(n):
    is_prime = [True] * (n+1)       
    is_prime[0] = is_prime[1] = False  
    
    for i in range(2, int(n**0.5)+1):  
        if is_prime[i]:               
            for j in range(i*i, n+1, i):  
                is_prime[j] = False       
    
    return [i for i in range(2, n+1) if is_prime[i]]  
  
print(count_primes(10))  # ➤ 4 (2, 3, 5, 7)

####################################################################

"""Volume of a Sphere: Given the radius, return the volume of a sphere with that radius."""
def vol(rad):
    result = (4/3) * 3.14 * (rad**3)
    return result
print(vol(2))  # 33.49333333333333


"""Write a function that checks whether a number is in a given range (inclusive of high and low)."""
def ran_check(num, low, high):
    return num in range(low, high + 1)
print(ran_check(5, 1, 10))


"""Write a python function that accepts a string and calculates the number of uppercase letters and lowercase letters."""
def up_low(string):
    d = {'upper': 0, 'lower': 0}
    for letter in string:
        if letter.isupper():
            d['upper'] += 1
        elif letter.islower():
            d['lower'] += 1
        else:
            pass
    print(f"Original String: {string}")
    print(f"Lower count: {d['lower']}")
    print(f"Upper count: {d['upper']}")

# Example
up_low("Hello World!")


"""Write a function that takes a list and returns a new list with unique elements of the first list."""
def unique_list(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique
print(unique_list([1, 2, 3, 1, 2, 4]))  # [1, 2, 3, 4]

# another way using set
def unique_list(*unfiltered):
    result = set(unfiltered)
    print("unique elements:", *result)

unique_list(1, 2, 3, 5, 3, 2, 1)

"""Write a python function to multiply all the numbers in a list."""
def multiply(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result
print(multiply([1, 2, 3, 4]))  # 24

"""Write a function that checks whether a word or phrase is a palindrome."""
def palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
print(palindrome("sumaiyah"))  # False
print(palindrome("madam"))  # True

"""Write a python function to check whether a string is pangram or not."""
def is_pangram(s):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return set(s.lower()) >= alphabet
print(is_pangram("The quick brown fox jumps over the lazy dog"))  # True