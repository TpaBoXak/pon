from naturals import Natural
from integer import Integer
from rational import Rational
from polynome import Polynome
import telebot


def create_keyboard(buttons):
    new_keyboard = telebot.types.InlineKeyboardMarkup()
    for i in buttons:
        new_keyboard.add(telebot.types.InlineKeyboardButton(i[0], callback_data=i[1]))
    return new_keyboard


f = open('token.txt', 'r')
for i in f:
    bot = telebot.TeleBot(i)
f.close()

numbers_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
numbers_keyboard.row('Натуральные числа')
numbers_keyboard.row('Целые числа')
numbers_keyboard.row('Рациональные числа')
numbers_keyboard.row('Многочлены')
natural_numbers = [('Сравнение натуральных чисел: 2 - если первое больше второго, 0, если равно, 1 иначе.', 'COM_NN_D'),
                   ('Проверка на ноль: если число не равно нулю, то «да» иначе «нет»', 'NZER_N_B'),
                   ('Добавление 1 к натуральному числу', 'ADD_1N_N'),
                   ('Сложение натуральных чисел', 'ADD_NN_N'),
                   ('Вычитание из первого большего натурального числа второго меньшего или равного', 'SUB_NN_N'),
                   ('Умножение натурального числа на цифру', 'MUL_ND_N'),
                   ('Умножение натурального числа на 10^k', 'MUL_Nk_N'),
                   ('Умножение натуральных чисел', 'MUL_NN_N'),
                   ('Вычитание из натурального другого натурального, умноженного на цифру для случая с неотрицательным результатом', 'SUB_NDN_N'),
                   ('Вычисление первой цифры деления большего натурального на меньшее, домноженное на 10^k,где k - номер позиции этой цифры (номер считается с нуля)', 'DIV_NN_Dk'),
                   ('Частное от деления большего натурального числа на меньшее или равное натуральное с остатком(делитель отличен от нуля)', 'DIV_NN_N'),
                   ('Остаток от деления большего натурального числа на меньшее или равное натуральное с остатком(делитель отличен от нуля)', 'MOD_NN_N'),
                   ('НОД натуральных чисел', 'GCF_NN_N'),
                   ('НОК натуральных чисел', 'LCM_NN_N')]
natural_keyboard = create_keyboard(natural_numbers)


def is_natural(s):
    return True


def get_natural(message):
    if is_natural(message.text):

    else:



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     'Этот бот предназначен для использования системы компьютерной алгебры. Выберите вид алгебрических выражений, с которыми хотит работать:',
                     reply_markup=numbers_keyboard)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'натуральные числа':
        bot.send_message(message.chat.id, 'Выберите функцию для работы с натуральными числами:', reply_markup=natural_keyboard)
    elif message.text.lower() == 'целые числа':
        bot.send_message(message.chat.id, 'Выберите функцию для работы с целыми числами:')
    elif message.text.lower() == 'рациональные числа':
        bot.send_message(message.chat.id, 'Выберите функцию для работы с рациональными числами:')
    elif message.text.lower() == 'многочлены':
        bot.send_message(message.chat.id, 'Выберите функцию для работы с многочленами:')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'COM_NN_D':
        bot.send_message(call.message.chat.id, 'Введите первое число')
        bot.register_next_step_handler(call.message, get_natural)

    elif call.data == 'menu':
        print('"press button menu"')


bot.infinity_polling()
