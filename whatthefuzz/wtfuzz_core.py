import requests
from whatthefuzz.wtfconfig import wtfconfig

HTTPVERBS = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'PATCH']
CODE = 'Code'
VERB = 'Verb'
LENGTH = 'Length'
URL = 'url'


# trace and connect not working

class wtfuzz():
    def __init__(self, verify=True):
        self.wtfconfig = wtfconfig()
        self.responses = {}
        self.fullResponses = {}
        self.verbResponses = []
        self.verify = verify

    def config(self, url='', filename='', original=False):
        if url != '':
            self.wtfconfig.setUrl(url)
        if filename != '':
            self.wtfconfig.getPayloads(filename, original)

    def sendSimpleRequest(self):
        if (self.wtfconfig.validConfig()):
            url = self.wtfconfig.url
            payloads = self.wtfconfig.payloads
            for payload in payloads:
                urlp = url + payload
                response = requests.get(urlp, verify=self.verify).status_code
                self.responses[urlp] = response
                print(urlp + " --> " + str(response))
        else:
            print('Url not correctly initialised')

    def fuzzParameter(self, parameter):
        results_list = []
        results = {}
        if (self.wtfconfig.validConfig()):
            url = self.wtfconfig.url
            payloads = self.wtfconfig.payloads
            for payload in payloads:
                urlp = url.replace(parameter, payload)
                response = requests.get(urlp, verify=self.verify)
                self.responses[urlp] = response.status_code
                results['payload'] = payload
                results['length'] = len(response.content)
                results['code'] = response.status_code
                results_list.append(results.copy())
        else:
            print('Url not correctly initialised')
        length_list = sorted(results_list, key=lambda k: k['length'])
        code_list = sorted(results_list, key=lambda k: k['code'])
        print(length_list[0])
        print(length_list[-1])
        print(code_list[0])
        print(code_list[-1])

    def fuzzInteger(self, parameter):
        results_list = []
        results = {}
        if (self.wtfconfig.validConfig()):
            url = self.wtfconfig.url
            payloads = list(range(20, 22))
            for payload in payloads:
                urlp = url.replace(parameter, str(payload))
                response = requests.get(urlp, verify=self.verify)
                self.responses[urlp] = response.status_code
                results['payload'] = payload
                results['length'] = len(response.content)
                results['code'] = response.status_code
                results_list.append(results.copy())
        else:
            print('Url not correctly initialised')
        length_list = sorted(results_list, key=lambda k: k['length'])
        code_list = sorted(results_list, key=lambda k: k['code'])
        print(length_list[0])
        print(length_list[-1])
        print(code_list[0])
        print(code_list[-1])

    def sendVerbRequest(self, verb):
        if verb in HTTPVERBS:
            if (self.wtfconfig.validConfig()):
                url = self.wtfconfig.url
                payloads = self.wtfconfig.payloads
                for payload in payloads:
                    urlp = url + payload
                    response = getattr(requests, str(verb).lower())(urlp, verify=self.verify).status_code
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
                    response = getattr(requests, str(verb).lower())(urlp, verify=self.verify)
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
                response = getattr(requests, str(verb).lower())(url, allow_redirects=False, verify=self.verify)
                fullresp = {}
                fullresp[CODE] = response.status_code
                fullresp[VERB] = str(verb).lower()
                fullresp[LENGTH] = len(response.content)
                self.verbResponses.append(fullresp)
                print(url + " " + str(fullresp))
        else:
            print('Url/Payloads not correctly initialised')

    def sendFullRequest_report(self, verb, folders):
        report = []
        payloads = self.wtfconfig.payloads
        if verb in HTTPVERBS:
            for item in folders:
                if item[-1] != '/':
                    item = item + '/'
                self.wtfconfig.url = item
                if (self.wtfconfig.validConfig()):
                    url = self.wtfconfig.url
                    for payload in payloads:
                        urlp = url + payload
                        try:
                            response = getattr(requests, str(verb).lower())(urlp, verify=self.verify)
                            fullresp = self.__set_response_data(response, verb, urlp)
                        except requests.exceptions.ConnectionError:
                            fullresp = self.__set_response_data(verb=str(verb).lower(), error=True)
                        report.append(fullresp)
                else:
                    print('Url/Payloads not correctly initialised')
        else:
            print("Error - Verb " + verb + " not valid")
        return report

    def sendAllVerbsRequest_report(self, folders):
        report = []
        for item in folders:
            self.wtfconfig.url = item
            if self.wtfconfig.url is not None:
                url = self.wtfconfig.url
                for verb in HTTPVERBS:
                    try:
                        response = getattr(requests, str(verb).lower())(url, allow_redirects=False, verify=self.verify)
                        fullresp = self.__set_response_data(response, verb, url)
                    except requests.exceptions.ConnectionError:
                        fullresp = self.__set_response_data(verb=str(verb).lower(), error=True)
                    report.append(fullresp)
            else:
                print('Url/Payloads not correctly initialised')
        return report

    def sendFullFoldersAndVerbsRequest_report(self, folders):
        report = []
        payloads = self.wtfconfig.payloads
        for item in folders:
            for verb in HTTPVERBS:
                if item[-1] != '/':
                    item = item + '/'
                self.wtfconfig.url = item
                if (self.wtfconfig.validConfig()):
                    url = self.wtfconfig.url
                    for payload in payloads:
                        urlp = url + payload
                        try:
                            response = getattr(requests, str(verb).lower())(urlp, verify=self.verify)
                            fullresp = self.__set_response_data(response, verb, urlp)
                        except requests.exceptions.ConnectionError:
                            fullresp = self.__set_response_data(verb=str(verb).lower(), error=True)
                        report.append(fullresp)

                else:
                    print('Url/Payloads not correctly initialised')
        else:
            print("Error - Verb " + verb + " not valid")
        return report

    def __set_response_data(self, response='', verb='', url='', error=False):
        fullresp = {}
        if not error:

            fullresp[CODE] = response.status_code
            fullresp[VERB] = str(verb).lower()
            fullresp[LENGTH] = len(response.content)
            fullresp[URL] = url
        else:
            fullresp[CODE] = 0
            fullresp[VERB] = str(verb).lower()
            fullresp[LENGTH] = 0
            fullresp[URL] = 'Connection error'
        return fullresp
