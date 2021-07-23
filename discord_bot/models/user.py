class User(object):
    def __init__(self, id, username, discriminator, banner=None, banner_color=None, public_flags=None,
                 bio=None, **kwargs):
        self.id = int(id)
        self.username = username
        self.discriminator = discriminator
        self.banner = banner
        self.banner_color = banner_color
        self.public_flags = public_flags
        self.bio = bio

        self.__dict__.update(**kwargs)
