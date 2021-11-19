import sys

from yandex_music import Client

# from secret_config import LOGIN
# from secret_config import PASSWORD
from secret_config import YA_TOKEN


# client = Client.from_credentials(LOGIN, PASSWORD)
client = Client(YA_TOKEN, report_new_fields=False)

queues = client.queues_list()
print(queues)
print('\n')
if len(queues) == 0:
    print('Очередь прослушивания куда-то потерялась.')
    sys.exit(1)

for q in queues:
    data = client.queue(q.id)
    print(data)

# sys.exit(1)

# Последняя проигрываемая очередь всегда в начале списка
last_queue = client.queue(queues[0].id)

print(queues[0].id)

print(last_queue)

if len(last_queue.tracks) == 0:
    sys.exit(1)
# sys.exit(1)

last_track_id = last_queue.get_current_track()
last_track = last_track_id.fetch_track()

track_id = last_track_id.track_id  # return str

# print(track_id, type(track_id))

duration_last_track = last_track.duration_ms / 1000

print(duration_last_track)

print(f'Ссылка на трек: https://music.yandex.com/track/{ track_id }')

artists = ', '.join(last_track.artists_name())
title = last_track.title
line = f'Сейчас играет: { artists } - { title }: https://music.yandex.com/track/{ track_id }'
print(line)
print(len(line))


# а тут надо помнить,
# что ограничение на длину био -
# 120 символов, а я туда еще хочу ссылку затолкать...
# впрочем, для тестового примера хватило длины в 97 с учетом ссылки

