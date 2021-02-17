import random


def isLucky():
    luck = True
    i = 0
    list2 = [1, 2, 3, 4, 5, 6]

    while luck is True:

        random_num = random.choice(list2)
        if i < 5:
            if random_num != 6:
                print("Rolling the dice... ", random_num)
                i += 1
                continue
            else:
                print("Rolling the dice... ", random_num)
                print("The student can graduate!""\n")
                luck = False
        else:
            print("The student cannot graduate!""\n")
            luck = False

