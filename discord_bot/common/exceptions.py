class TooManyRequests(Exception):
    def __init__(self, response, url):
        super().__init__()
        self.response = response
        self.url = url
