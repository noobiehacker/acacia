import unittest

#Enter a Search Input

def scanInput():
    person = raw_input('Enter Your Search Input: ')
    print("Hello", person)
    return True

#Query youtube with search input and return result as HTML String


#Given an HTML Youtube Result page, return first X results parsed into a String Array


#Given a Youtube link, download the result


#Give a list of youtube links, download all of the results

# Here's our "unit tests".
class functionTests(unittest.TestCase):

    def testScanInput(self):
        self.failUnless(scanInput())

def main():
    unittest.main()

if __name__ == '__main__':
    main()