'''
Created on Jan 13, 2014

@author: rene
'''

from salesdata import SalesData

def displayGreeting():
    print("HELLO HAPPY SALES PEOPLE!")
    print("THIS APP SHOWS SALES DATA")

def main():
    print("Executing main")
    displayGreeting()
    data = SalesData()
    data.display()

if __name__ == '__main__':
    main()