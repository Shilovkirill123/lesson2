age_2=int(input('Введите Ваш возраст: '))
def busy(age):
    if age <=6:
        return 'Детский сад'
    elif 7 <= age <=17:
         return 'Школа'
    elif 18<= age <= 23:
        return 'Вуз'
    else:
        return 'Пора работать'
x=busy(age_2)
print(x)