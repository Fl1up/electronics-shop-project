from src.item import Item

class MixinLog:
    __slots__ = ["__language"]

    def __init__(self, language="EN"):
        self.__language = language

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.language == "EN":
            self.__language = "RU"
            return self
        else:
            self.__language = "EN"
            return self

class KeyBoard(Item, MixinLog):
   pass




