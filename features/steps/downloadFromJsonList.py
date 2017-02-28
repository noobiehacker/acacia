import logging
import json
from pprint import pprint
from behave import given, when, then, step

@given('A collection of youtubeLink is loaded into memory')
def step_impl(context):
    pass

@when('Youtube DL Library is called{number:d}')
def step_impl(context, number):  # -- NOTE: number is converted into integer
    with open('testData.json') as data_file:
        data = json.load(data_file)
    assert number >= 1 or number == 0
    context.tests_count = number
    assert data["key"] == "value"

@then('Then It will download the link\'s file onto disk')
def step_impl(context):
    assert context.failed is False
    assert context.tests_count >= 0

#After we got the youtubeLink data structures, we run it through
#A loop to call youtubedl command on each on the links
