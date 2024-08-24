from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menu_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("✅ Ovoz berish",request_contact=True),
            KeyboardButton("❌ Bekor qilish")
        ]
    ],
    resize_keyboard=True
)