import requests


class Request(object):
    def __init__(self, token, url, method, json_data=None, headers=None):
        self.token = token
        self.url = url
        self.method = method
        self.json_data = json_data
        self.headers = headers

    @staticmethod
    def get_response_data(response):
        json_data = {}
        if response.content:
            json_data = response.json()
        return json_data

    def execute(self):
        headers = {"Authorization": f"{self.token}"}
        if self.headers:
            headers.update(self.headers)

        response = requests.request(method=self.method, url=self.url, headers=headers, json=self.json_data)
        return self.get_response_data(response)
