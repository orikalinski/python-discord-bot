class User(object):
    def __init__(self, id, username, discriminator, banner, banner_color, public_flags, bio, **kwargs):
        self.id = int(id)
        self.username = username
        self.discriminator = discriminator
        self.banner = banner
        self.banner_color = banner_color
        self.public_flags = public_flags
        self.bio = bio

        self.__dict__.update(**kwargs)
