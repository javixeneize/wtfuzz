HTTP = 'http://'
HTTPS = 'https://'


class wtfconfig():
    def __init__(self):
        self.url = ''
        self.payloads = []

    def setUrl(self, url):
        if (HTTP in url) or (HTTPS in url):
            if (url[-1:] != "/"):
                self.url = url + "/"
            else:
                self.url = url
        else:
            self.url = None
            print("url not valid")

    def getPayloads(self, filename, original=False):
        try:
            with open(filename, 'r') as file:
                self.payloads = file.read().splitlines()
                if original:
                    self.payloads.insert(0, '')  # sends the original request as well
        except FileNotFoundError:
            self.payloads = []
            print("File not found")

    def validConfig(self):
        return self.payloads != [] and self.url is not None
