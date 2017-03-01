import logging
import json
import downloadFunction
from pprint import pprint
from behave import given, when, then, step

@given('Function is called')
def step_impl(context):
    pass

@when('Json is loaded{number:d}')
def step_impl(context, number):  # -- NOTE: number is converted into integer
    with open('testData.json') as data_file:
        data = json.load(data_file)
    #1 Create a for loop that does two tasks
    #1a Read a Link from the Json
    json_data_row = 10
    youtubelist = []
    for row in range json_data_row
        link = data["key"]
        youtubelist.append(link)
    #1b Pass link to youtubedl library to download file
    for x in range(youtubelist.count):
        downloadResult = downloadFunction.downloadList(youtubelist[x])
        searchNetworkFunctions.printResult(downloadResult)
    assert number >= 1 or number == 0
    context.tests_count = number
    assert data["key"] == "value"

@then('It will be parsed and loaded in memory')
def step_impl(context):
    assert context.failed is False
    assert context.tests_count >= 0

#After we got the youtubeLink data structures, we run it through
#A loop to call youtubedl command on each on the links
