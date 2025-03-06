from django import template

register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    print(f"Price: {price}, Quantity: {quantity}, Quantity Type: {type(quantity)}")
    if isinstance(quantity, dict):
        print(f"Quantity keys: {quantity.keys()}")
        # Assuming the numeric value is stored under the key 'amount'
        quantity = quantity.get('amount', 0)
        print(f"Extracted Quantity: {quantity}, Extracted Quantity Type: {type(quantity)}")
    return price * quantity
