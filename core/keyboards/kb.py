from aiogram.types import InlineKeyboardButton, \
    InlineKeyboardMarkup, KeyboardButton, \
    ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import emoji


kb_days_of_week = [
    [
        KeyboardButton(text="понедельник"),
        KeyboardButton(text="вторник"),
        KeyboardButton(text="среда"),
    ],
    [
        KeyboardButton(text="четверг"),
        KeyboardButton(text="пятница"),
        KeyboardButton(text="суббота")
    ],
]

keyboard_days_of_week = ReplyKeyboardMarkup(
    keyboard=kb_days_of_week,
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Выберите день недели"
)


kb_yes_no = [
    [
        KeyboardButton(text="✅"),
        KeyboardButton(text="❌")
    ],
    [
        KeyboardButton(text="Назад")
    ]
]
keyboard_yes_no = ReplyKeyboardMarkup(
    keyboard=kb_yes_no,
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Всё верно?"
)


ikb_confirm_schedule = InlineKeyboardMarkup(
    inline_keyboard=[
        [

        InlineKeyboardButton(
            text='Да',
            callback_data='sch_yes'
        )
        ],
        [
        InlineKeyboardButton(
            text='Нет',
            callback_data='sch_no'
        )
        ]
    ]
)

kb_main_menu = [
    [
        KeyboardButton(text="Расписание"),
        KeyboardButton(text="Домашнее Задание")
    ],
]
keyboard_main_menu = ReplyKeyboardMarkup(
    keyboard=kb_main_menu,
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Чем я могу быть полезен?"
)


# def get_num_builder():
#     builder = ReplyKeyboardBuilder()
#     for i in range(5, 11):
#         # builder.button(text=str(i))
#         builder.add(KeyboardButton(text=str(i)))
#     builder.adjust(3)
#
#     return builder.as_markup(resize_keyboard=True,one_time_keyboard=True,input_field_placeholder="Выберите цифру класса"),
#
#
# print(get_num_builder())