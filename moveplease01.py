#!/usr/bin/env python3
import shutil
import os

def main():
    #Force the program to start in the mycode directory
    os.chdir('/home/student/mycode/')

    #shutil.move(source, destination) will move the file or folder at the path source to the path destination
    shutil.move('raynor.obj', 'ceph_storage/')

    #Asks the user to rename the kerrigan file - best name is Sarah
    xname = input('What is the new name for kerrigan.obj? ')

    #renames the file to the new name
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

main() #Call this function
