day = int(input('Введите день:\r\n'))
month =  input('Введите месяц:\r\n').lower()
sign = 'Указана неверная дата'
if month == 'январь':
    if day >= 1 and day <=31:
        sign = 'Козерог' if day <= 20 else 'Водолей'
elif month == 'февраль':
    if day >= 1 and day <=28:
        sign = 'Водолей' if day <= 19 else 'Рыбы'
elif month == 'март':
    if day >= 1 and day <=31:
        sign = 'Рыбы' if day <= 20 else 'Овен'
elif month == 'апрель':
    if day >= 1 and day <=30:
        sign = 'Овен' if day <= 20 else 'Телец'
elif month == 'май':
    if day >= 1 and day <=31:
        sign = 'Телец' if day <= 22 else 'Близнецы'
elif month == 'июнь':
    if day >= 1 and day <=30:
        sign = 'Близнецы' if day <= 22 else 'Рак'
elif month == 'июль':
    if day >= 1 and day <=31:
        sign = 'Рак' if day <= 22 else 'Лев'
elif month == 'август':
    if day >= 1 and day <=31:
        sign = 'Лев' if day <= 21 else 'Дева'
elif month == 'сентябрь':
    if day >= 1 and day <=30:
        sign = 'Дева' if day <= 23 else 'Весы'
elif month == 'октябрь':
    if day >= 1 and day <=31:
        sign = 'Весы' if day <= 23 else 'Скорпион'
elif month == 'ноябрь':
    if day >= 1 and day <=30:
        sign = 'Скорпион' if day <= 22 else 'Стрелец'
elif month == 'декабрь':
    if day >= 1 and day <=31:
        sign = 'Стрелец' if day <= 22 else 'Козерог'

print('Ваш знак зодиака: ' + sign)
