"""
File: coin_flip_runs.py
Name: Charlie Chen
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
    print("Let's flip a coin")
    run = input("Number of runs: ")
    coin_result = "##"
    counter = 1
    # To use string splicing method to check the previous flip result
    while counter <= int(run):
        coin = r.randint(0, 1)
        if coin == 0:
            if coin_result[-1] == "H" and coin_result[-2] != "H":
                counter += 1
            coin_result += "H"
        else:
            if coin_result[-1] == "T" and coin_result[-2] != "T":
                counter += 1
            coin_result += "T"
    print(coin_result[2:])


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
    main()
