from random import choice

variant = {
    1: 'камень',
    2: 'ножницы',
    3: 'бумага'
}


def variant_game(user_choice: int):
    computer_choice = choice(list(variant))
    if user_choice == computer_choice:
        return f'Ничья, Боб выбрал {variant[computer_choice]}'
    
    elif user_choice == 1 and computer_choice == 2 \
        or user_choice == 2 and computer_choice == 3 \
            or user_choice == 3 and computer_choice == 1:
        return f"Вы выйграли, Бот выбрал {variant[computer_choice]}"
    
    elif user_choice == 1 and computer_choice == 3 \
        or user_choice == 2 and computer_choice == 1 \
            or user_choice == 3 and computer_choice == 2:
        return f'Вы проигали, бот выбрал {variant[computer_choice]}'

    else:
        return 'Выберите корректный ответ'

def stiker(result:int):
    pass