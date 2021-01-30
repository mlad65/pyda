width = 15
length = 50
height = 15

if width < 15 and length < 15 and height < 15:
    output = 'Стандартная коробка №1'
elif width < 50 and length < 50 and height < 50:
    output = 'Стандартная коробка №2'
elif length > 200:
    output = 'Упаковка для лыж'
else:
    output = 'Стандартная коробка №3'

print(output)