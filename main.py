import networkFunctions
import folderFunctions
import userSearchInput
import IOFunctions

import os
def scanInInput():

    result = []
    while True:
        searchInput = networkFunctions.scanSearchInput()
        if networkFunctions.userWantsToExit(searchInput):
            break
        numOfResult = networkFunctions.scanNumOfResult()
        input = userSearchInput.UserSearchInput(searchInput,numOfResult)
        result.append(input)
    return result

def executeSearchMode():

    # 1.0)Scan In User Input
    array = scanInInput()
    baseDirectory = os.getcwd()

    for item in array:
        # 1.1)Make Directory
        folderFunctions.makemydir(item.searchInput)

        # 2)Go to youtube and search with input
        page = networkFunctions.queryYoutube(item.searchInput)

        # 3)Parse result into a list of array
        list = networkFunctions.parseDownloadLinkFromYT(page)

        # 4)Download all files in array one by one
        downloadResult = networkFunctions.downloadList(list, item.numOfResult)

        networkFunctions.printResult(downloadResult)

        os.chdir(baseDirectory)

def executePageMode():

def main():

    #1.01)Set up the mode
    if IOFunctions.isPageMode():
        executePageMode()
    else:
        executeSearchMode()

if __name__ == '__main__':
   main()