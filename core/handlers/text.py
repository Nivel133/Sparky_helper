greet = "Привет, {name}, я бот, который поможет тебе не забыть дз и расписание ☺️"
menu = "📍 Главное меню"

def get_start_text(names):
    start_comand = r'/start'
    return f'<b>👋Спасибо, что воспользовались моим ботом, {names}!</b>\n\n'\
    f'📌Отправь мне команду <i>{start_comand}</i> повторно, если захочешь вернуться в главное меню\n'

def get_day_text(user_name):
    return f'<b>{user_name}, </b>\n Введи цифру и букву класса слитно\n, 📎без пробелов и кавычек📎\n'\
                         f'<b><i>📝Пример:</i></b>\n  <i>7б, 5в, 11а</i>'

def data_user_schedule(day_of_week, num_and_letter):
    return f'<b>Вот твое расписание.📇</b> \r\n\n' \
                f'Выбранный день недели📆: <b>{day_of_week}</b>\r\n' \
                f'Выбранный класс📝: <b>{num_and_letter}</b>\r\n' \


def execute_hw_text(homework_message):
    return f'<b>Ты хочешь записать дз: </b>\n\n <i>{homework_message}</i>\n'\
                         f'<b>Всё верно?</b>🔜'


def parser_of_lessons_text(list_of_lessons, list_of_rooms):
    lessons_string = '\n'
    for lesson, room in zip(list_of_lessons, list_of_rooms):
        lessons_string += '📍'
        lessons_string += f'<b><i>{str(lesson)}</i></b>'
        lessons_string += '📍'
        lessons_string += ' КАБ. '
        lessons_string += f'<b><i>{str(room)}</i></b>'
        lessons_string += '🏫'
        lessons_string += '\n '
    # print(lessons_string)
    return lessons_string


enter_hw_text = f'<b>Отлично!</b>\n'\
                f'Отправь мне в следующем сообщении свое домашнее задание, а я сохраню его для тебя💽\n'\
                f'❗❗❗\n<i>Не забудь уточнить на какой предмет и на какой день ты записываешь</i>\n❗❗❗\n'\
                f'<b><i>📝Пример:</i></b>\n ' \
                f'<i>матеша, вторник уч 56 стр 77,78,79,83 упр доделать!</i>\n'


onstartup_text = '📳Бот запущен!📳'
onendup_text = '💤Бот выключен!💤'



