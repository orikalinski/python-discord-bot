class Connection(object):
    def __init__(self, id, name, type, visibility, integrations=None, access_token=None):
        self.id = id
        self.name = name
        self.type = type
        self.visibility = visibility
        self.integrations = integrations
        self.access_token = access_token
