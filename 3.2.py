def discounted(price, discount, max_discount=20):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount=abs(float(max_discount))
        if max_discount > 99:
            raise ValueError('Максимальная скидка не может быть больше 99%')
        if discount >= max_discount:
            return price
        else:
            return price - (price*discount/100)
    except (TypeError , ValueError) :
            return 'Вводить только числа'

print(discounted(100,2))
print(discounted('222',2))
print(discounted('abc',2))