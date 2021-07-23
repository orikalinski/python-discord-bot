class Message(object):
    def __init__(self, id, channel_id, author, content, type, embeds, attachments, components, flags, mention_everyone,
                 mention_roles, mentions, timestamp, pinned, tts, edited_timestamp=None, message_reference=None,
                 referenced_message=None, **kwargs):
        self.id = id
        self.channel_id = channel_id
        self.author = author
        self.content = content
        self.type = type
        self.embeds = embeds
        self.attachments = attachments
        self.components = components
        self.flags = flags
        self.mention_everyone = mention_everyone
        self.mention_roles = mention_roles
        self.mentions = mentions
        self.timestamp = timestamp
        self.pinned = pinned
        self.tts = tts
        self.edited_timestamp = edited_timestamp
        self.message_reference = message_reference
        self.referenced_message = referenced_message

        self.__dict__.update(**kwargs)