'''
Created on Jan 13, 2014

@author: rene
'''

from salesdata import SalesData


def displayGreeting():
    print("Hello Happy Sales People!")
    print("This app shows sales data.")
    print("-------------------------")

def main():
    displayGreeting()
    data = SalesData()
    data.display()
    data.doubleSales()
    data.display()

if __name__ == '__main__':
    main()
