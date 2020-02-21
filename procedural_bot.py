import random

import requests
from io import BytesIO

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.upload import VkUpload
from vk_api.utils import get_random_id

from commander.commander import Commander
from constants import *

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

vk = vk_api.VkApi(token=token)

vk_ses = vk.get_api()

upload = VkUpload(vk)

longpoll = VkLongPoll(vk)

commander = Commander()

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

            elif request.split()[0] == "command":
                write_msg(event.user_id, commander.do(request[8::]))

            elif 'help' in request or 'помощь' in request:
                write_msg(event.user_id, command_list)

            elif 'крол' in request:
                send_photo(vk_ses, event.user_id, *upload_photo(upload, ne_ponyal[random.randint(0, 3)]))

            elif 'инфо' in request:
                output = 0
                for i in material_translate.keys():
                    if i in request:
                        write_msg(event.user_id, material_description[material_translate[i]])
                        send_photo(vk_ses, event.user_id, *upload_photo(upload, material_list[material_translate[i]]))
                        output = 1
                        break
                if output == 0:        
                    write_msg(event.user_id, info_help)
                
            else:
                write_msg(event.user_id, help_text)
