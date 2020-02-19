import random

import requests
from io import BytesIO

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.upload import VkUpload
from vk_api.utils import get_random_id

from commander.commander import Commander


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


token = "6da505bf6faea32f5b4d8f52cd6f89509d0cbf5b0f74d3743a21b7f1516022c02ce81a1fac7198005a5b6"

vk = vk_api.VkApi(token=token)

vk_ses = vk.get_api()

upload = VkUpload(vk)

ne_ponyal = ['https://yt3.ggpht.com/a/AGF-l7_i56GQZf-s9TMplzzJFClNljRuc-CU3Oi2=s900-c-k-c0xffffffff-no-rj-mo', 
             'https://pbs.twimg.com/media/D7l_DcGXYAIsHq5.jpg',
             'https://i.ytimg.com/vi/EXyn3Xm4QI8/maxresdefault.jpg',
             'https://i1.sndcdn.com/artworks-000329585706-s0jmhb-t500x500.jpg']

longpoll = VkLongPoll(vk)

commander = Commander()

how_are_you_answer = ['Отлично!', "Я сегодня не в настроении", "Суперски", "Я еще не определился"]

print("Бот запущен")
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            request = event.text
            request = request.strip().lower()
            if "привет" in request:
                write_msg(event.user_id, "Доброго времени суток!")
            elif "пока" in request:
                write_msg(event.user_id, "Ну слава богу ты ушел")
            elif "как дела" in request:
                write_msg(event.user_id, how_are_you_answer[random.randint(0, 3)])
            elif request.split()[0] == "command":
                write_msg(event.user_id, commander.do(request[8::]))
            else:
                send_photo(vk_ses, event.user_id, *upload_photo(upload, ne_ponyal[random.randint(0, 3)]))

