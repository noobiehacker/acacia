import unittest

def isPageMode():
    mode = input('Press A for Whole Page Mode and press anything else for search Mode')
    return mode == "A"

#Enter a Search Input
def scanSearchInput():
    person = input('Enter Your Search Input: or press X to quit: ')
    return person

def scanNumOfResult():
    result = int(input('Please enter number of results in digits: '))
    return result

def userWantsToExit(input):
    return (input == "X")

# Here's our "unit tests".
class functionTests(unittest.TestCase):

    def testOne(selfself):
        print("no Test")

def main():
    unittest.main()

if __name__ == '__main__':
    main()