class Role(object):
    def __init__(self, id, name, permissions, position, color, hoist, managed, mentionable, tags=None, **kwargs):
        self.id = int(id)
        self.name = name
        self.permissions = permissions
        self.position = position
        self.color = color
        self.hoist = hoist
        self.managed = managed
        self.mentionable = mentionable
        self.tags = tags

        self.__dict__.update(**kwargs)
