from dataclasses import dataclass
from collections.abc import Callable


@dataclass
class Customer:
    name: str
    age: int


def send_email_promotion(
    customers: list[Customer], is_eligible: Callable[[Customer], bool]
) -> None:
    for customer in customers:
        if is_eligible(customer):
            print(f"Sending promotion email to {customer.name}")


def is_eligible_for_promotion(customer: Customer, cutoff_age: int) -> bool:
    return customer.age > cutoff_age


def is_eligible_closure(cutoff_age: int) -> Callable[[Customer], bool]:
    def is_eligible(customer: Customer) -> bool:
        return customer.age > cutoff_age

    return is_eligible


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
    send_email_promotion(customers, is_eligible_closure(50))


if __name__ == "__main__":
    main()
