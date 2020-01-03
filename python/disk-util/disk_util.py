import os
import shutil
import subprocess as sp

def main(): 
        print ("")
        print ("Main Choice: Choose 1 of 5 choices")
        print ("")
        print ("Choose 1 to check disk space")
        print ("Choose 2 to check disk permissions")
        print ("Choose 3 for something")
        print ("Choose 4 for something")
        print ("Choose q to quit script")
        print ("")

        choice = input ("Please make a choice: ")

        if choice == '1':
            print ("")
            print ("This would check disk space")
            print ("")
            tmp = sp.call('clear', shell=True)
            disk_check()
            print ("")
# This elif is pulling the script disk_status.py and running the print_read_permission
# function from that file
        elif choice == '2':
            print ("")
            tmp = sp.call('clear', shell=True)
            print ("")
            perm_check()
            print ("")
        elif choice == '3':
            print ("")
            print ("Do Something 3")
        elif choice == '4':
            print ("")
            print ("Do Something 4")
        elif choice == 'q':
            print ("")
            tmp = sp.call('clear', shell=True)
            exit()
        else:
            print ("")
            print ("Please select a valid option.")
            print ("")
            tmp = sp.call('clear', shell=True)
            main()

def disk_check():
    print ("")
    print ("Available directories to check: ")
    print ("")
    print ("Select 1 to check root")
    print ("Select 2 to check home")
    print ("Select 3 to check var")
    print ("Select q to exit")
    print ("")
    disk_choice = input ("Which directory do you want to check: ")
    print ("")
    if disk_choice == '1':
        tmp = sp.call('clear', shell=True)
        root_space()
    elif disk_choice == '2':
        tmp = sp.call('clear', shell=True)
        home_space()
    elif disk_choice == 'q':
        tmp = sp.call('clear', shell=True)
        exit()
    else:
        print ("")
        print ("Invalid options")

def root_space():
    total, used, free = shutil.disk_usage("//")
    print ("---------------------------")
    print ("Partition: /")
    print ("---------------------------")
    print ("Total: %d GB" % (total // (2**30)))
    print ("Used: %d GB" % (used // (2**30)))
    print ("Free: %d GB" % (free // (2**30)))
    print ("---------------------------")
    print ("")

def home_space():
    total, used, free = shutil.disk_usage("/home")
    print ("---------------------------")
    print ("Partition: /home")
    print ("---------------------------")
    print ("Total: %d GB" % (total // (2**30)))
    print ("Used: %d GB" % (used // (2**30)))
    print ("Free: %d GB" % (free // (2**30)))
    print ("---------------------------")
    print ("")

def perm_check():

    test_file = input ("What file do you want to check [full path]: ")
    
    file_read = os.access(test_file, os.R_OK)
    file_write = os.access(test_file, os.W_OK)
    file_execute = os.access(test_file, os.X_OK)
    
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

main()

