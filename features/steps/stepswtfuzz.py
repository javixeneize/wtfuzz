from behave import *
from wtfuzz.wtfuzz_core import *


@given(u'a configured wtfuzz')
def step_impl(context):
    context.wtfuzz = wtfuzz()
    context.wtfuzz.config("https://www.example.org", 'test/test.txt')


@when(u'I send a request to a valid endpoint')
def step_impl(context):
    context.wtfuzz.sendSimpleRequest()


@then(u'I expect to receive a valid http code')
def step_impl(context):
    assert (context.wtfuzz.responses[context.wtfuzz.wtfconfig.url] == 200)


@when(u'I send a HEAD request to a valid endpoint')
def step_impl(context):
    context.wtfuzz.sendVerbRequest("HEAD")


@when(u'I send a HEAD full request to a valid endpoint')
def step_impl(context):
    context.wtfuzz.sendFullRequest("HEAD")


@then(u'I expect to receive a full response')
def step_impl(context):
    assert (context.wtfuzz.fullResponses[context.wtfuzz.wtfconfig.url] == {'Code': 200, 'Verb': 'head', 'Length': 0})
