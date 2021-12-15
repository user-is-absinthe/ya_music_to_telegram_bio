import asyncio
import time

import telethon
from yandex_music import Client

from secret_config import TG_API_ID
from secret_config import TG_API_HASH
from secret_config import YA_TOKEN
from secret_config import SESSION_NAME

TIME_TO_WAIT = 15
TG_BIO_LEN = 70


def time_in_the_city(city_name: str):
    need_city = time.strftime("Today %d.%m.%Y; now in {0} %H:%M.", time.localtime())
    return need_city.format(city_name)


def get_music(client):
    queues = client.queues_list()
    if len(queues) == 0:
        # нет очередей просушивания
        return -1, -1, -1
    # Последняя проигрываемая очередь всегда в начале списка
    last_queue = client.queue(queues[0].id)
    if len(last_queue.tracks) == 0:
        # нет треков в последней очереди прослушивания, например слушает "мою волну"
        return -1, -1, -1
    last_track_id = last_queue.get_current_track()
    last_track = last_track_id.fetch_track()
    track_id = last_track_id.track_id
    title = last_track.title
    # artists = last_track.artists_name()
    # artists = ', '.join(last_track.artists_name())
    duration = last_track.duration_ms / 1000
    return title, track_id, duration


async def change_tg_bot(line: str):
    async with telethon.TelegramClient(SESSION_NAME, TG_API_ID, TG_API_HASH) as client:
        await client(telethon.functions.account.UpdateProfileRequest(about=line))


def main():
    client = Client(YA_TOKEN, report_new_fields=False)
    next_track_time = -1
    last_track_id = ''
    last_minute = time.localtime().tm_min
    while True:
        time.sleep(TIME_TO_WAIT)

        music_info = get_music(client=client)
        now_track_id = music_info[1]

        if music_info == (-1, -1, -1):
            this_line = time_in_the_city('Moscow')
            next_track_time = -1
            last_track_id = ''
        elif now_track_id != last_track_id:
            # time.time() < next_track_time
            this_line = '🎧 {0}: https://music.yandex.com/track/{1}'.format(
                music_info[0],
                music_info[1],
            )
            if len(this_line) >= 70:
                this_line = '🎧: https://music.yandex.com/track/{0}'.format(
                    music_info[1],
                )
            next_track_time = time.time() + music_info[2]
            last_track_id = now_track_id
        elif time.time() <= next_track_time:
            # this_line = time_in_the_city('Moscow')
            continue
        elif last_minute == time.localtime().tm_min:
            continue
        else:
            # this_line = 'Something went wrong.'
            this_line = time_in_the_city('Moscow')

        # print(this_line)
        # print(len(this_line))
        try:
            asyncio.run(change_tg_bot(this_line))
        except telethon.errors.FloodWaitError as e:
            time.sleep(e.seconds)
        except telethon.errors.rpcerrorlist.AboutTooLongError as e:
            # слишком длинное описание, скорее всего изз-за музыки
            time.sleep(TIME_TO_WAIT)
            pass


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        asyncio.run(change_tg_bot(''))
    finally:
        print('exit')
