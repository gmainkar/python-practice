'''
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
'''
class UpperCasing(object):
    def __init__(self):
        self.s = ''

    def inputString(self):
        self.s = input("Enter a string\n")
    
    def outputString(self):
        print(self.s.upper())

newObject = UpperCasing()

newObject.inputString()

newObject.outputString()
