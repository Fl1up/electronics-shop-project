import csv


class Item:
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self) -> float:
        return self.price * self.quantity

    def apply_discount(self) -> None:
        self.price = self.price * self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, word):
        names = word.split(":")
        for name in names:
            if len(name) <= 10:
                self.__name = name

    @classmethod
    def instantiate_from_csv(cls):
        try:
            with open('items.csv', "r", encoding='UTF-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    cls.all.append(cls(row["name"], row["price"], row["quantity"]))
        except FileNotFoundError:
            print("FileNotFoundError: Отсутствует файл item.csv")
        raise

    @staticmethod
    def string_to_number(x):
        return int(float(x))

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity
