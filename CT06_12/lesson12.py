print("Hello from lesson 12")

# game_status = "paused" #active/paused
# if game_status  == "active" or not (game_status == "paused"):
#     print("game in progress")
# else:
#     print("game is paused")

# visitors = 4
# while visitors < 25:
#     visitors += 1
#     print(visitors)

# counter = 1
# while True:
#     print(counter)
#     if counter == 30:
#         break
#     counter = counter + 1

# final_order = ""
# reply = input("enter order ")
# while not (reply == "end"):
#     if reply == "end":
#         break
#     final_order = final_order + ", " + reply
#     reply = input("enter order")
# print("your order is", final_order)

count = 10
while count > 0:
    print(count)
    count = count - 1
    if count == 5:
        break
else:
    print("happy new year!")