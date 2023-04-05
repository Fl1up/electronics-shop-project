class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

        self.all = self.all.append(f"{Item.__repr__(self)}")

    def calculate_total_price(self) -> float:
        return self.price * self.quantity


    def apply_discount(self) -> None:
        self.price = self.price * self.pay_rate


