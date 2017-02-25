import logging
from behave import given, when, then, step

@given('Function is called')
def step_impl(context):
    import logging
    loglevel = logging.DEBUG
    logging.basicConfig(level=loglevel)
    logging.debug("Some messages to be shown just when debugging or unittesting")
    pass

@when('Json is loaded{number:d}')
def step_impl(context, number):  # -- NOTE: number is converted into integer
    assert number > 1 or number == 0
    context.tests_count = number

@then('It will be parsed and loaded in memory')
def step_impl(context):
    assert context.failed is False
    assert context.tests_count >= 0
