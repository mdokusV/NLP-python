#!/usr/bin/env python
# -*- coding: utf8 -*-

# list of squares of natural numbers in [0,50]
squares = [x**2 for x in range(51)]
print(squares)


# cubes of natural numbers in [20,30]
cubes = [x**3 for x in range(20, 31)]
print(cubes)

# values of 3x-2 in [-5,5]
values = [3 * x - 2 for x in range(-5, 6)]
print(values)

# tuples (x,y), where x is in [10,20] and y is in [5,10]
numbers_X_numbers = [(x, y) for x in range(10, 21) for y in range(5, 11)]
print(numbers_X_numbers)


# tuples (x,y), where x is in [4,7] and y is in ["jabłko", "gruszka, "komputer"]
numbers_X_names = [
    (x, y) for x in range(4, 8) for y in ["jabłko ", "gruszka", "komputer"]
]
print(numbers_X_names)
