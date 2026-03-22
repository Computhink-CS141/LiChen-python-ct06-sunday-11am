print("Hello from lesson 9")

# import random
# num1 = random.randint(1,6)
# num2 = random.randint(1,6)
# num3 = random.randint(1,6)
# print("1st number: " , str(num1))
# print("2nd number: " , str(num2))
# print("3rd number: " , str(num3))
# all_even_odd = (num1%2==0) == (num2%2==0) == (num3%2==0)
# print("all numbers are even/odd: " , all_even_odd)

numApple = int(input("how many apples? "))
numOrange = int(input("how many oranges? "))
if numApple > 5:
    costApple = numApple * 0.6 * 0.9
else:
    costApple = numApple * 0.6
if numOrange > 5:
    costOrange = numOrange * 0.9 * 0.9
else:
    costOrange = numOrange * 0.9