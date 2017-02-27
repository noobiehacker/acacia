import unittest
from youtubeLink import YoutubeLink

class YoutubeLinkTest(unittest.TestCase):

    def testInit(self):
        self.assertTrue(YoutubeLink("","") != None)

if __name__ == '__main__':
    unittest.main()
