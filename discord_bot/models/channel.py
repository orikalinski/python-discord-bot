from discord_bot.models.permission_override import PermissionOverride
from discord_bot.models.role import Role


class Channel(object):
    def __init__(self, id, guild_id, name, last_message_id, nsfw, parent_id, type, position, permission_overwrites,
                 roles, topic=None, rate_limit_per_user=None, **kwargs):
        self.id = int(id)
        self.guild_id = int(guild_id)
        self.name = name
        self.last_message_id = last_message_id
        self.nsfw = nsfw
        self.parent_id = parent_id
        self.type = type
        self.position = position
        self.permission_overwrites = [PermissionOverride(**permission_override)
                                      for permission_override in permission_overwrites]
        self.roles = [Role(**role) for role in roles]
        self.topic = topic
        self.rate_limit_per_user = rate_limit_per_user

        self.__dict__.update(**kwargs)
