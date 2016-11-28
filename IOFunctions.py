import unittest

def isPageMode():
    mode = input('Press A for Whole Page Mode and press anything else for search Mode')
    return mode == "A"

#Enter a Search Input
def scanSearchInput():
    return input('Enter Your Search Input: or press X to quit: ')

def scanPageInput():
    return input('Please enter the url you want to parse: ')

def scanNumOfResult():
    return int(input('Please enter number of results in digits: '))

def userWantsToExit(input):
    return (input == "X")

def scanInFolderName():
    return input('Please enter folder name of your choice: ')

# Here's our "unit tests".
class functionTests(unittest.TestCase):

    def testOne(selfself):
        print("no Test")

def main():
    unittest.main()

if __name__ == '__main__':
    main()