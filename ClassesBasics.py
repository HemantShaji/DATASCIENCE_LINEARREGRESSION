import math
Constant_INT=10
Constant_String='Hello Hemant'

#Define a class inside which we will define functions under the class

class democlass:

    def firstfn(self):
        self.int=10
        self.string='i am using PYCHARM'
    #Using another function to give the print commands for the above
    def secondfn(self):
        print(self.int)
        print(self.string)


#Create a function to Manage all these called functions outside of the class
def main():
    x= democlass().secondfn()

_name_=0

if _name_== '_main_':
    main()
