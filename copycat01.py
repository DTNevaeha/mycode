#!/usr/bin/env python3
import shutil
import os


def main(): 

#Change to working directory
os.chdir("/home/student/mycode/")

#shutil.copy(source, destination) - Creates a single file copy
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

#shutil.copytree() will copy an entire folder and every folder and file contained in it.
shutil.copytree("5g_research/", "5g_research_backup/")

#Not really sure what this does
if __name__ == "__main__":
    main()
