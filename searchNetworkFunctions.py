import unittest
import requests
import downloadFunction

from bs4 import BeautifulSoup

#Query youtube with search input and return result as HTML String
def queryYoutube(input):
    prefix = "https://www.youtube.com/results?search_query="
    postfix = "&sp=EgIYAQ%253D%253D"
    fixedInput = fixInput(input)
    url = prefix + fixedInput + postfix
    page = requests.get(url)
    return page.content

def isWatchLink(link):
    return link.startswith("/watch?v=")

#Given an HTML Youtube Result page, return all results parsed into a String Array
def parseDownloadLinkFromYT(page):
    soup = BeautifulSoup(page, 'html.parser')
    aset = set()
    for link in soup.find_all('a'):
        linkhref = link.get('href')
        if isWatchLink(linkhref):
            prefix = "https://www.youtube.com"
            youtubeLink = prefix + linkhref
            aset.add(youtubeLink)
    for link in aset:
        print(link)
    return aset


def printResult(result):
    if result == True:
        print("Files has been downloaded successfully")
    else:
        print("Files has failed")

def fixInput(input):
    output = input.replace(' ', '+')
    return output

# Here's our "unit tests".
class functionTests(unittest.TestCase):

    def testQueryYoutube(self):
        input= "Stuff"
        actural = queryYoutube(input)
        self.assertTrue(len(actural) > 500)

    def testParseDownloadLink(self):
        page = queryYoutube("stuff")
        result = parseDownloadLinkFromYT(page)
        self.assertIsNotNone(result)
        self.assertTrue(len(result) > 9)

    def testIsWatchLink(self):
        success = "/watch?v=7RDSLzHJ74I"
        self.assertTrue(isWatchLink(success))
        failure = "ABCDE"
        self.assertFalse(isWatchLink(failure))

    def testDownload(self):
        link = "https://www.youtube.com/watch?v=FZvtATBfSpM"
        self.assertTrue(downloadFunction.download(link))

    def testDownloadList(self):
        aset = set()
        aset.add("https://www.youtube.com/watch?v=uw7R_RGAd9I")
        aset.add("https://www.youtube.com/watch?v=q-H62GgHjeg")
        aset.add("https://www.youtube.com/watch?v=V7vjxhqMPng")
        self.assertTrue(downloadFunction.downloadList(aset))

    def testFixInput(self):
        name = "Cosmic Gate"
        result = "Cosmic+Gate"
        actural = fixInput(name)
        self.assertEqual(actural, result)

def main():
    unittest.main()

if __name__ == '__main__':
    main()