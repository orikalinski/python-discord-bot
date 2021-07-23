class Button(object):
    def __init__(self, label, url=None, custom_id=None, **kwargs):
        self.type = 2
        self.label = label
        self.url = url
        self.custom_id = custom_id

    def to_dict(self):
        data = {"type": self.type, "label": self.label}
        if self.custom_id:
            style = 1
            data["custom_id"] = self.custom_id
        elif self.url:
            style = 5
            data["url"] = self.url
        else:
            raise Exception("You need either custom_id or url in order to use Button")
        data["style"] = style
        return data
