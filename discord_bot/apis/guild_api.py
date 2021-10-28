from discord_bot.common.endpoints import BASE_URL, GET_GUILD, GET_GUILD_PREVIEW, GUILD_ICON, GET_GUILD_ROLES, \
    GET_GUILD_MEMBERS, GET_GUILD_MEMBERS_SEARCH, GET_GUILD_MEMBER
from discord_bot.common.request import Request
from discord_bot.models.guild import Guild
from discord_bot.models.member import Member
from discord_bot.models.role import Role
from discord_bot.models.user import User


class GuildAPI(object):
    def __init__(self, token):
        self.token = token

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

    @staticmethod
    def _parse_role(role_payload):
        return Role(**role_payload)

    def get_guild_roles(self, guild_id):
        url = BASE_URL + GET_GUILD_ROLES.format(guild_id)
        request = Request(self.token, url, "GET")
        payload = request.execute()
        roles = list()
        for role_payload in payload:
            roles.append(self._parse_role(role_payload))
        return roles

    @staticmethod
    def _parse_member(member_payload):
        member_payload["user"] = User(**member_payload["user"])
        return Member(**member_payload)

    def _get_guild_members_batch(self, base_url, last_user_id=None, limit=1000):
        url = base_url
        if last_user_id:
            url += "?" + f"after={last_user_id}"
        if limit:
            separator = "&" if last_user_id else "?"
            url += separator + f"limit={limit}"
        request = Request(self.token, url, "GET")
        payload = request.execute()
        members = list()
        for member_payload in payload:
            members.append(self._parse_member(member_payload))
        return members

    def get_guild_member(self, guild_id, user_id):
        url = BASE_URL + GET_GUILD_MEMBER.format(guild_id, user_id)
        request = Request(self.token, url, "GET")
        member_payload = request.execute()
        return self._parse_member(member_payload)

    def get_guild_members_iter(self, guild_id):
        url = BASE_URL + GET_GUILD_MEMBERS.format(guild_id)
        fetch_limit = 1000
        current_batch = self._get_guild_members_batch(url, limit=fetch_limit)
        while len(current_batch) == fetch_limit:
            last_user = current_batch[-1]
            last_user_id = last_user.user.id
            for user in current_batch:
                yield user
            current_batch = self._get_guild_members_batch(url, last_user_id=last_user_id, limit=fetch_limit)
        for user in current_batch:
            yield user

    # deprecated
    def get_guild_members(self, guild_id, limit=1000):
        url = BASE_URL + GET_GUILD_MEMBERS.format(guild_id)
        fetch_limit = 1000
        users = current_batch = self._get_guild_members_batch(url, limit=fetch_limit)
        while len(current_batch) >= fetch_limit and (not limit or len(users) < limit):
            last_user = current_batch[-1]
            last_user_id = last_user.user.id
            current_batch = self._get_guild_members_batch(url, last_user_id=last_user_id, limit=fetch_limit)
            users.extend(current_batch)

        return users

    def search_guild_members(self, guild_id, query):
        url = BASE_URL + GET_GUILD_MEMBERS_SEARCH.format(guild_id) + f"?query={query}"
        request = Request(self.token, url, "GET")
        payload = request.execute()
        members = list()
        for member_payload in payload:
            members.append(self._parse_member(member_payload))
        return members
