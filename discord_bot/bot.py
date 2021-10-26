from discord_bot.apis.channel_api import ChannelAPI
from discord_bot.apis.guild_api import GuildAPI
from discord_bot.apis.user_api import UserAPI
from discord_bot.common.permissions import has_permission, MANAGE_MESSAGES_PERMISSION, ADMINISTRATOR_PERMISSION


class Bot(object):
    def __init__(self, bot_token):
        self.token = f"Bot {bot_token}"
        self.user_api = UserAPI(self.token)
        self.channel_api = ChannelAPI(self.token)
        self.guild_api = GuildAPI(self.token)
        self.user = self.get_current_user()

    def get_current_user(self):
        return self.user_api.get_current_user()

    def get_user(self, user_id):
        return self.user_api.get_user(user_id)

    def get_channel(self, channel_id):
        return self.channel_api.get_channel(channel_id)

    def get_guild(self, guild_id):
        return self.guild_api.get_guild(guild_id)

    def get_guild_preview(self, guild_id):
        return self.guild_api.get_guild_preview(guild_id)

    def get_guild_icon_url(self, guild_id, icon_hash):
        return self.guild_api.get_guild_icon_url(guild_id, icon_hash)

    def get_message(self, channel_id, message_id):
        return self.channel_api.get_message(channel_id, message_id)

    def get_messages(self, channel_id):
        return self.channel_api.get_messages(channel_id)

    def delete_message(self, channel_id, message_id):
        return self.channel_api.delete_message(channel_id, message_id)

    def send_message(self, channel_id, content, menu=None, reply_to_message_id=None):
        return self.channel_api.send_message(channel_id, content, menu=menu, reply_to_message_id=reply_to_message_id)

    def edit_message(self, channel_id, message_id, content, menu=None):
        return self.channel_api.edit_message(channel_id, message_id, content, menu=menu)

    def get_guild_roles(self, guild_id):
        return self.guild_api.get_guild_roles(guild_id)

    def get_guild_members_iter(self, guild, limit=1000):
        yield self.guild_api.get_guild_members_iter(guild, limit=limit)

    def get_guild_members(self, guild_id, limit=1000):
        return self.guild_api.get_guild_members(guild_id, limit=limit)

    @staticmethod
    def _has_manage_messages_permission(user_roles, guild_roles):
        for user_role_id in user_roles:
            role = guild_roles.get(int(user_role_id))
            if role:
                permissions = int(role.permissions)
                if any(has_permission(permissions, permission) for permission in [ADMINISTRATOR_PERMISSION,
                                                                                  MANAGE_MESSAGES_PERMISSION]):
                    return True
        return False

    def get_guild_admins(self, guild_id, members=None):
        guild = self.guild_api.get_guild(guild_id)
        guild_owner_id = guild.owner_id
        guild_members = self.get_guild_members(guild_id, limit=None) if members is None else members
        guild_roles = {role.id: role for role in self.get_guild_roles(guild_id)}
        admins = list()
        for member in guild_members:
            user = member.user
            user_id = user.id
            if user_id == guild_owner_id or self._has_manage_messages_permission(member.roles, guild_roles):
                admins.append(member)
        return admins

    def search_guild_members(self, guild_id, query):
        return self.guild_api.search_guild_members(guild_id, query)

    def get_guild_member(self, guild_id, user_id):
        return self.guild_api.get_guild_member(guild_id, user_id)
