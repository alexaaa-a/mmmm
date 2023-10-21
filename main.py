import telebot
from telebot import custom_filters
from telebot import StateMemoryStorage
from telebot.handler_backends import StatesGroup, State


state_storage = StateMemoryStorage()
# Вставить свой токет или оставить как есть, тогда мы создадим его сами
bot = telebot.TeleBot("6439483110:AAGWU4cdYyb449pgDUljTmnUFFfAwBiXYbI",
                      state_storage=state_storage, parse_mode='Markdown')


class PollState(StatesGroup):
    name = State()
    age = State()


class HelpState(StatesGroup):
    wait_text = State()


text_poll = "Расскажи сказку"  # Можно менять текст
text_button_1 = "Лучшие мультики"  # Можно менять текст
text_button_2 = "Песенки"  # Можно менять текст
text_button_3 = "Мультики!"  # Можно менять текст


menu_keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
menu_keyboard.add(
    telebot.types.KeyboardButton(
        text_poll,
    )
)
menu_keyboard.add(
    telebot.types.KeyboardButton(
        text_button_1,
    )
)

menu_keyboard.add(
    telebot.types.KeyboardButton(
        text_button_2,
    ),
    telebot.types.KeyboardButton(
        text_button_3,
    )
)


@bot.message_handler(state="*", commands=['start'])
def start_ex(message):
    bot.send_message(
        message.chat.id,
        'Привет! Я Атта, твой персональный друг, чем будем заниматься?',  # Можно менять текст
        reply_markup=menu_keyboard)

@bot.message_handler(func=lambda message: text_poll == message.text)
def first(message):
    bot.send_message(message.chat.id, 'В давние времена осёл, как рассказывает сказка, пел получше тенора. Однажды'
                                      ' собрались все звери на совет, и лев, который был у них царём, спросил:'
                                      ' – Кто из вас самый красивый? – Я, я! – сразу же закричал осёл.'
                                      ' – Хорошо, ты самый красивый. – А кто же самый сильный?'
                                      ' – Я, я! – закричал осёл раньше, чем остальные звери успели раскрыть рты.'
                                      ' – Ладно, – сказал лев. – А кто здесь самый глупый? – Я, я, я! – второпях заревел осёл,'
                                      ' испугавшись, как бы его не опередили. Все звери так и покатились со смеху,'
                                      ' а бедняга осёл со стыда потерял свой красивый голос. И с тех пор он'
                                      ' только и умеет реветь: – Я, я, я! *НАПИШИ "ещё" ДЛЯ ДРУГОЙ СКАЗКИ*')  # Можно менять текст
    bot.set_state(message.from_user.id, PollState.name, message.chat.id)


@bot.message_handler(state=PollState.name)
def name(message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['name'] = message.text
    bot.send_message(message.chat.id,   'Дождь громко стучал по крыше. Котёнок Гав сидел на своём чердаке и боялся. '
                                        'А к нему в гости пришёл щенок с первого этажа. — Гав, — позвал щенок, — где ты?'
                                        ' — Я тут, — ответил Гав из самого дальнего угла чердака. — Что ты делаешь?'
                                        ' — Боюсь дождя. — Давай вместе бояться, — предложил щенок, сел рядом с котёнком,'
                                        ' и они стали бояться вместе. Щенок послушал, послушал, как стучит дождь, '
                                        'и ему на самом деле стало страшно. — Знаешь что, — сказал щенок, — пойдём'
                                        ' лучше вниз бояться. Котёнок и щенок спустились на первый этаж и сели на '
                                        'самой нижней ступеньке. — Нет, — сказал Гав, — здесь дождя совсем не слышно, '
                                        'и поэтому бояться неинтересно. Я лучше пойду побоюсь на чердаке.'
                                        ' *НАПИШИ "ещё" ДЛЯ ДРУГОЙ СКАЗКИ*')  # Можно менять текст
    bot.set_state(message.from_user.id, PollState.age, message.chat.id)



@bot.message_handler(state=PollState.age)
def age(message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['age'] = message.text
    bot.send_message(message.from_user.id,'К сожалению, сказок больше нет! Приношу свои извинения!')  # Можно менять текст
    bot.delete_state(message.from_user.id, message.chat.id)


@bot.message_handler(func=lambda message: text_button_1 == message.text)
def help_command(message):
    bot.send_message(message.chat.id, "Вот что нашлось в интернете: [Популярные мультфильмы](https://yandex.ru/search/?text=%D0%9F%D0%BE%D0%BF%D1%83%D0%BB%D1%8F%D1%80%D0%BD%D1%8B%D0%B5+%D0%BC%D1%83%D0%BB%D1%8C%D1%82%D1%84%D0%B8%D0%BB%D1%8C%D0%BC%D1%8B&clid=2411726&lr=192)", reply_markup=menu_keyboard)  # Можно менять текст


@bot.message_handler(func=lambda message: text_button_2 == message.text)
def help_command(message):
    bot.send_message(message.chat.id, "Вот твои песенки: [Сборник песен для детей](https://www.youtube.com/watch?v=eFLeZSEKjZ8)", reply_markup=menu_keyboard)  # Можно менять текст


@bot.message_handler(func=lambda message: text_button_3 == message.text)
def help_command(message):
    bot.send_message(message.chat.id, 'Приятного просмотра: [Маша и медведь](https://www.youtube.com/watch?v=1V3ZY_TXKwU), [Синий Трактор](https://www.youtube.com/watch?v=0PxL90M56Cw&list=PLEjv3nvaXinE5P--iWKGNQ_sCdFwD2b9z)', reply_markup=menu_keyboard)  # Можно менять текст


bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.add_custom_filter(custom_filters.TextMatchFilter())

bot.infinity_polling()