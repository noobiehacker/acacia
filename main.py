import searchNetworkFunctions
import folderFunctions
import userSearchInput
import IOFunctions
import os
import downloadFunction

def scanInInputForSearchMode():

    result = []
    while True:
        searchInput = IOFunctions.scanSearchInput()
        if IOFunctions.userWantsToExit(searchInput):
            break
        numOfResult = IOFunctions.scanNumOfResult()
        input = userSearchInput.UserSearchInput(searchInput,numOfResult)
        result.append(input)
    return result

def executeSearchMode():

    # 1.0)Scan In User Input
    array = scanInInputForSearchMode()
    baseDirectory = os.getcwd()

    for item in array:
        # 1.1)Make Directory
        folderFunctions.makemydir(item.searchInput)

        # 2)Go to youtube and search with input
        page = searchNetworkFunctions.queryYoutube(item.searchInput)

        # 3)Parse result into a list of array
        list = searchNetworkFunctions.parseDownloadLinkFromYT(page)

        # 4)Download all files in array one by one
        downloadResult = downloadFunction.downloadList(list, item.numOfResult)

        searchNetworkFunctions.printResult(downloadResult)

        os.chdir(baseDirectory)

def executePageMode():
    print("Implement ME")

def main():

    #1.01)Set up the mode
    if IOFunctions.isPageMode():
        executePageMode()
    else:
        executeSearchMode()

if __name__ == '__main__':
   main()