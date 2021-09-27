#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    nb_print = 0
    for j in my_list[0:x]:
        num = my_list[j]
        try:
            nb_print += 1
            print("{:d}".format(num), end="")
        except Exception:
            continue
    print("")
    return nb_print
