'''
Created on Jan 13, 2014

@author: rene
'''

from salesdata import SalesData

def displayGreeting():
    print("Hello Happy Sales People!")
    print("This app shows sales data.")
    print("-------------------------")

    print("Test 1")
    print("Test2")

def main():
    print("Executing main")
    displayGreeting()
    data = SalesData()
    data.display()

if __name__ == '__main__':
    main()