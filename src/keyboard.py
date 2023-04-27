from src.item import Item

class MixinLog:
    Language = "EN"

    def __init__(self):
        self._language = self.Language

    @property
    def language(self,):
        return self._language

    @language.setter
    def language(self, value):
        self._language = value
        raise AttributeError("property 'language' of 'KeyBoard' object has no setter")

class KeyBoard(Item, MixinLog):
    def change_lang(self):
        if self.language == "EN":
            self._language = "RU"
            return self
        elif self.language == "RU":
            self._language = "EN"
            return self




