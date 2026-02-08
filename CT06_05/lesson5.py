print("Hello from lesson 5")

# age = input("what is your age?")
# name = input("what is your name?")
# msg = input("what is your message?")
# print("Happy ", age, "th Birthday,", name, ".", msg)

# for count in range(100):
#     print("i like chicken rice")
#     print(count)

# print("i am out of the loop")

# for count in range(100):
#     print("i like cake")
#     print("gimme more")
#     print(count)

# print("i am out of the loop")

# myword = "gay"
# for letter in myword:
#     print("give me a ", letter)

# print("XunYuan is", myword)


# for count in range(60):
#     print(count)


# for count in range(1, 6, 1):
#     print(count)

# for count in range(51, 100, 1):
#     print(count)



# for count in range(18, 30, 1):
#     print(count)


# for count in range(2, 25, 2):
#     print(count)

# for count in range(8, 97, 8):
#     print(count)

# for count in range(5, 0, -1):
#     print(count)


# print("ready!")
# for count in range(3, 0, -1):
#      print(count)

# for count in range(10, 0, -1):
#      print(count)
# print("boo!")


# Using input(), ask the user for 2 numbers and store them in the
# variables:
# 1. start
# 2. stop

# Write a 'for' loop to count from **start** to **stop**

# Note:
# What happens if the user inputs a higher start number than stop?
# Modify your code to be able to handle that scenario.

n1 = input("give me a number: ")
n1 = int(n1) #convert
n2 = input("give me another number: ")
n2 = int(n2) #convert

if n1 > n2: 
    start = n2
    stop = n1
else:
    start = n1
    stop = n2

for count in range(start, stop):
    print(count)