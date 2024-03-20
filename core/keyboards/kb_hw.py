from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, \
         KeyboardButton, ReplyKeyboardMarkup



ikb_confirm = InlineKeyboardMarkup(
    inline_keyboard=[
        [

        InlineKeyboardButton(
            text='Да',
            callback_data='yes_hw'
        )
        ],
        [
        InlineKeyboardButton(
            text='Нет',
            callback_data='no_hw'
        )
        ]
    ]
)


kb_main_hw = [
    [
        KeyboardButton(text="Записать"),
        KeyboardButton(text="Посмотреть"),
        KeyboardButton(text="🔙")
    ],
]
keyboard_main_hw = ReplyKeyboardMarkup(
    keyboard=kb_main_hw,
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Ты хочешь посмотреть или записать ДЗ?"
)