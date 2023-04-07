import csv
class Item:
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.__name = name
        self.price = price
        self.quantity = quantity


    def calculate_total_price(self) -> float:
        return self.price * self.quantity


    def apply_discount(self) -> None:
        self.price = self.price * self.pay_rate

    @property
    def name(self):
        return f"{self.__name}"

    @name.setter
    def name(self,word):
        name = word.split(":")
        for i in name:
            self.__name = i

    @classmethod
    def instantiate_from_csv(cls):
        with open('../src/items.csv', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                cls.all.append(cls(row["name"], row["price"], row["quantity"]))

    @staticmethod
    def string_to_number(x):
        return int(float(x))


