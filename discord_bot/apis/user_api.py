from discord_bot.common.endpoints import BASE_URL, GET_ME, GET_USER
from discord_bot.common.request import Request
from discord_bot.models.user import User


class UserAPI(object):
    def __init__(self, token):
        self.token = token

    def get_current_user(self):
        url = BASE_URL + GET_ME
        request = Request(self.token, url, "GET")
        payload = request.execute()
        return User(**payload)

    def get_user(self, user_id):
        url = BASE_URL + GET_USER.format(user_id)
        request = Request(self.token, url, "GET")
        payload = request.execute()
        return User(**payload)
