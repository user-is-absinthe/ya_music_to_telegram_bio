# import asyncio

import telethon

from telethon import TelegramClient

from secret_config import TG_API_ID
from secret_config import TG_API_HASH

# api_id = 1586339
# api_hash = '52dcf6e77d0dab47c918261e7532d6b1'

# client = telethon.TelegramClient('clacson_session', TG_API_ID, TG_API_HASH)
# client.start()
#
# print(client.get_me().stringify())

with TelegramClient('clacson_session', TG_API_ID, TG_API_HASH) as client:
    # client(telethon.tl.functions.account.UpdateProfileRequest(about='test'))
    result = client(telethon.functions.account.UpdateProfileRequest(about='test'))
    # await client
    print(result)

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

