import openpyxl
import random


book = openpyxl.load_workbook(filename='schedule.xlsx')
ws = book.active


def get_column_for_class(num_and_letter: str) -> int:
    try:
        for i in range(1, ws.max_row):
            current_cell = ws.cell(row=4, column=i)
            if str(current_cell.value).lower() == num_and_letter:
                index_current_cell = current_cell.column
                # print('Найденный столбик: ', current_cell.column, '\nАдрес ячейки: ', current_cell.coordinate)
                return index_current_cell

        print('Такого класса не существует')
    except:
        print('что-то не так с поиском нужного класса')


def get_day_of_week_row(day_of_week: str) -> int:
    try:
        for i in range(1, ws.max_column):
            current_cell = ws.cell(row=i, column=1)
            if str(current_cell.value).lower() == day_of_week:
                # print('Найденная строка: ', current_cell.row)
                return current_cell.row
    except:
        print('День не удаётся найти')


def get_schedule(column, row):
    lessons_list = []
    lessons_room = []
    try:
        for i in range(7):
            cur_cell = ws.cell(row=row + i, column=column)
            cur_cell_room = ws.cell(row=row + i, column=column+1)
            if cur_cell.value is None:
                continue
            if cur_cell_room.value is None:
                continue

            lessons_list.append(cur_cell.value)
            lessons_room.append(cur_cell_room.value)

        return lessons_list, lessons_room
    except:
        return None


# print(get_schedule(get_column_for_class('5б'), get_day_of_week_row('понедельник')))


def parser_of_data_hw(data):
    list_of_emoji = ['⚠', '📎', '📌', '🔬🧬', '🗿', '📵', '🆘']
    result_string = ''
    for homework in data:
        for target in homework:
            cur_emoji = random.choice(list_of_emoji)
            #здесь можно отправлять дату создания дз
            result_string += f'{cur_emoji*5}\n'
            result_string += f'{str(target)}\n'
    return result_string


# написать фукнцию для вывода целой недели на класс
# нужно написать фукцию, которая будет кидать рассписание по таймеру на каждый день
# написать фунции для сохранения дз и его изменения


# def get_schedule_for_all_week(num_and_letter: str):
#     d1 = get_schedule(get_column_for_class(num_and_letter), get_day_of_week_row('понедельник'))
#     d2 = get_schedule(get_column_for_class(num_and_letter), get_day_of_week_row('вторник'))
#     d3 = get_schedule(get_column_for_class(num_and_letter), get_day_of_week_row('среда'))
#     d4 = get_schedule(get_column_for_class(num_and_letter), get_day_of_week_row('четверг'))
#     d5 = get_schedule(get_column_for_class(num_and_letter), get_day_of_week_row('пятница'))
#     d6 = get_schedule(get_column_for_class(num_and_letter), get_day_of_week_row('суббота'))
#
#     print(
#         'понедельник \n', d1,
#           '\nвторник \n', d2,
#           '\nсреда \n', d3,
#           '\nчетверг \n', d4,
#           '\nпятница \n', d5,
#           '\nсуббота \n', d6)
#
#
# get_schedule_for_all_week('5б')