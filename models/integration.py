class Integration(object):
    def __init__(self, id, name, type, role_id, enable_emoticons, expire_behaviour, expire_grace_period, user=None,
                 account=None, synced_at=None, subscriber_count=None, application=None, **kwargs):
        self.id = id
        self.name = name
        self.type = type
        self.role_id = role_id
        self.enable_emoticons = enable_emoticons
        self.expire_behaviour = expire_behaviour
        self.expire_grace_period = expire_grace_period
        self.user = user
        self.account = account
        self.synced_at = synced_at
        self.subscriber_count = subscriber_count
        self.application = application

        self.__dict__.update(**kwargs)
