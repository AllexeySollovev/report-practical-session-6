temperature = float(input("Введите температуру (°C): "))
pressure = int(input("Введите давление: "))
pulse = int(input("Введите пульс (уд/мин): "))

if (temperature < 35 or temperature > 38) or \
   (pressure < 105 or pressure > 140) or \
   (pulse < 55 or pulse > 110):
    status = "Требуется врач"

elif (35 <= temperature < 36 or 37 < temperature <= 38) or \
     (105 <= pressure < 110 or 130 < pressure <= 140) or \
     (55 <= pulse < 60 or 100 < pulse <= 110):
    status = "Легкое недомогание"

else:
    status = "Нормальное состояние"

print(f"Результат анализа: {status}")
