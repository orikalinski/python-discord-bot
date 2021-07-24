class Member(object):
    def __init__(self, user, roles, joined_at, mute, deaf, nick=None, avatar=None, premium_since=None, pending=None,
                 is_pending=None, **kwargs):
        self.user = user
        self.roles = roles
        self.nick = nick
        self.avatar = avatar
        self.premium_since = premium_since
        self.joined_at = joined_at
        self.is_pending = is_pending
        self.pending = pending
        self.mute = mute
        self.deaf = deaf

        self.__dict__.update(**kwargs)
