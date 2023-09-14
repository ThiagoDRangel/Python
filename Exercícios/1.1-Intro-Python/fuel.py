#  Álcool:
#    - Até 20 litros, desconto de 3% por litro;
#    - Acima de 20 litros, desconto de 5% por litro.
#  Gasolina:
#    - Até 20 litros, desconto de 4% por litro;
#    - Acima de 20 litros, desconto de 6% por litro.

def fuel(liters, fuel_type):
    if fuel_type.lower() == "a":
        price_per_liter = 1.90
        discount = 0.03 if liters <= 20 else 0.05
        total_price = liters * price_per_liter * (1 - discount)
        print(f"Total a pagar: R${total_price:.2f} por {liters} litros de álcool")
    elif fuel_type.lower() == "g":
        price_per_liter = 2.50
        discount = 0.04 if liters <= 20 else 0.06
        total_price = liters * price_per_liter * (1 - discount)
        print(f"Total a pagar: R${total_price:.2f} por {liters} litros de gasolina")
    else:
        print("Tipo de combustível inválido, tente novamente!")

fuel(10, 'g')

