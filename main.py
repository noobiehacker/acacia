import function

def makemydir(whatever):
  try:
    os.makedirs(whatever)
  except OSError:
    pass
  # let exception propagate if we just can't
  # cd into the specified directory
  os.chdir(whatever)

def main():

    #1)Scan In User Input
    searchInput = function.scanSearchInput()
    numOfResult = function.scanNumOfResult()

    #1.1)Make Directory
    makemydir(searchInput)

    #2)Go to youtube and search with input
    page = function.queryYoutube(searchInput)

    #3)Parse result into a list of array
    list = function.parseDownloadLink(page)

    #4)Download all files in array one by one
    downloadResult = function.downloadList(list, numOfResult)

    function.printResult(downloadResult)

if __name__ == '__main__':
   main()