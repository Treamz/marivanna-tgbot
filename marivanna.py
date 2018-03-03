# Copyright Ivan Chernoknizhnikov t.me/treamz
# https://github.com/Treamz/

import telebot
from telebot import types
import pymysql
import time
from time import sleep

API_TOKEN = 'YOUR API KEY' # TG BOT KEY

daysweek = ['/monday - Понедельник','/tuesday - Вторник','/wednesday - Среда','/thursday - Четверг', '/friday - Пятница',]
del_daysweek = ['/del_monday - Понедельник','/del_tuesday - Вторник','/del_wednesday - Среда','/del_thursday - Четверг', '/del_friday - Пятница',]
# Handle 'start' and 'help'

pares_dict = {}


class Pares:
    def __init__(self, day):
        self.day = day
        self.fpare = None
        self.secpare = None
        self.thirdpare = None
        self.fourthpare = None
        self.fifthpare = None
        self.sixthpare = None
        self.seventhpare = None
        self.eighthpare = None
        


def nullcheack():
    if pares.fpare == "0":
        pares.fpare = None
        return pares.fpare
        


# Handle delete sch
@bot.message_handler(commands=['delete'])
def delete(message):
     msg = bot.send_message(message.chat.id, 'Какой день вы хотите удалить? \n' + ('\n'.join(del_daysweek)))
     bot.register_next_step_handler(msg, process_first_step_delete)
    
def process_first_step_delete(message):
    chat_id = message.chat.id
    conn = pymysql.connect(host='localhost', port=3306, user='mysql',passwd='mysql', db='mysql', use_unicode=True, charset="utf8")
    cur = conn.cursor(pymysql.cursors.DictCursor)
    chatidd = str(message.chat.id)
    if message.text =="/del_monday":
        dday = "mysql.monday_info"
    if message.text =="/del_tuesday":
        dday = "mysql.tuesday_info"
    if message.text =="/del_wednesday":
        dday = "mysql.wednesday_info"
    if message.text =="/del_thursday":
        dday = "mysql.thursday_info"
    if message.text =="/del_friday":
        dday = "mysql.friday_info"
    isql = "DELETE FROM {} WHERE chatidd={}".format(dday, chatidd)
    cur.execute(isql)
    conn.commit()

# Handle 'start' and 'help'
@bot.message_handler(commands=['start'])
def start(message):
     bot.send_message(message.chat.id, 'Привет,надо расписание?')
     print(str(message.chat.id))

@bot.message_handler(commands=['sch'])
def addsch(message):

     info =  'Пожалуйста,выберите день:''\n' + ('\n'.join(daysweek))
     print(info)
     bot.send_message(message.chat.id, info)

# Handle add day
@bot.message_handler(commands=['addmonday', 'addtuesday', 'addwednesday', 'addthursday', 'addfriday'])
def add_tuesday(message):
    chat_id = message.chat.id
    if message.text == "/addmonday":
        day = "mysql.monday_info"
    if message.text == "/addtuesday":
        day = "mysql.tuesday_info"
    if message.text == "/addwednesday":
        day = "mysql.wednesday_info"
    if message.text == "/addthursday":
        day = "mysql.thursday_info"
    if message.text == "/addfriday":
        day = "mysql.friday_info"
    pares = Pares(day)
    pares_dict[chat_id] = pares
    msg = bot.reply_to(message, 'Какая у тебя первая пара? Если ее нет пиши 0')
    bot.register_next_step_handler(msg, process_first_step)

def process_first_step(message):
    try:
        chat_id = message.chat.id
        fpare = message.text
        pares = pares_dict[chat_id]
        pares.fpare = fpare
        msg = bot.reply_to(message, 'А вторая? Если ее нет пиши 0')
        bot.register_next_step_handler(msg, process_second_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_second_step(message):
    try:
        chat_id = message.chat.id
        secpare = message.text

        pares = pares_dict[chat_id]
        pares.secpare = secpare
        msg = bot.reply_to(message, 'А Третья? Если ее нет пиши 0')
        bot.register_next_step_handler(msg, process_third_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_third_step(message):
    try:
        chat_id = message.chat.id
        thirdpare = message.text

        pares = pares_dict[chat_id]
        pares.thirdpare = thirdpare
        msg = bot.reply_to(message, 'А Четвертая? Если ее нет пиши 0')
        bot.register_next_step_handler(msg, process_fourth_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_fourth_step(message):
    try:
        chat_id = message.chat.id
        fourthpare = message.text

        pares = pares_dict[chat_id]
        pares.fourthpare = fourthpare
        msg = bot.reply_to(message, 'А Пятая? Если ее нет пиши 0')
        bot.register_next_step_handler(msg, process_fifth_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')        

def process_fifth_step(message):
    try:
        chat_id = message.chat.id
        fifthpare = message.text

        pares = pares_dict[chat_id]
        pares.fifthpare = fifthpare
        msg = bot.reply_to(message, 'А Шестая? Если ее нет пиши 0')
        bot.register_next_step_handler(msg, process_sixth_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')    

def process_sixth_step(message):
    try:
        chat_id = message.chat.id
        sixthpare = message.text

        pares = pares_dict[chat_id]
        pares.sixthpare = sixthpare
        msg = bot.reply_to(message, 'А седьмая? Если ее нет пиши 0')
        bot.register_next_step_handler(msg, process_seventh_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')            

def process_seventh_step(message):
    try:
        chat_id = message.chat.id
        seventhpare = message.text

        pares = pares_dict[chat_id]
        pares.seventhpare = seventhpare
        msg = bot.reply_to(message, 'А Восьмая? Если ее нет пиши 0')
        bot.register_next_step_handler(msg, process_eighth_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')       

def process_eighth_step(message):
    try:
        chat_id = message.chat.id
        eighthpare = message.text

        pares = pares_dict[chat_id]
        pares.eighthpare = eighthpare
        TUESDAY = '\n' + pares.fpare + '\n' + pares.secpare + '\n' + pares.thirdpare + '\n' + pares.fourthpare + '\n' + pares.fifthpare + '\n' + pares.sixthpare + '\n' + pares.seventhpare + '\n' + pares.eighthpare
        info = 'Сохранить пары?'
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Да', 'Нет')
        msg = bot.send_message(chat_id, TUESDAY + '\n' + info, reply_markup=markup)
        bot.register_next_step_handler(msg, process_ninth_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')
def process_ninth_step(message):
    try:
        chat_id = message.chat.id
        pares = pares_dict[chat_id]
        TUESDAY = '\n' + pares.fpare + '\n' + pares.secpare + '\n' + pares.thirdpare + '\n' + pares.fourthpare + '\n' + pares.fifthpare + '\n' + pares.sixthpare + '\n' + pares.seventhpare + '\n' + pares.eighthpare
        if message.text == "Да":
           conn = pymysql.connect(host='localhost', port=3306, user='mysql',passwd='mysql', db='mysql', use_unicode=True, charset="utf8")   
           cur = conn.cursor(pymysql.cursors.DictCursor)
           chatidd = str(message.chat.id)
           #isql = "INSERT INTO mysql.tuesday_info (first, second, third, fourth, fifth, sixth, seventh, eighth, chatidd)  VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(pares.fpare, pares.secpare, pares.thirdpare, pares.fourthpare, pares.fifthpare, pares.sixthpare, pares.seventhpare, pares.eighthpare, chatidd)
           isql = "INSERT INTO {} (first, second, third, fourth, fifth, sixth, seventh, eighth, chatidd)  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);".format(pares.day)
           if pares.fpare == "0":
              pares.fpare = "Пары нет"
           if pares.secpare == "0":
              pares.secpare = "Пары нет"
           if pares.thirdpare == "0":
              pares.thirdpare = "Пары нет"
           if pares.fourthpare == "0":
              pares.fourthpare = "Пары нет"
           if pares.fifthpare == "0":
              pares.fifthpare = "Пары нет"
           if pares.sixthpare == "0":
              pares.sixthpare = "Пары нет" 
           if pares.seventhpare == "0":
              pares.seventhpare = "Пары нет"
           if pares.eighthpare == "0":
              pares.eighthpare = "Пары нет"
           print(pares.fpare)
           cur.execute(isql,  (pares.fpare, pares.secpare, pares.thirdpare, pares.fourthpare, pares.fifthpare, pares.sixthpare, pares.seventhpare, pares.eighthpare, chatidd))
           conn.commit()
           bot.send_message(message.chat.id, 'Пары сохранены')
        else:   
           bot.send_message(chat_id, 'Пары не сохранены') 
    except Exception as e:
        bot.reply_to(message, 'oooop23s')


@bot.message_handler(commands=['monday', 'tuesday', 'wednesday', 'thursday', 'friday'])
def monday_info(message):
     try:
         conn = pymysql.connect(host='localhost', port=3306, user='mysql',passwd='mysql', db='mysql', use_unicode=True, charset="utf8")
         cur = conn.cursor(pymysql.cursors.DictCursor)   
         chatidd = str(message.chat.id) 
         day = None 
         if message.text == "/monday":
            day = "mysql.monday_info"
         if message.text == "/tuesday":
            day = "mysql.tuesday_info"
         if message.text == "/wednesday":
            day = "mysql.wednesday_info"
         if message.text == "/thursday":
            day = "mysql.thursday_info"
         if message.text == "/friday":
            day = "mysql.friday_info"
         print(day)
         ssql = "SELECT first, second, third, fourth, fifth, sixth, seventh, eighth, chatidd FROM {} WHERE chatidd='{}'".format(day, chatidd)
         cur.execute(ssql)
         for row in cur.fetchall():
           try_sch_mon = ('<b>Первая:</b> ' + row['first'],'<b>Вторая:</b> ' + row['second'],'<b>Третья:</b> ' + row['third'],'<b>Четвертая:</b> ' + row['fourth'],'<b>Пятая:</b> ' + row['fifth'],'<b>Шестая:</b> ' + row['sixth'],'<b>Седьмая:</b> ' + row['seventh'],'<b>Восьмая:</b> ' + row['eighth'])
           print('***********************************')
           #print('\n Первая:' + row['first'],'\n Вторая: ' + row['second'],'\n Третья: ' + row['third'],'\n Четвертая: ' + row['fourth'],'\n Пятая: ' + row['fifth'],'\n Шестая: ' + row['sixth'],'\n Седьмая: ' + row['seventh'],'\n Восьмая: ' + row['eighth'])
           print('***********************************')
       
           for item in try_sch_mon:
             if not item.find("Пары") != -1:
                 print(item)
                 
                 bot.send_message(message.chat.id, item, parse_mode="HTML")
           
           
           #try_sch_mon = ('\n'.join(try_sch_mon))
           #bot.send_message(message.chat.id, try_sch_mon, parse_mode="HTML")
               
     except:     

         bot.send_message(message.chat.id, 'Сорри,чет не получилось')


while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print('***********************************')
        print(e)
        print('***********************************')
        sleep(15)