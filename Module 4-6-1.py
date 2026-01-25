# Module 4-6

import random

number_of_points= int(input("Please enter the number of random points  you want to generate:"))

points_circle = 0
points_total = 0

while points_total < number_of_points:
    x= random.uniform(-1,1)
    y= random.uniform(-1,1)


    if x ** 2 + y ** 2 < 1:
        points_circle = points_circle + 1

    points_total = points_total + 1

pi_approximation= 4 * points_circle / points_total
print(f"Pi is approximately {pi_approximation}, by generating {number_of_points} random points.")




