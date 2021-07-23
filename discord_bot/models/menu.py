class Menu(object):
    def __init__(self, components, **kwargs):
        self.type = 1
        self.components = components

        self.__dict__.update(**kwargs)

    def to_components(self):
        return [{"type": 1, "components": [button.to_dict() for button in row]}
                for row in self.components]
