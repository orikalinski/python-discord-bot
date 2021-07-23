from discord_bot.common.endpoints import BASE_URL, GET_CHANNEL, GET_GUILD, GET_GUILD_PREVIEW, GUILD_ICON, \
    CHANNEL_MESSAGE, CHANNEL_MESSAGES
from discord_bot.common.request import Request
from discord_bot.models.channel import Channel
from discord_bot.models.guild import Guild
from discord_bot.models.message import Message
from discord_bot.models.user import User


class ChannelAPI(object):
    def __init__(self, token):
        self.token = token

    def get_channel(self, channel_id):
        url = BASE_URL + GET_CHANNEL.format(channel_id)
        payload = Request(self.token, method="GET", url=url).execute()
        return Channel(**payload)

    def get_guild(self, guild_id):
        url = BASE_URL + GET_GUILD.format(guild_id)
        request = Request(self.token, url, "GET")
        payload = request.execute()
        return Guild(**payload)

    def get_guild_preview(self, guild_id):
        url = BASE_URL + GET_GUILD_PREVIEW.format(guild_id)
        request = Request(self.token, url, "GET")
        payload = request.execute()
        return Guild(**payload)

    @staticmethod
    def get_guild_icon_url(guild_id, icon_hash):
        return GUILD_ICON.format(guild_id, icon_hash)

    def _parse_message(self, message_payload):
        message_payload["author"] = User(**message_payload["author"])
        referenced_message = message_payload.get("referenced_message")
        if referenced_message:
            message_payload["referenced_message"] = self._parse_message(referenced_message)
        return Message(**message_payload)

    def get_message(self, channel_id, message_id):
        url = BASE_URL + CHANNEL_MESSAGE.format(channel_id, message_id)
        request = Request(self.token, url, "GET")
        payload = request.execute()
        return self._parse_message(payload)

    def get_messages(self, channel_id):
        url = BASE_URL + CHANNEL_MESSAGES.format(channel_id)
        request = Request(self.token, url, "GET")
        payload = request.execute()
        messages = list()
        for message_payload in payload:
            messages.append(self._parse_message(message_payload))
        return messages

    def delete_message(self, channel_id, message_id):
        url = BASE_URL + CHANNEL_MESSAGE.format(channel_id, message_id)
        request = Request(self.token, url, "DELETE")
        return request.execute()

    def send_message(self, channel_id, content, menu=None):
        url = BASE_URL + CHANNEL_MESSAGES.format(channel_id)
        json_data = {"content": content}
        if menu:
            json_data["components"] = menu.to_components()
        request = Request(self.token, url, "POST", json_data=json_data)
        return request.execute()

    def edit_message(self, channel_id, message_id, content, menu=None):
        url = BASE_URL + CHANNEL_MESSAGE.format(channel_id, message_id)
        json_data = {"content": content}
        if menu:
            json_data["components"] = menu.to_components()
        request = Request(self.token, url, "PATCH", json_data=json_data)
        return request.execute()
