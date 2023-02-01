<<<<<<< HEAD
=======
"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""

>>>>>>> 15de14d (First commit)
import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
<<<<<<< HEAD

=======
    
>>>>>>> 15de14d (First commit)
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # предполагаемое число
        if number == predict_number:
            break # выход из цикла, если угадали
    return(count)
<<<<<<< HEAD
def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм
=======

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм
>>>>>>> 15de14d (First commit)

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
<<<<<<< HEAD
    np.random.seed(1) # фиксируем сид для воcпроизводимости
=======
    np.random.seed(1) # фиксируем сид для воспроизводимости
>>>>>>> 15de14d (First commit)
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

<<<<<<< HEAD
=======
# RUN
>>>>>>> 15de14d (First commit)
if __name__ == '__main__':
    score_game(random_predict)