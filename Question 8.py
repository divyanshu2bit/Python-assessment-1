# Program to create a dictionary of odd numbers and their cubes using dictionary comprehension

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

odd_cubes = {n: n**3 for n in numbers if n % 2 != 0}

print(odd_cubes)
