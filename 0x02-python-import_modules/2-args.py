#!/usr/bin/python3
from sys import argv

num_of_args = len(argv)

if num_of_args == 1:
    print("{} arguments.".format(num_of_args-1))
elif num_of_args == 2:
    print("{} argument:".format(num_of_args-1))
    print("{}: {}".format(num_of_args-1, argv[num_of_args-1]))
else:
    print("{} arguments:".format(num_of_args-1))
    for i in range(1,num_of_args):
        print("{}: {}".format(i, argv[i]))
