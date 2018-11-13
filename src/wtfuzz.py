import requests
import sys

sys.path.append('src')
from wtfconfig import wtfconfig

HTTPVERBS = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'PATCH']
CODE = 'Code'
VERB = 'Verb'
LENGTH = 'Length'

# trace and connect not working

class wtfuzz():
    def __init__(self):
        self.wtfconfig = wtfconfig()
        self.responses = {}
        self.fullResponses = {}
        self.verbResponses = []

    def config(self, url='', filename=''):
        if url != '':
            self.wtfconfig.setUrl(url)
        if filename != '':
            self.wtfconfig.getPayloads(filename)

    def sendSimpleRequest(self):
        if (self.wtfconfig.validConfig()):
            url = self.wtfconfig.url
            payloads = self.wtfconfig.payloads
            for payload in payloads:
                urlp = url + payload
                response = requests.get(urlp).status_code
                self.responses[urlp] = response
                print(urlp + " --> " + str(response))
        else:
            print('Url not correctly initialised')

    def sendVerbRequest(self, verb):
        if verb in HTTPVERBS:
            if (self.wtfconfig.validConfig()):
                url = self.wtfconfig.url
                payloads = self.wtfconfig.payloads
                for payload in payloads:
                    urlp = url + payload
                    response = getattr(requests, str(verb).lower())(urlp).status_code
                    self.responses[urlp] = response
                    print(urlp + " " + str(verb).lower() + " --> " + str(response))
            else:
                print('Url not correctly initialised')
        else:
            print("Error - Verb " + verb + " not valid")

    def sendFullRequest(self, verb):
        if verb in HTTPVERBS:
            if (self.wtfconfig.validConfig()):
                url = self.wtfconfig.url
                payloads = self.wtfconfig.payloads
                for payload in payloads:
                    urlp = url + payload
                    response = getattr(requests, str(verb).lower())(urlp)
                    fullresp = {}
                    fullresp[CODE] = response.status_code
                    fullresp[VERB] = str(verb).lower()
                    fullresp[LENGTH] = len(response.content)
                    self.fullResponses[urlp] = fullresp
                    print(urlp + " " + str(fullresp))
            else:
                print('Url/Payloads not correctly initialised')
        else:
            print("Error - Verb " + verb + " not valid")

    def sendAllVerbsRequest(self):
        if self.wtfconfig.url is not None:
            url = self.wtfconfig.url
            for verb in HTTPVERBS:
                response = getattr(requests, str(verb).lower())(url, allow_redirects=False)
                fullresp = {}
                fullresp[CODE] = response.status_code
                fullresp[VERB] = str(verb).lower()
                fullresp[LENGTH] = len(response.content)
                self.verbResponses.append(fullresp)
                print(url + " " + str(fullresp))
        else:
            print('Url/Payloads not correctly initialised')
