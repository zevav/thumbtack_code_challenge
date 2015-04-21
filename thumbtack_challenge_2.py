from __future__ import division
import sys
from collections import defaultdict

""" write a program that takes in an indeterminate number of 
numbers and determines the mathematical expression that can 
combine all but the last number through addition, subtraction,
multiplication, and division, to output the last number.
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


def split_into_first_nums_and_one(a_list_of_numbers):
    """splits inputs into a list of numbers and the number
    they need to combine to output."""
    first_nums = []
    for i in range(len(a_list_of_numbers)-1):
        first_nums.append(a_list_of_numbers[i])
    should_equal = int(a_list_of_numbers[-1])
    return first_nums, should_equal


def do_math_on_two_numbers(first_number, second_number, operator):
    """takes two numbers and an operator, then returns the calculated output"""
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
        the_total[operator] = do_math_on_two_numbers(first_number, second_number, operator) 
    return the_total


def do_each_possible_combination_of_operators(list_of_nums):
    """this currently creates a list of dictionaries, each with the results of 
    applying this or that operator to two consecutive numbers from the list.  it needs
    to instead combine the result of the previous two numbers with the next number
    and each of the operators.  there will be a dictionary for each step factorial four (?):
    one for each operator.
    """
    the_steps = []
    for i in range(len(list_of_nums)-1):
        the_steps.append(do_each_possible_math_operation(list_of_nums[i], list_of_nums[i+1]))
    return the_steps

def test_if_first_numbers_equal_four(list_of_nums, should_equal):
    for i in range(len(list_of_nums)):
        totals = do_each_possible_math_operation(list_of_nums[i], list_of_nums[i-1])
        for first_operator, first_total in totals.iteritems():
            print first_operator, first_total
            for second_operator, second_total in do_each_possible_math_operation(first_total, list_of_nums[i-2]).iteritems():
                if second_total == should_equal:
                    return list_of_nums[i], first_operator, list_of_nums[i-1], second_operator, list_of_nums[i-2]
    

if __name__ == "__main__":
    the_nums = split_input(sys.stdin)
    for num in the_nums:
        validate_input(num)
    first_nums, should_equal = split_into_first_nums_and_one(the_nums)
    the_steps = do_each_possible_combination_of_operators(first_nums) 
    print the_steps
 
#    initial_results = test_if_first_numbers_equal_four(first_nums, should_equal) 
#    try:
#        first, first_op, second, second_op, third = initial_results
#    except:
#        print "Invalid."
#        sys.exit()
#    print first, first_op, second, second_op, third
