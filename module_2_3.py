my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]    #1
n = -1
while n <= len(my_list):
    n += 1
    if my_list[n] < 0:
        break
    elif my_list[n] == 0:
        continue
    print(my_list[n])





