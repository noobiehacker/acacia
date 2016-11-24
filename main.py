import networkFunctions
import folderFunctions

def main():

    #1)Scan In User Input
    while True:
        searchInput = networkFunctions.scanSearchInput()
        if searchInput == "X":
            break
        numOfResult = networkFunctions.scanNumOfResult()

    #1.1)Make Directory
    folderFunctions.makemydir(searchInput)

    #2)Go to youtube and search with input
    page = networkFunctions.queryYoutube(searchInput)

    #3)Parse result into a list of array
    list = networkFunctions.parseDownloadLink(page)

    #4)Download all files in array one by one
    downloadResult = networkFunctions.downloadList(list, numOfResult)

    networkFunctions.printResult(downloadResult)

    folderFunctions.goUpOneDirectory()


if __name__ == '__main__':
   main()