import random

import requests
from io import BytesIO

import json, os

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.upload import VkUpload
from vk_api.utils import get_random_id

from parser_things import *

from commander.commander import Commander
from constants import *

from vk_api.keyboard import VkKeyboard, VkKeyboardColor

def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random.randint(0, 2048)})


def upload_photo(upload, url):
    img = requests.get(url).content
    f = BytesIO(img)

    response = upload.photo_messages(f)[0]

    owner_id = response['owner_id']
    photo_id = response['id']
    access_key = response['access_key']

    return owner_id, photo_id, access_key


def send_photo(vk, user_id, owner_id, photo_id, access_key):
    attachment = f'photo{owner_id}_{photo_id}_{access_key}'
    vk.messages.send(
        random_id=get_random_id(),
        peer_id=user_id,
        attachment=attachment
    )

def send_message(vk_session, id_type, id, message=None, attachment=None, keyboard=None):
    vk.method('messages.send', {id_type: id, 'message': message, 'random_id': random.randint(-2147483648, +2147483648), 'attachment': attachment, 'keyboard': keyboard})
 
def create_keyboard(response):
    keyboard = VkKeyboard(one_time=True)
 
    #if response == 'привет':
    keyboard.add_line()
    keyboard.add_button('Хочу тян', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Тян не нужны!', color=VkKeyboardColor.NEGATIVE)
 
 
    keyboard = keyboard.get_keyboard()
    return keyboard

vk = vk_api.VkApi(token=token)

vk_ses = vk.get_api()

upload = VkUpload(vk)

longpoll = VkLongPoll(vk)

commander = Commander()

ships = parseShips()

items = parseItems()

print("Бот запущен")
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            request = event.text
            request = request.strip().lower()
            if "привет" in request:
                write_msg(event.user_id, hello)

            elif "пока" in request:
                write_msg(event.user_id, bye)

            elif "как дела" in request:
                write_msg(event.user_id, how_are_you_answer[random.randint(0, 3)])
            
            elif 'клавиатура' in request:
                #create_keyboard(request)
                send_message(vk, 'peer_id', event.user_id, 'clava', None, create_keyboard(request))

            elif request.split()[0] == "command":
                write_msg(event.user_id, commander.do(request[8::]))

            elif 'help' in request or 'помощь' in request:
                write_msg(event.user_id, command_list)

            elif 'глад' in request:
                send_photo(vk_ses, event.user_id, *upload_photo(upload, ne_ponyal[random.randint(0, 3)]))

            elif 'инфо' in request:
                output = 0
                for item in material_translate.keys():
                    if item in request:
                        write_msg(event.user_id, material_description[material_translate[item]])
                        send_photo(vk_ses, event.user_id, *upload_photo(upload, material_list[material_translate[item]]))
                        output = 1
                        break
                for ship in ships_translate.keys():
                    if ship in request:
                        write_msg(event.user_id, ships_description[ships_translate[ship]])
                        send_photo(vk_ses, event.user_id, *upload_photo(upload, ship_images[ships_translate[ship]]))
                        write_msg(event.user_id, info_upgrades)
                        output = 1
                if output == 0:        
                    write_msg(event.user_id, info_help)
            elif 'улучшения' in request:
                for ship in ships_translate.keys():
                    if ship in request:
                        write_msg(event.user_id, find_ship_upgrades(ships_translate[ship], ships))
                
                
            else:
                write_msg(event.user_id, help_text)
