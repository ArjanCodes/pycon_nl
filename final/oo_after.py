from dataclasses import dataclass


@dataclass
class Customer:
    name: str
    age: int


class Promotion:
    def is_eligible(self, customer: Customer) -> bool:
        return customer.age > 50

    def send_email_promotion(self, customers: list[Customer]) -> None:
        for customer in customers:
            if self.is_eligible(customer):
                print(f"Sending promotion email to {customer.name}")


class AdvancedPromotion(Promotion):
    def is_eligible(self, customer: Customer) -> bool:
        return super().is_eligible(customer) and not customer.name.startswith("H")


def main() -> None:
    customers = [
        Customer("Alice", 25),
        Customer("Bob", 30),
        Customer("Charlie", 35),
        Customer("David", 40),
        Customer("Eve", 45),
        Customer("Frank", 50),
        Customer("Grace", 55),
        Customer("Holly", 60),
        Customer("Iris", 65),
    ]
    promotion = AdvancedPromotion()
    promotion.send_email_promotion(customers)


if __name__ == "__main__":
    main()
