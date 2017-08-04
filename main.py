#!/usr/bin/env python3

import sys
import os
import operator

def main():
    if len(sys.argv) != 2:
        sys.exit("Enter directory as specified: ./main.py filename")

    filename = sys.argv[1]
    file_location = os.path.join(sys.path[0], filename)

    word_array = []
    flat_list = []
    # final_list = []
    word_quantity = {}

    with open(file_location) as file:
        for line in file:
            splitted_line = line.split(' ')
            word_array.append(splitted_line)
            #
            # for row in word_array:
            #     for element in row:
            #         flat_list.append(element)

        for row in word_array:
            for element in row:
                flat_list.append(element)

        for i in range (len(flat_list)):
            flat_list[i] = flat_list[i].strip()

    final_list = list(filter(lambda a: a != '', flat_list))

    for pick in final_list:
        if pick not in word_quantity:
            word_quantity[pick] = 1
            # print(word_quantity)
        else:
            word_quantity[pick] = word_quantity[pick] + 1
            # print(word_quantity)

    sorted_final_list = sorted(word_quantity.items(), key = operator.itemgetter(1))
    print(sorted_final_list)





if __name__ == '__main__':
    main()
