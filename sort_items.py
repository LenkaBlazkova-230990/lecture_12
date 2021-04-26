import csv
import os
import random

cwd_path = os.getcwd()


def read_row(file_name):
    """
    Reads one row for a CSV file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (list, int),
    """
    path = os.path.join(cwd_path, file_name)
    with open(path, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter="\t")

        for line in reader:
            row = [int(number) for number in line]

    return row


def read_rows(file_name, row_number):
    """
    Reads selected row for a CSV file and returns selected numeric data.

    :param file_name: (str), name of CSV file
    :param row_number: (int), number of selected row
    :return: (list, int),
    """
    path = os.path.join(cwd_path, file_name)
    with open(path, 'r') as csv_file:
        reader = csv.reader(csv_file)

        for line_idx, line in enumerate(reader):
            if line_idx == row_number:
                row = [int(number) for number in line]

    return row

def selection_sort(number_array, direction="ascending"):
    """
    Sorts and returns selected numeric data with Selection Sort.

    :param number_array: (list,int), list with numeric array
    :return: (list, int), sorted numeric array
    """
    # hlavni cyklus prochazeni sekvence - v prvni iteraci ukazuji na prvni prvek
    for position, _ in enumerate(number_array):
        extreme_idx = position
        for idx_number, number in enumerate(number_array[position + 1:]):
            if direction == "ascending":
                if number < number_array[extreme_idx]:                          # zmena zanmenka na '>' = opacne serazeni
                    extreme_idx = idx_number + position + 1
            elif direction == "descending":
                if number > number_array[extreme_idx]:
                    extreme_idx = idx_number + position + 1

        number_array[position], number_array[extreme_idx] = number_array[extreme_idx], number_array[position]

    return number_array


def bubble_sort(number_array):
    """
    Sorts and returns selected numeric data with Bubble Sort.

    :param number_array: (list,int), list with numeric array
    :return: (list, int), sorted numeric array
    """



def main():
    """This is the driver function"""

    # # Nacitani dat 1
    # file_name_1 = "numbers_one.csv"
    # row_of_numbers = read_row(file_name_1)
    # print(row_of_numbers)

    # Ukol: Selection Sort
    # ordered_list_1 = selection_sort(row_of_numbers, "ascending")
    # print(ordered_list_1)

    # Ukol: Selection Sort - se smerem razeni
    # -''-

    # --------------------------------------------------------
    # # Nacitani dat 2
    file_name_2 = "numbers_two.csv"
    row_number = 0
    one_row_of_numbers = read_rows(file_name_2, row_number)
    # print(one_row_of_numbers)

    # Ukol: Bubble Sort
    ordered_list_2 = bubble_sort(one_row_of_numbers)
    print(ordered_list_2)

    # příklad výpisu hodnot seřazené řady
    # print ("Seřazená řada čísel je:")
    # for i in range(len(number_array)):
    #	print ("%d" %number_array[i]),


if __name__ == '__main__':
    main()
