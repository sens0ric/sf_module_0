import numpy as np

def game(number):
    count = 0                          # счетчик попыток
    step = 50
    predict = step                    # предполагаемое число
    while True:                        # бесконечный цикл
        count += 1                     # плюсуем попытку
        if number == predict: break    # выход из цикла, если угадали
        elif number > predict:
            print (f"Угадываемое число больше {predict} ")
            step = (step + 1) // 2
            predict += step
        elif number < predict:
            print (f"Угадываемое число меньше {predict} ")
            step = (step + 1) // 2
            predict -= step
            
    print (f"Вы угадали число {number} за {count} попыток.")
    return count


def main():
    number = np.random.randint(1,100)    # загадали число
    print ("Загадано число от 1 до 99")
    return game(number)

def test_main():
    max_count = 0
    i = 1000
    while i >= 0:
        i -= 1
        result = main()
        if result > max_count:
            max_count = result
    print(f"Максимальное число попыток {max_count}")

def test_range():
    max_count = 0
    for i in range(1,101):
        result = game(i)
        if result > max_count:
            max_count = result
    print(f"Максимальное число попыток {max_count}")

main()

# test_main()       # test using random input
# test_range()      # test using all possible inputs for range from 1 to 100