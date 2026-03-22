print("Hello from lesson 8")


# results = 1
# for count in range(1, 5+1):
#     ans = input("give me a number #" + str(count) + "?")
#     results = results * int(ans)
# print(results)

# import time
# for i in range(10, 0, -1):
#     print(i)
#     time.sleep(1)
# print(":3")

# import time
# ans = input("how long? ")
# ans = int(ans)
# for i in range(10, ans+1, -1):
#     print(i)
#     time.sleep(1)

# import random
# start = 1
# stop = 9999
# for count in range(20):
#     num = random.randint(start, stop)
#     print(num)


# isGirl = False
# print(isGirl)
# print(not isGirl)

# y = 50
# y = True
# x = 40
# x = True
# print(y == x)

# y = 50
# y = True
# x = 40
# x = False
# print(y == x)

# num1
# num2
# hidden_num
# reply

# import random
# num1 = random.randint(1, 50)
# num2 = random.randint(1, 50)
# question = "what is " + str(num1) + " + " + str(num2) + "?"
# hiddenNum = num1 + num2
# rely = input(question)
# reply = int(reply)
# print(reply == hiddenNum)

import random
num_questions = int(input("how many questions? "))
for count in range(num_questions):
    num1 = random.randint(1,6)
    num2 = random.randint(1,6)
    question = "what is " + str(num1) + " x " + str(num2) + "? "
    hidden_answer = num1 * num2
    user_answer = int(input(question))
    if hidden_answer == user_answer:
        print("correct")
    else:
        print("wrong")