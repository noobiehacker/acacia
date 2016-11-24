import unittest
import requests
from bs4 import BeautifulSoup
import youtube_dl

#Enter a Search Input

def scanSearchInput():
    person = input('Enter Your Search Input: or press X to quit')
    return person

def scanNumOfResult():
    result = int(input('Please enter number of results in digits: '))
    return result

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

#Given an HTML Youtube Result page, return first X results parsed into a String Array
def parseDownloadLink(page):
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

#Given a Youtube link, download the result
def download(link):
    ydl_opts = {'format': 'bestaudio/best',
                'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3'}]}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    return True

#Give a list of youtube links, download all of the results
def downloadList(list, n):
    count = 0
    for link in list:
        download(link)
        count = count + 1
        if count > n:
            break
    return True

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

    def testDownload(self):
        link = "https://www.youtube.com/watch?v=FZvtATBfSpM"
        self.assertTrue(download(link))

    def testDownloadList(self):
        aset = set()
        aset.add("https://www.youtube.com/watch?v=uw7R_RGAd9I")
        aset.add("https://www.youtube.com/watch?v=q-H62GgHjeg")
        aset.add("https://www.youtube.com/watch?v=V7vjxhqMPng")
        self.assertTrue(downloadList(aset))

    def testFixInput(self):
        name = "Cosmic Gate"
        result = "Cosmic+Gate"
        actural = fixInput(name)
        self.assertEqual(actural, result)

def main():
    unittest.main()

if __name__ == '__main__':
    main()