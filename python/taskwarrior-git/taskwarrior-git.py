#!/usr/bin/python3

import os
import subprocess
import sys

####################################################################
# GOALS FOR THIS SCRIPT
#####################################################################
# The goal for this will be to have hook written in python that 
# will complete a git add, git commit -a -m, and a git push every
# time a task is modified. The variables should include the .task
# and the .taskrc in order to keep everything up to date in github.




#TASK_DIR = os.path.dirname(__file__) + os.sep + os.pardir

TASK_DIR = os.path.expanduser("~") + os.path.join('.task')
TASKRC_DIR = os.path.expanduser("~") + os.path.join('.taskrc')

if os.path.exists(TASK_DIR):
    print("True")
else:
    print("False")


