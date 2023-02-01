<<<<<<< HEAD
import numpy as np

number = np.random.randint(1, 101) # загадываем число

count = 0

while True:
    count += 1
    predict_number = int(input("Угадай число от 1 до 100"))

=======
""" Игра угадай число """

import numpy as np

number =  np.random.randint(1, 101) # загадываем число

count = 0 # колличество попыток

while True:
    count += 1
    predict_number = int(input("Угадай число от 1 до 100:"))
>>>>>>> 15de14d (First commit)
    if predict_number > number:
        print("Число должно быть меньше!")

    elif predict_number < number:
        print("Число должно быть больше!")

    else:
        print(f"Вы угадали число! Это число = {number}, за {count} попыток")
        break # конец игры, выход из цикла
<<<<<<< HEAD
=======
    
>>>>>>> 15de14d (First commit)
