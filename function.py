import unittest
import requests
from bs4 import BeautifulSoup
import youtube_dl

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
    aset = set()
    for link in soup.find_all('a'):
        linkhref = link.get('href')
        if isWatchLink(linkhref):
            prefix = "https://www.youtube.com/results?search_query="
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
def downloadList(list):
    for link in list:
        download(link)
    return True

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

def main():
    unittest.main()

if __name__ == '__main__':
    main()