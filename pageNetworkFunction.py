import unittest
import downloadFunction
from bs4 import BeautifulSoup
from selenium import webdriver

def downloadAllLinksFromWB(url):
    #1 Open The Link With Selenium Browser
    driver = openLinkWithSelenium(url)

    #2 Find all the iframes

    frameIDs = findAllFramesID(driver.page_source.encode('utf-8'))

    #3 Loop through each iframe
    for id in frameIDs:
        # 3.1 Load element in iframe
        frame = loadInFrameSource(driver,id)

        #3.2 Find and download list in iframe
        downloadLinkFromFrame(frame)

        #3.3 Move back to main page
        driver.switch_to.default_content()

def openLinkWithSelenium(link):
    driver = webdriver.Chrome()
    driver.get(link)
    return driver

def findAllFramesID(page):
    #Todo Implement
    frameIDs = []
    return frameIDs

def loadInFrameSource(driver , id):
    #Todo Implement
    frame = None
    return frame

def downloadLinkFromFrame(frame):
    soup = BeautifulSoup(frame, 'html.parser')
    for link in soup.find_all('a'):
        linkhref = link.get('href')
        if isWatchLink(linkhref):
            downloadFunction.download(linkhref)

def isWatchLink(link):
    return link.startswith("http://www.youtube.com/watch?v=")

# Here's our "unit tests".
class functionTests(unittest.TestCase):

    def testFindAllFramesID(self):
        self.asserTrue(False)

    def testLoadInFrameSource(self):
        self.assertTrue(False)

def main():
    unittest.main()

if __name__ == '__main__':
    main()