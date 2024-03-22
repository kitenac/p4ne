import random

'''
 Декоратор может функцию, как переменную использовать:
  - конструировать новые функции из старой - тут cubic  генериться на основе Func_construct
  - т.е. Func_coonstruct - определяет, где и как использовать переданную функцию - как с переменной работа
'''

def Func_construct(x_func):
    def new_func(arg):
        print(f'''
        Исполняется стрый код - считаем random: {random.randint(0, arg)}, 
        потом в дополнение исполняем переданную функцию - куб считаем - {x_func(arg)}
        ''')

        return x_func(arg)

    return new_func

# Генерим новую функцию на основе старой - Func_construct
@Func_construct
def cubic(arg):
   return arg * arg * arg


# Это функция - сгенерирована на основе старой
cubic(100)
