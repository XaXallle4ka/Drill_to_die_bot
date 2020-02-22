from parser_things import __ParseItems, find_item_cost, find_item_description

items = __ParseItems()

info_help = ('Напиши "Инфо" + обьект из списка:\nИСКОПАЕМЫЕ\n1. Камень\n2. Железо\n3. Золото\n 4. Иридий' + 
             '\n5. Белый кристалл\n6. Зеленый кристалл\n7. Красный кристалл\nКОРАБЛИ\n1. Бетти\n2. Апполо\n3. Хексагон')

command_list = "Список комманд:\n1. Как дела\n2. Привет\n3. Пока\n4. Инфо\n5. Крол"

hello = "Доброго времени суток!"
bye = "Бай бай)"

help_text = "Не понимаю тебя, напиши 'помощь', чтобы узнать список команд"

token = "6da505bf6faea32f5b4d8f52cd6f89509d0cbf5b0f74d3743a21b7f1516022c02ce81a1fac7198005a5b6"

ne_ponyal = ['https://yt3.ggpht.com/a/AGF-l7_i56GQZf-s9TMplzzJFClNljRuc-CU3Oi2=s900-c-k-c0xffffffff-no-rj-mo', 
             'https://pbs.twimg.com/media/D7l_DcGXYAIsHq5.jpg',
             'https://i.ytimg.com/vi/EXyn3Xm4QI8/maxresdefault.jpg',
             'https://i1.sndcdn.com/artworks-000329585706-s0jmhb-t500x500.jpg']

how_are_you_answer = ['Отлично!', "Я сегодня не в настроении", "Суперски", "Я еще не определился"]

material_list = {'stone': 'https://sun9-60.userapi.com/c855332/v855332998/1fd3e5/-oMj0Y7VKB0.jpg',
                 'ferrum': 'https://sun9-11.userapi.com/c855332/v855332998/1fd3d3/FMgj5nE0pIM.jpg',
                 'gold': 'https://sun9-69.userapi.com/c855332/v855332998/1fd3b8/-4d0o7lQ-NM.jpg',
                 'iridium': 'https://sun9-31.userapi.com/c855332/v855332998/1fd3ca/bXO_eOQQHOE.jpg',
                 'whitecrystall': 'https://sun9-61.userapi.com/c855332/v855332998/1fd3ee/d63alj4JAs0.jpg',
                 'greencrystall': 'https://sun9-60.userapi.com/c855332/v855332998/1fd3c1/319UL5OZ_zk.jpg',
                 'redcrystall': 'https://sun9-34.userapi.com/c855332/v855332998/1fd3dc/dg9DCzpPZIY.jpg'}
                 
material_description = {'stone': 'Камень:\nСредняя цена - ' + str(find_item_cost('Stone', items)) + '\nШанс на получение - Очень высокий\nОписание:\n' + find_item_description('Stone', items),
                        'ferrum': 'Железо:\nСредняя цена - ' + str(find_item_cost('Ferrum', items)) + '\nШанс на получение - Высокий\nОписание:\n' + find_item_description('Ferrum', items),
                        'gold': 'Золото:\nСредняя цена - ' + str(find_item_cost('Gold', items)) + '\nШанс на получение - Средний\nОписание:\n' + find_item_description('Gold', items),
                        'iridium': 'Иридий:\nСредняя цена - ' + str(find_item_cost('Iridium', items)) + '\nШанс на получение - Низкий\nОписание:\n' + find_item_description('Iridium', items),
                        'whitecrystall': 'Белый кристалл:\nСредняя цена - ' + str(find_item_cost('WhiteCrystal', items)) + '\nШанс на получение - Безумно маленький\nОписание:\n' + find_item_description('WhiteCrystal', items),
                        'greencrystall': 'Зеленый кристалл:\nСредняя цена - ' + str(find_item_cost('GreenCrystal', items)) + '\nШанс на получение - Крайне маленький\nОписание:\n' + find_item_description('GreenCrystal', items),
                        'redcrystall': 'Красный кристалл:\nСредняя цена - ' + str(find_item_cost('RedCrystal', items)) + '\nШанс на получение - Очень маленький\nОписание:\n' + find_item_description('RedCrystal', items)}

material_translate = {'камень': 'stone',
                      'железо': 'ferrum',
                      'золото': 'gold',
                      'иридий': 'iridium',
                      'белый кристалл': 'whitecrystall',
                      'зеленый кристалл': 'greencrystall',
                      'красный кристалл': 'redcrystall'}