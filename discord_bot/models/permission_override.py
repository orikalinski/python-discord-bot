class PermissionOverride(object):
    def __init__(self, id, type, allow, deny, **kwargs):
        self.id = int(id)
        self.type = int(type)
        self.allow = int(allow)
        self.deny = int(deny)
        self.__dict__.update(**kwargs)
