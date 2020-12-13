#!/usr/bin/env python3

# Created by: Mohammad-al-buraiki
# Created on December 2020
# This program calculates the cost of a pizza

import constants

def main():
    # this function calculates the  cost of a pizza

    # input
    diameter = input("Enter the diameter of the pizza (inch) :")
    
    # process
    cost1 = (int(diameter)*(constants.MATERIALS)+(constants.LABOR)+(constants.RENT))
    cost2 = (cost1)*(constants.HST)
    total = (cost1)+(cost2)
    
    # output
    print("")
    print("The cost for a {0} inch pizza is: ${1:,.2f}".format(diameter, total))
    
    
if __name__ == "__main__":
    main()
