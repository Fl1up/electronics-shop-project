from src.item import Item


class MixinLog:
    Language = "EN"

    def __init__(self):
        self.language = self.Language


class Keyboard(Item, MixinLog):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    def change_lang(self):
        if self.language == "EN":
            self.language = "RU"
            return self.Language
        if self.language == "RU":
            self.language = "EN"
            return self.Language
        elif self.language != "RU" and "EN":
            raise AttributeError("property 'language' of 'KeyBoard' object has no setter")
