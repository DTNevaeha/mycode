#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   Conditionals - strings test true"""

#Ask the user for an IP
ipchk = input("Insert an IP Address")

# a string tests as True
if ipchk:
   print("Looks like the IP address was set: " + ipchk)
else:
    print("You did not provide input.") #If the user left IP blank:
