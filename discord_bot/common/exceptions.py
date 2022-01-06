class TooManyRequests(Exception):
    def __init__(self, response_json, url):
        super().__init__(response_json)
        self.response_json = response_json
        self.url = url
