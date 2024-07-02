#!/usr/bin/env python3

def happy_new_year():
        # code goes here!
    count = 10
    while count > 0:
        print(count)
        count -= 1
    print("Happy New Year!")
    pass

def square_integers(int_list):
    # code goes here!
    if int_list is None:
        return None
    squared_nums = [num ** 2 for num in int_list]
    return squared_nums

    pass

def fizzbuzz():
        # code goes here!
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
    pass
