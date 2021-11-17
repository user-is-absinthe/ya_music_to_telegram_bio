import asyncio
import time

import telethon

# from telethon import TelegramClient
# from telethon import functions
# from telethon import errors

from secret_config import TG_API_ID
from secret_config import TG_API_HASH


TIME_TO_WAIT = 15

# api_id = 1586339
# api_hash = '52dcf6e77d0dab47c918261e7532d6b1'

# client = telethon.TelegramClient('clacson_session', TG_API_ID, TG_API_HASH)
# client.start()
#
# print(client.get_me().stringify())


def camel_case(line: str, last_index: int = -1):
    print(last_index)
    last_index += 1
    if last_index == len(line):
        last_index = 0
    line = line.lower()
    new_line = ''
    for index, letter in enumerate(line):
        if index == last_index:
            new_line += letter.upper()
        else:
            new_line += letter
    return new_line, last_index


def time_in_the_city(city_name: str):
    # need_city = time.strftime("Сегодня %d.%m.%Y; в {0} сейчас %H:%M.", time.gmtime())
    need_city = time.strftime("Today %d.%m.%Y; now in {0} %H:%M.", time.localtime())
    return need_city.format(city_name)


async def main(line: str):
    async with telethon.TelegramClient('clacson_session', TG_API_ID, TG_API_HASH) as client:
        # client(telethon.tl.functions.account.UpdateProfileRequest(about='test'))
        await client(telethon.functions.account.UpdateProfileRequest(about=line))
        # client
        # print(line)

# async def re_tg():
#     with TelegramClient('clacson_session', TG_API_ID, TG_API_HASH) as client:
#         # client(telethon.tl.functions.account.UpdateProfileRequest(about='test'))
#         client(telethon.functions.account.UpdateProfileRequest(about='test'))
#
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(re_tg())
#     loop.close()

this_index = -1
# i = 0
while True:
    this_index += 1
    if this_index * TIME_TO_WAIT % 60 == 0:
        print(time_in_the_city('Moscow'))
    if this_index == 100:
        this_index = -1
    # this_line, this_index = camel_case('test description', this_index)
    this_line = time_in_the_city('Moscow')
    try:
        asyncio.run(main(this_line))
    except telethon.errors.FloodWaitError as e:
        print(f'Need to wait: { e.seconds }')
        # print(e.seconds)
        time.sleep(e.seconds)
    time.sleep(TIME_TO_WAIT)

    # print(i)
    # i += 1

