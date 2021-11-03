from yandex_music import Client

# from secret_config import LOGIN
# from secret_config import PASSWORD
from secret_config import TOKEN_MUSIC


# client = Client.from_credentials(LOGIN, PASSWORD)
client = Client(TOKEN_MUSIC)

queues = client.queues_list()
# Последняя проигрываемая очередь всегда в начале списка
last_queue = client.queue(queues[0].id)

last_track_id = last_queue.get_current_track()
last_track = last_track_id.fetch_track()

track_id = last_track_id.track_id

duration_last_track = last_track.duration_ms / 1000

print(duration_last_track)

print(f'Ссылка на трек: https://music.yandex.com/track/{ track_id }')

artists = ', '.join(last_track.artists_name())
title = last_track.title
print(f'Сейчас играет: {artists} - {title}')


# а тут надо помнить,
# что ограничение на длину био -
# 120 символов, а я туда еще хочу ссылку затолкать...
# впрочем, для тестового примера хватило длины в 97 с учетом ссылки

