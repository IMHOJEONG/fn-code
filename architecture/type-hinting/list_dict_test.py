def process_order(items: list[str],
                  quantities: list[int]) -> dict[str, int]:
    return {
        item: quantity for item,
        quantity in zip(items, quantities)
    } 

order = process_order(['apple', 'banana', 'orange'], [2,3,1])
print(order)