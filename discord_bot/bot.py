from discord_bot.apis.channel_api import ChannelAPI
from discord_bot.apis.user_api import UserAPI
from discord_bot.models.button import Button
from discord_bot.models.menu import Menu


class Bot(object):
    def __init__(self, bot_token):
        self.token = f"Bot {bot_token}"
        self.users_api = UserAPI(self.token)
        self.channels_api = ChannelAPI(self.token)
        self.user = self.get_current_user()

    def get_current_user(self):
        return self.users_api.get_current_user()

    def get_user(self, user_id):
        return self.users_api.get_user(user_id)

    def get_channel(self, channel_id):
        return self.channels_api.get_channel(channel_id)

    def get_guild(self, guild_id):
        return self.channels_api.get_guild(guild_id)

    def get_guild_preview(self, guild_id):
        return self.channels_api.get_guild_preview(guild_id)

    def get_guild_icon_url(self, guild_id, icon_hash):
        return self.channels_api.get_guild_icon_url(guild_id, icon_hash)

    def get_message(self, channel_id, message_id):
        return self.channels_api.get_message(channel_id, message_id)

    def get_messages(self, channel_id):
        return self.channels_api.get_messages(channel_id)

    def delete_message(self, channel_id, message_id):
        return self.channels_api.delete_message(channel_id, message_id)

    def send_message(self, channel_id, content, menu=None):
        return self.channels_api.send_message(channel_id, content, menu=menu)

    def edit_message(self, channel_id, message_id, content, menu=None):
        return self.channels_api.edit_message(channel_id, message_id, content, menu=menu)
