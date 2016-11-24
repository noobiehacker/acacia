import unittest
import requests
from bs4 import BeautifulSoup

#Enter a Search Input

def scanInput():
    #person = raw_input('Enter Your Search Input: ')
    #print("Hello", person)
    return True

#Query youtube with search input and return result as HTML String
def queryYoutube(input):
    prefix = "https://www.youtube.com/results?search_query="
    url = prefix + input
    page = requests.get(url)
    return page.content

def isWatchLink(link):
    return link.startswith("/watch?v=")

#Given an HTML Youtube Result page, return first X results parsed into a String Array
def parseDownloadLink(page):
    soup = BeautifulSoup(page, 'html.parser')
    array = set()
    for link in soup.find_all('a'):
        linkhref = link.get('href')
        if isWatchLink(linkhref):
            prefix = "https://www.youtube.com/results?search_query="
            youtubeLink = prefix + linkhref
            array.add(youtubeLink)
    for link in array:
        print(link)
    return array

#Given a Youtube link, download the result


#Give a list of youtube links, download all of the results

# Here's our "unit tests".
class functionTests(unittest.TestCase):

    def testScanInput(self):
        self.assertTrue(scanInput())

    def testQueryYoutube(self):
        input= "Stuff"
        actural = queryYoutube(input)
        self.assertTrue(len(actural) > 500)

    def testParseDownloadLink(self):
        page = queryYoutube("stuff")
        result = parseDownloadLink(page)
        self.assertIsNotNone(result)
        self.assertTrue(len(result) > 9)

    def testIsWatchLink(self):
        success = "/watch?v=7RDSLzHJ74I"
        self.assertTrue(isWatchLink(success))
        failure = "ABCDE"
        self.assertFalse(isWatchLink(failure))

def main():
    unittest.main()

if __name__ == '__main__':
    main()