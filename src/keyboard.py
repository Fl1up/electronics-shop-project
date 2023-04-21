from src.item import Item

class MixinLog:
    Language = "EN"

    def __init__(self):
        self.language = self.Language

class KeyBoard(Item, MixinLog):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    def change_lang(self):
        if self.language == "EN":
            self.language = "RU"
            return self
        elif self.language == "RU":
            self.language = "EN"
            return self
        elif self.language != ("RU", "EN"):
            raise AttributeError("property 'language' of 'KeyBoard' object has no setter")


