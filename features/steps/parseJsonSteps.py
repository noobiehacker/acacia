import logging
import json
from pprint import pprint
from behave import given, when, then, step

@given('Function is called')
def step_impl(context):
    pass

@when('Json is loaded{number:d}')
def step_impl(context, number):  # -- NOTE: number is converted into integer
    with open('testData.json') as data_file:
        data = json.load(data_file)
#        print("    " + data["key"])
#    print("\n")
    assert number >= 1 or number == 0
    context.tests_count = number
    assert data["key"] == "value"

@then('It will be parsed and loaded in memory')
def step_impl(context):
    assert context.failed is False
    assert context.tests_count >= 0
