class SalesData(object):

    def __init__(self):
        self.data = [0,4,42]

    def display(self):
        print("Data:")
        for n in self.data:
            print("Next value: ", n)

    def doubleSales(self):
        for i in range(len(self.data)):
            self.data[i] *= 2



