# PROJECT: Project 3 for CS/CYCS1110
# AUTHOR: Cameron Brenberger
# DESCRIPTION: This Generates if a student can graduate high school.
#           Input 5 student grades (0-100) in Math, English, Physics, History, and Biology:
#              - Average of grades should be more of equal to 85.
#              - Lowest grade should be more or equal to 75.
#              - Highest grade should not be more than 20 points higher than the lowest grade.
#              - If condition 3 is not met, the student should be lucky. The program is given
#                5 chances to roll a dice with 6 surfaces with values from 1 to 6. If out of the 5
#                chances, the program never hits 6, the student cannot graduate.
#           The program will then ask, "Do you want to continue?", to put other student grades in (Y or N).

from luckyModule import isLucky


def main():
    print("Enter Student's Grade (0-100) : ""\n")

    ask = False

    while True:
        grad_m = int(input("Maths: "))

        if grad_m in range(0, 101):
            break
        else:
            print("Invalid Grade.")
            continue

    while True:
        grad_e = int(input("English: "))

        if grad_e in range(0, 101):
            break
        else:
            print("Invalid Grade.")
            continue

    while True:
        grad_p = int(input("Physics: "))

        if grad_p in range(0, 101):
            break
        else:
            print("Invalid Grade.")
            continue

    while True:
        grad_h = int(input("History: "))

        if grad_h in range(0, 101):
            break
        else:
            print("Invalid Grade.")
            continue

    while True:
        grad_b = int(input("Biology: "))
        print("\t")

        if grad_b in range(0, 101):
            break
        else:
            print("Invalid Grade.")
            continue

    total = (grad_m + grad_e + grad_p + grad_h + grad_b)
    list1 = [grad_m, grad_e, grad_p, grad_h, grad_b]
    minG = minGrade(list1)
    maxG = maxGrade(list1)
    avg = averageGrade(total)
    evaluate(minG, maxG, avg)

def minGrade(list1):

    minG = min(list1)
    return minG


def maxGrade(list1):

    maxG = max(list1)
    return maxG


def averageGrade(total):

    avg = total // 5
    return avg


def evaluate(minG, maxG, avg):

    con = minG + 20

    if avg >= 85 and minG >= 75:
        if maxG > con:
            isLucky()
        else:
            print("The student can graduate!""\n")
    else:
        print("The student cannot graduate!""\n")

    ask = True
    multi(ask)


def multi(ask):

    if ask is True:
        ans = input("Do you want to continue? ").strip()
        print("\t")
        ans1 = ans[0]
        ans_up = ans1.upper()

        if ans_up == "Y":
            main()
        else:
            exit()


main()
