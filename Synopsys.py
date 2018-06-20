# Python Program to find the pairs that results in sum of 10
# I am choosing python as a first choice to solve this exercise.


class Utility:

    # Constructor
        def __init__(self):
            pass
# Function that takes input

        def read(self):
            print("Please enter the list of numbers:")
            myList = input().split(",")                                          # Storing numbers in list
            return myList

# Function that outputs the pairs whose sum is 10
        def returnpair(self,myList):

            for i in range(len(myList)):
                for j in range(len(myList)):
                    if (int(myList[i]) + int(myList[j])) == 10:
                        print('(' + str(myList[i]) + ',' + str(myList[j]) + ')', end=',')    # Print the output pairs

# Calling the function to perform the operation
        returnpair('self',read('self'))


