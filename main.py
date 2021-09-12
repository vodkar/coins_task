# -*- coding: utf-8 -*-

"""main loop"""

__author__ = "vodkar"

from coins_task import split_on_coins


def protected_int_input(to_print="") -> int:
    inp = input(to_print)
    while not str.isdigit(inp):
        print("Only digits!")
        inp = input(to_print)
    return int(inp)


if __name__ == "__main__":
    total = protected_int_input("Enter amount of return: ")
    total_coins = protected_int_input("Amount of type of coins: ")

    i = 0
    coins = []
    while i < total_coins:
        coin = protected_int_input(f"Amount of coin number {i + 1}: ")
        if coin in coins:
            print("Already exists!")
        else:
            coins.append(coin)
            i += 1

    print(split_on_coins(total, coins))
    input()
