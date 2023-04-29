from src.item import Item


class MixinLog:
    def __init__(self):
        self.language = "EN"

    def change_lang(self):
        if self.language == "EN":
            self.language = "RU"
            return self
        elif self.language == "RU":
            self.language = "EN"
            return self


class KeyBoard(Item, MixinLog):
    def __init__(self, name, price, quantity, language='EN'):
        super().__init__(name, price, quantity)
        self._language = language

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        if value not in ["EN", "RU"]:
            raise AttributeError("property 'language' of 'KeyBoard' object has no setter")
        self._language = value




