"""
File: class_reviews.py
Name: Charlie Chen
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""
def main():
    score_SC001,score_SC101,sum_SC001,sum_SC101,counter_SC001,counter_SC101 = None,None,0,0,0,0

    while True:
        switch = True
        class_name = str(input("Which class? "))
        # To check whether the class scores were entered
        if class_name == "-1" and (counter_SC001 == 0 and counter_SC101 == 0):
            print("No class scores were entered")
            switch = False
            break
        if class_name.upper() == "SC001":
            score_SC001 = int(input("Score: "))
            #calculate maximum value of SC001
            if counter_SC001 == 0:
                min_SC001, max_SC001 = score_SC001, score_SC001
            elif score_SC001 > max_SC001:
                max_SC001 = score_SC001
            elif min_SC001 > score_SC001:
                min_SC001 = score_SC001
            #calculate average of SC001
            counter_SC001 += 1
            sum_SC001+=score_SC001
        elif class_name.upper() == "SC101":
            score_SC101 = int(input("Score: "))
            #calculate maximum value of SC101
            if counter_SC101 == 0:
                min_SC101, max_SC101 = score_SC101, score_SC101
            elif score_SC101 > max_SC101:
                max_SC101 = score_SC101
            elif min_SC101 > score_SC101:
                 min_SC101 = score_SC101
            #calculate average of SC101
            counter_SC101 += 1
            sum_SC101 += score_SC101
        elif class_name == "-1":
            break
    if switch:
        print("============SC001===========")
        print(f"Max (001):{max_SC001} \nMin (001):{min_SC001} \nAvg (001): {sum_SC001/counter_SC001:f} " if score_SC001 else "No score for SC001")
        print("============SC101===========")
        print(f"Max (101):{max_SC101} \nMin (101):{min_SC101} \nAvg (101): {sum_SC101/counter_SC101:f} "if score_SC101 else "No score for SC101")

# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #
if __name__=="__main__":
    main()