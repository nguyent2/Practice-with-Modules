/Learn more or give us feedback
######################################################################
# Author: Thy H. Nguyen
# TODO: Change this to your names
# Username: nguyent2
# TODO: Change this to your usernames
#
# Assignment: A06: It's in your Genes
#
# Purpose: A test suite for testing the a06_genes.py program
#
######################################################################
# Acknowledgements:
#   Original Author: Dr. Jan Pearce
#
#   Idea from: http://www.cs.uni.edu/~schafer/1140/assignments/pa9/index.htm
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################
import sys

from t12_dots import *
# You may get red squiggly lines from PyCharm; it'll be okay though.
# To remove them, right click the folder where this file is located, and select
# "Mark directory as" and then "Sources Root"


def testit(did_pass):
    """
    Print the result of a unit test.
    :param did_pass: a boolean representing the test
    :return: None
    """
    # This function works correctly--it is verbatim from the text

    linenum = sys._getframe(1).f_lineno         # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def dots_test_suite():
    """
    The dots_test_suite() is designed to test the following:
      calculate_size(num_dots)
      is_valid_size(dot_width, dot_height, distance, screen_width, screen_height)
    :return: None
    """

    # The following tests test the calculate_size() function
    print("\nTesting calculate_size")
    testit(calculate_size(25) == (5,5))
    testit(calculate_size(36) == (6,6))
    testit(calculate_size(49) == (7,7))
    testit(calculate_size(64)==(8,8))
    #testit(calculate_size("hat") == "Error")

    # The following tests test the is_valid_size() function
    print("\n is_valid_size")
    testit(is_valid_size(45,100,20,1100,650)== False)
    testit(is_valid_size(5, 7, 20, 1100, 650) == True)
    testit(is_valid_size(3, 3, 20, 1100, 650) == True)
    testit(is_valid_size(3,3,44,1100,650)==True)




dots_test_suite()

# Notice the lack of a main? This is because this is a test suite; it's not intended to be run as a main() program.
# However, to run the test suite, you run this file. It should just work.
