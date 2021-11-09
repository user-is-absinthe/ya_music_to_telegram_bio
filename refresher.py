import time

import yandex_music
import telethon
from telethon import TelegramClient

from secret_config import YA_TOKEN
from secret_config import TG_API_ID
from secret_config import TG_API_HASH


def get_last_music(token: str = YA_TOKEN):
    client = yandex_music.Client(YA_TOKEN)
    queues = client.queues_list()
    if len(queues) == 0:
        return ''
    # Последняя проигрываемая очередь всегда в начале списка
    last_queue = client.queue(queues[0].id)
    last_track_id = last_queue.get_current_track()
    last_track = last_track_id.fetch_track()
    track_id = last_track_id.track_id
    duration = last_track.duration_ms / 1000
    # print(f'Ссылка на трек: https://music.yandex.com/track/{track_id}')
    artists = ', '.join(last_track.artists_name())
    title = last_track.title
    # line = f'Сейчас играет: {artists} - {title}: https://music.yandex.com/track/{track_id}'
    # print(line)
    # print(len(line))
    return duration, artists, title


def update_tg_status(
        api_id: str = TG_API_ID,
        api_hash: str = TG_API_HASH,
        line_to_update: str = ''
):
    pass


def main():
    len_track_sec = 0
    while True:
        get_last_music()
    pass


if __name__ == '__main__':
    main()
