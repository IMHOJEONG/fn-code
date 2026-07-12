from typing import NewType

UserId = NewType('UserId', int)
ProductId = NewType('ProductId', int)

def process_order(user_id: UserId, product_id: ProductId) -> None:
    print(f"Processing order for User {user_id}, Product {product_id}")

user_id = UserId(1)
product_id = ProductId(1)

process_order(user_id, product_id)
process_order(product_id, user_id)
