import logging
import json
import downloadFunction
import searchNetworkFunctions
from pprint import pprint
from behave import given, when, then, step

@given('Function is called')
def step_impl(context):
    pass

@when('Json is loaded{number:d}')
def step_impl(context, number):  # -- NOTE: number is converted into integer
    with open('testData.json') as data_file:
        data = json.load(data_file)
        #niceData = json.dumps(json.load(data_file))
    #1 Create a for loop that download All Music from the Json
    #print("\n")
    #print(len(data['links']))
    #print("\n")
    bound = len(data['links'])
    for index in range(bound):
        link = data['links'][index]['key']
        print("\n")
        print(link)
        print("\n")
        downloadResult = downloadFunction.download(link)
        searchNetworkFunctions.printResult(downloadResult)
    #1b Pass link to youtubedl library to download file
    #for x in range(youtubelist.count):
    #     downloadResult = downloadFunction.downloadList(youtubelist[x])
    assert number >= 1 or number == 0
    context.tests_count = number

@then('It will be parsed and loaded in memory')
def step_impl(context):
    assert context.failed is True
    assert context.tests_count >= 0

#After we got the youtubeLink data structures, we run it through
#A loop to call youtubedl command on each on the links
