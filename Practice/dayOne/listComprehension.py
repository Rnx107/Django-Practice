# https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

# --- General List Comprehension (Standard Loop) ---
squares = []
for num in range(10):
    squares.append(num**2)

print("Standard loop squares:", squares)


# --- Using List Comprehension ---
# Note: The notebook comment mentioned lambda, but this is a standard list comprehension
squares_comp = [x**2 for x in range(10)]
print("List comprehension squares:", squares_comp)


# --- Using list comprehension for complex list operations ---
comp = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print("Filtered combinations:", comp)


# --- Filtering and squaring a vector ---
vec = [-4, -2, 0, 2, 4]
vec_pos = [x**2 for x in vec if x**2 >= 0]
print("Squared vector:", vec_pos)


# --- Creating tuples ---
values = [(x, x**2) for x in range(5)]
print("Tuples (x, x^2):", values)


# --- List comprehension with imports ---
from math import pi
math_list = [str(round(pi, i)) for i in range(1, 6)]
print("Pi rounded at various precisions:", math_list)