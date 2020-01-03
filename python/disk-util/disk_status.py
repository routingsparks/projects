import os
import shutil

#test_file = './test.txt'
test_file = input ("What file do you want to check: ")

file_read = os.access(test_file, os.R_OK)
file_write = os.access(test_file, os.W_OK)
file_execute = os.access(test_file, os.X_OK)


def print_read_permission():
    if file_read is True:
        print("You have read access.")
        exit(0)
    else:
        print("You do not have read access.")
        exit(1)


def print_write_permission():
    if file_write is True:
        print("You have write access.")
        exit(0)
    else:
        print("You do not have write access.")
        exit(1)


def print_execute_permission():
    if file_execute is True:
        print("You have execute access.")
        exit(0)
    else:
        print("You do not have execute access.")
        exit(1)


""" This function defines the variable rwx by utilizing the variables defines
in lines 6,7 and 8. It's running and if elif and elf statement to check
permission sets on the file. The elif (else-if) will let you keep passing
inputs into the string, and else is how you'd end the loop. """


def full_file_permission():
    rwx = [file_read, file_write, file_execute]
    rw = [file_read, file_write]
    r = [file_read]
    if all(p is True for p in rwx):
        print("You have rwx rights to this file")
        exit(0)
    elif all(p is True for p in rw):
        print("You have rw rights to this file")
        exit(0)
    elif all(p is True for p in r):
        print("This is a read-only file")
        exit(0)
    else:
        print("You have no file permissions")
        exit(1)


print('True or False, you have write access: ' + str(file_read))
