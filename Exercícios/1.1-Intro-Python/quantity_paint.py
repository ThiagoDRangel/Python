import math

def quantity_paint(measure):
    quantity = math.ceil((measure / 3) / 18)
    price = quantity * 80.00
    
    print(f"Quantidade de latas necessárias: {quantity}")
    print(f"Preço total: R${price:.2f}")
    return (quantity, price)

quantity_paint(100)
