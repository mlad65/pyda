number = 123411
left = str(number)[:3]
right = str(number)[3:]
print('Счастливый билет' if int(left[0]) + int(left[1]) + int(left[2]) == int(right[0]) + int(right[1]) + int(right[2]) else 'Несчастливый билет')
    