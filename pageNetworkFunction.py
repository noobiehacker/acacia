import unittest
import requests
import downloadFunction
from bs4 import BeautifulSoup
from selenium import webdriver

def downloadAllLinksFromWB(url):
    #1 Open The Link With Selenium Browser
    page = requests.get(url)

    #2 Find all the iframes 's src
    frameEmdSrcs = findAllFramesEmdSrc(page.content)

    #3 Transform into dlable link and download
    downloadAllLinkFromSrcs(frameEmdSrcs)

def downloadAllLinkFromSrcs(frameEmdSrcs):
    for src in frameEmdSrcs:
        downloadLinkFromEmdSrc(src)

def openLinkWithSelenium(link):
    driver = webdriver.Chrome()
    driver.get(link)
    return driver

def findAllFramesEmdSrc(source):
    frameSrc = []
    soup = BeautifulSoup(source, 'html.parser')
    for iframe in soup.find_all('iframe'):
        src = iframe.get('src')
        if src!= None and src.startswith("https://www.youtube.com/embed/"):
            frameSrc.append(src)
    return frameSrc

def downloadLinkFromEmdSrc(frameSrc):
    downloadableLink = turnEmbedLinkToDlLink(frameSrc)
    downloadFunction.download(downloadableLink)

def turnEmbedLinkToDlLink(embLink):
    id = parseIDFromEmbLink(embLink)
    return "https://www.youtube.com/watch?v=" + id

def parseIDFromEmbLink(embLink):
    startIndex = 'embed/'
    return embLink[embLink.index(startIndex) + len(startIndex):]

# Here's our "unit tests".
class functionTests(unittest.TestCase):

    def testDownloadAllLinksFromWB(self):
        link = 'http://www.billboard.com/articles/columns/k-town/6828140/best-k-pop-songs-2015'
        downloadAllLinksFromWB(link)

    def testFindAllFramesEmdedSource(self):
        link = 'http://www.billboard.com/articles/columns/k-town/6828140/best-k-pop-songs-2015'
        driver = openLinkWithSelenium(link)
        source = driver.page_source.encode('utf-8')
        frameSrc = findAllFramesEmdSrc(source)
        self.assertTrue(len(frameSrc) > 0)

    def testTurnEmbedLinkToDlLink(self):
        input = 'https://www.youtube.com/embed/zzC3HXA50cs'
        result = turnEmbedLinkToDlLink(input)
        expected = "https://www.youtube.com/watch?v=zzC3HXA50cs"
        self.assertEqual(result, expected)

    def testParseIDFromEmbLink(self):
        input = 'https://www.youtube.com/embed/zzC3HXA50cs'
        result = parseIDFromEmbLink(input)
        expected = "zzC3HXA50cs"
        self.assertEqual(result,expected)

def main():
    unittest.main()

if __name__ == '__main__':
    main()