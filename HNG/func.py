from math import sqrt
import requests

"""
    takes an integer variable num 
    checks if num is a prime number
    return True if the number is a prime number and False on otherwise
"""
def is_prime_num(num):
    if num < 2:
        return "false"
    for i in range(2, int(sqrt(num)) + 1):
        if (num % i == 0):
            return "false"
    return "true"


"""
    takes an integer variable num 
    checks if num is a prime number
    return "even" if the number is an even number and otherwise, "odd"
"""
def is_even_or_odd(num):
    return "even" if(num % 2 == 0) else "odd"

"""
    takes an integer variable num 
    checks if num is a prime number
    return "armstrong" if the number is an armstrong and otherwise, "Not armstrong"
"""
def is_armstrong(num):
    if num < 0:
        return "Not armstrong"

    # convert the int num to string
    str_num = str(num)

    # the len of the str_num is the power
    power = len(str_num)

    # using list comprehension loop through the str_num 
    arm = sum(int(dig) ** power for dig in str_num)

    return "armstrong" if num == arm  else "Not Armstrong"

"""
    takes an integer variable num 
    checks if num is a prime number
    return "true" if the number is a perfect number and otherwise, "false"
"""
def is_perfect(num):
    if num < 0:
        return "false"
    divisor_sum = sum(dig for dig in range(1, num // 2 + 1) if num % dig == 0 )
    return "true" if num == divisor_sum else "false"

"""
    sums the digits of a number and returns the sum
"""
def digit_sum(num):
    if num < 0:
        num = num * -1
    return sum(int(dig) for dig in str(num))


"""
    returns a string concerning an int
    the string is gotten from numbersapi.com
"""
def fun_fact(num):
    url = f"http://numbersapi.com/{num}/math"
    
    try:
        res = requests.get(url, timeout=10)  # Set a timeout to avoid long waits
        if res.status_code != 200:
            return 500
        return res.text
    except requests.exceptions.RequestException:
        return 500  # Return 500 for any network-related error