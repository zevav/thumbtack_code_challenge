from __future__ import division
import sys
from collections import defaultdict

""" write a program that takes in four numbers and determines the \
mathematical expression that can combine the first three numbers, \
through addition, subtraction, multiplication, and division, to  \
get the fourth.

e.g. echo '1 2 3 5' | python challenge.py
$ 3 + 2 * 1

e.g. echo '1 1 1 6' | python challenge.py
$ 4 / 6 * 3

"""

operators = ["*", "/", "+", "-"]


def split_input(arg):
    """splits input by spaces"""
    the_nums = arg.readline().rstrip().split(" ")
    return the_nums


def validate_input(arg):
    """tests whether the arg is an integer; quits if not"""
    if "." in arg or any([l.isalpha() for l in arg]):
        print "only integers, please."
        return sys.exit()
    else:
        arg = int(arg)
    return arg


def split_into_three_and_one(a_list_of_numbers):
    first_three = []
    for i in range(3):
        first_three.append(a_list_of_numbers[i])
    should_equal = int(a_list_of_numbers[3])
    return first_three, should_equal


def do_math_on_two_numbers(first_number, second_number, operator):
    first_number = int(first_number)
    second_number = int(second_number)
    if operator == "+":
        return sum([first_number, second_number])
    if operator == "-":
        return first_number - second_number
    if operator == "*":
        return first_number * second_number
    if operator == "/":
        return first_number / second_number


def do_each_possible_math_operation(first_number, second_number):
    the_total = defaultdict(str)
    for operator in operators:
        the_total[operator] = do_math_on_two_numbers(first_number,
                                                     second_number, operator)
    return the_total


def test_if_first_three_equals_four(list_of_nums, should_equal):
    for i in range(len(list_of_nums)):
        totals = do_each_possible_math_operation(list_of_nums[i],
                                                 list_of_nums[i-1])
        for first_operator, first_total in totals.iteritems():
            for second_operator, second_total in \
                do_each_possible_math_operation(first_total,
                                                list_of_nums[i-2]).iteritems():
                if second_total == should_equal:
                    return list_of_nums[i], first_operator, list_of_nums[i-1], \
                        second_operator, list_of_nums[i-2]

if __name__ == "__main__":
    the_nums = split_input(sys.stdin)
    for num in the_nums:
        validate_input(num)
    first_three, should_equal = split_into_three_and_one(the_nums)
    initial_results = test_if_first_three_equals_four(first_three,
                                                      should_equal)
    try:
        first, first_op, second, second_op, third = initial_results
    except:
        print "Invalid."
        sys.exit()
    print first, first_op, second, second_op, third
